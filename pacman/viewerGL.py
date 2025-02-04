#!/usr/bin/env python3

import OpenGL.GL as GL
import glfw
import pyrr
import numpy as np
import time
from cpe3d import Object3D, Text
from mesh import Mesh

class ViewerGL:
    def __init__(self):
        # initialisation de la librairie GLFW
        glfw.init()
        # paramétrage du context OpenGL
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        # création et paramétrage de la fenêtre
        glfw.window_hint(glfw.RESIZABLE, False)
        self.window = glfw.create_window(800, 800, 'OpenGL', None, None)
        # paramétrage de la fonction de gestion des évènements
        glfw.set_key_callback(self.window, self.key_callback)
        # activation du context OpenGL pour la fenêtre
        glfw.make_context_current(self.window)
        glfw.swap_interval(1)
        # activation de la gestion de la profondeur
        GL.glEnable(GL.GL_DEPTH_TEST)
        # choix de la couleur de fond
        GL.glClearColor(0.5, 0.6, 0.9, 1.0)
        print(f"OpenGL: {GL.glGetString(GL.GL_VERSION).decode('ascii')}")

        self.objs = []
        self.touch = {}
        self.ko = False

    def run(self, vao_text, programGUI_id, texture_text):
        # boucle d'affichage
        while not glfw.window_should_close(self.window) :
            # nettoyage de la fenêtre : fond et profondeur
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

            self.update_key()
            self.fantomas()

            for obj in self.objs:
                GL.glUseProgram(obj.program)
                if isinstance(obj, Object3D):
                    self.update_camera(obj.program)
                obj.draw()

            # changement de buffer d'affichage pour éviter un effet de scintillement
            glfw.swap_buffers(self.window)
            # gestion des évènements
            glfw.poll_events()

            if self.ko == True :
                o = Text('Vous avez perdu !', np.array([-0.8, 0.3], np.float32), np.array([0.8, 0.8], np.float32), vao_text, 2, programGUI_id, texture_text)
                self.add_object(o) # va amener la fermeture de la fenêtre (à cause d'une erreur)
                time.sleep(2)
        
    def key_callback(self, win, key, scancode, action, mods):
        # sortie du programme si appui sur la touche 'échappement'
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(win, glfw.TRUE)
        self.touch[key] = action
    
    def add_object(self, obj):
        self.objs.append(obj)

    def set_camera(self, cam):
        self.cam = cam

    def update_camera(self, prog):
        GL.glUseProgram(prog)
        # Récupère l'identifiant de la variable pour le programme courant
        loc = GL.glGetUniformLocation(prog, "translation_view")
        # Vérifie que la variable existe
        if (loc == -1) :
            print("Pas de variable uniforme : translation_view")
        # Modifie la variable pour le programme courant
        translation = -self.cam.transformation.translation
        GL.glUniform4f(loc, translation.x, translation.y, translation.z, 0)

        # Récupère l'identifiant de la variable pour le programme courant
        loc = GL.glGetUniformLocation(prog, "rotation_center_view")
        # Vérifie que la variable existe
        if (loc == -1) :
            print("Pas de variable uniforme : rotation_center_view")
        # Modifie la variable pour le programme courant
        rotation_center = self.cam.transformation.rotation_center
        GL.glUniform4f(loc, rotation_center.x, rotation_center.y, rotation_center.z, 0)

        rot = pyrr.matrix44.create_from_eulers(-self.cam.transformation.rotation_euler)
        loc = GL.glGetUniformLocation(prog, "rotation_view")
        if (loc == -1) :
            print("Pas de variable uniforme : rotation_view")
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, rot)
    
        loc = GL.glGetUniformLocation(prog, "projection")
        if (loc == -1) :
            print("Pas de variable uniforme : projection")
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, self.cam.projection)

    def update_key(self):
        disp = pyrr.Vector3()
        if glfw.KEY_UP in self.touch and self.touch[glfw.KEY_UP] > 0 :
            disp -= pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0, 0, 0.5]))
        if glfw.KEY_DOWN in self.touch and self.touch[glfw.KEY_DOWN] > 0 :
            disp += pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0, 0, 0.5]))

        if not self.collision(self.objs[0].transformation.translation + disp):
            self.objs[0].transformation.translation += disp

        if glfw.KEY_LEFT in self.touch and self.touch[glfw.KEY_LEFT] > 0 :
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] -= 0.1
        if glfw.KEY_RIGHT in self.touch and self.touch[glfw.KEY_RIGHT] > 0 :
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] += 0.1

        if glfw.KEY_C in self.touch and self.touch[glfw.KEY_C] > 0:  # permet de remettre le pac man
            m = Mesh.load_obj('real_pacman.obj')
            m.normalize()
            m.apply_matrix(pyrr.matrix44.create_from_scale([1, 1, 1, 1]))
            self.objs[0].transformation.translation.x = 0
            self.objs[0].transformation.translation.y = -np.amin(m.vertices, axis=0)[1] # place l'objet à ras du sol 
            self.objs[0].transformation.translation.z = -22
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] = np.pi # place le personnage dans le bon sens sur le plateau
            self.objs[0].transformation.rotation_center.z = 0.2

        self.cam.transformation.rotation_euler = self.objs[0].transformation.rotation_euler.copy() + pyrr.Vector3([np.pi/4, 0, 0])
        self.cam.transformation.rotation_euler[pyrr.euler.index().roll] += np.pi/10
        self.cam.transformation.rotation_center = self.objs[0].transformation.translation + self.objs[0].transformation.rotation_center
        self.cam.transformation.translation = self.objs[0].transformation.translation + pyrr.Vector3([0, 2, 12])

    def fantomas(self) :
        for obj in self.objs[-7:-1] :
            diff_position = self.objs[0].transformation.translation-obj.transformation.translation
            l = pyrr.vector3.length(diff_position)
            if l < 1 :
                # Collisions entre les fantômes et le joueur
                self.ko = True
            else : # déplace le fantôme en direction du joueur
                obj.transformation.translation += 0.05*diff_position/l

    def collision(self, p) :
        pos_player_x = p.x
        pos_player_z = p.z
        for object in self.objs[1:659] :
            pos_objec_x = object.transformation.translation.x
            dist_x = abs(pos_player_x - pos_objec_x)
            pos_object_z = object.transformation.translation.z
            dist_z = abs(pos_player_z - pos_object_z)
            if dist_x < 0.7 and dist_z < 0.7 :
                return True
        return False