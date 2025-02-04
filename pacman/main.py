from viewerGL import ViewerGL
import glutils
from mesh import Mesh
from cpe3d import Object3D, Camera, Transformation3D, Text
import numpy as np
import OpenGL.GL as GL
import pyrr

def main():
    viewer = ViewerGL()

    viewer.set_camera(Camera())
    viewer.cam.transformation.translation.x = 10
    viewer.cam.transformation.translation.y = 2
    viewer.cam.transformation.translation.z = 0
    viewer.cam.transformation.rotation_center = viewer.cam.transformation.translation.copy()

    program3d_id = glutils.create_program_from_file('shader.vert', 'shader.frag')
    programGUI_id = glutils.create_program_from_file('gui.vert', 'gui.frag')

    # Objet principal, à la première personne
    m = Mesh.load_obj('real_pacman.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([1, 1, 1, 1]))
    tr = Transformation3D()
    tr.translation.x = 0
    tr.translation.y = -np.amin(m.vertices, axis=0)[1]  # place l'objet à ras du sol 
    tr.translation.z = -22
    tr.rotation_euler[pyrr.euler.index().yaw] = np.pi # place le personnage dans le bon sens sur le plateau
    tr.rotation_center.z = 0.2
    texture = glutils.load_texture('texture_couleur_pacman.png')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, tr)
    viewer.add_object(o)

    # Objet cube, pour créer les murs
    m = Mesh.load_obj('cube.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([0.5, 2, 0.5, 1]))
    texture = glutils.load_texture('mur.jpg')
    vao = m.load_to_gpu()

    # ouvre le fichier labyrinthe pour former le plateau de jeu
    with open('labyrinthe.txt', 'r', encoding='utf-8') as fichier :
        lignes = [ligne.strip() for ligne in fichier]

    # crée tous les cubes en fonction du labyrinthe établi
    for i in range(len(lignes)) :
        for j in range(len(lignes[i])) :
            if lignes[i][j] == '0' :
                tr = Transformation3D()
                tr.translation.x = 25 - j
                tr.translation.y = -np.amin(m.vertices, axis=0)[1]
                tr.translation.z = 25 - i
                tr.rotation_center.z = 0.2
                o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, tr)
                viewer.add_object(o)
    
    # Objet fantôme
    m = Mesh.load_obj('fantome.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([1, 1, 1, 1]))
    vao = m.load_to_gpu()

    couleur = ["bleu", "orange", "rose", "rouge", "vert", "violet"]
    place_fantomes = [[-20,-20], [-20,0], [-20,20], [20,-20], [20,0], [20,20]]

    for i in range(6):
        tr = Transformation3D()
        tr.translation.x = place_fantomes[i][0]
        tr.translation.y = -np.amin(m.vertices, axis=0)[1]  # place l'objet à ras du sol 
        tr.translation.z = place_fantomes[i][1]
        if i < 3 : tr.rotation_euler[pyrr.euler.index().yaw] =  -3*np.pi/4 # place le personnage dans le bon sens sur le plateau
        else : tr.rotation_euler[pyrr.euler.index().yaw] =  np.pi/4
        tr.rotation_center.z = 0.2
        
        texture = glutils.load_texture("texture_couleur_%s.png" %couleur[i])
        o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, tr)
        viewer.add_object(o)

    # Objet plateau de jeu
    m = Mesh()
    p0, p1, p2, p3 = [-25, 0, -25], [25, 0, -25], [25, 0, 25], [-25, 0, 25]
    n, c = [0, 1, 0], [1, 1, 1]
    t0, t1, t2, t3 = [0, 0], [1, 0], [1, 1], [0, 1]
    m.vertices = np.array([[p0 + n + c + t0], [p1 + n + c + t1], [p2 + n + c + t2], [p3 + n + c + t3]], np.float32)
    m.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('map.jpg')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    viewer.add_object(o)

    vao_text = Text.initalize_geometry()
    texture_text = glutils.load_texture('fontB.jpg')

    viewer.run(vao_text, programGUI_id, texture_text)

if __name__ == '__main__':
    main()