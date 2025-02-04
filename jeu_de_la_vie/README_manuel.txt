Le jeu de la vie----------------
Url     : http://codes-sources.commentcamarche.net/source/100911-le-jeu-de-la-vieAuteur  : lespinxDate    : 20/05/2015
Licence :
=========

Ce document intitul� � Le jeu de la vie � issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis � disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fix�es par la licence, tant que cette note
appara�t clairement.

Description :
=============

Bien que le code &quot;Jeu de la vie&quot; soit d�j� pr�sent plusieurs fois sur 
CCM/Codes-Sources, je poste � mon tour une nouvelle version.
<br />La particula
rit� du &quot;Jeu de la vie&quot; est qu'il n'y a pas de joueurs!
<br />L'histo
rique et les r�gles du jeu sont tr�s bien expliqu�es sur Wikipedia (automate cel
lulaire, jeu de la vie...)
<br />
<br />Infos:
<br />Compatible Python 2 et 3

<br />Test� avec Python 2.7.3 et Python 3.3.5 dans l'environnement Windows 7 6
4 bits avec un �cran 23&quot; 1080x1920
<br />-- Ajout le 11/02/2015
<br />-- 
Modifi� le 29/04/2015 : Optimisation du code et ajout de fonctionnalit�s.
<br /
>-- Modifi� le 01/05/2015 : Correction d'un bug.
<br />-- Modifi� le 17/05/2015
 : Ajout de fonctionnalit� (Acc�l�rer)
<br />
<br />Utilisation:
<br />En fon
ction de la taille et de la r�solution de votre �cran vous devrez, peut-�tre, ad
apter les valeurs par d�faut qui d�terminent la dimension de la grille.
<br />P
our cela, dans la section &quot;__init__&quot; vous interviendrez sur la variabl
e &quot;self.H_appli_diff&quot; (En pixels, estimation de la hauteur de l'�cran 
- hauteur de la grille)
<br />La dimension de la grille est fixe, augmenter ou 
diminuer la taille d'une cellule augmentera ou diminuera le nombre de cellules p
ar ligne/colonne.
<br />
<br />Ajouter une cellule = clic gauche
<br />Suppri
mer une cellule = clic droit
<br />
<br />Le contr�le &quot;Ralentir&quot; per
met de temporiser l'affichage des g�n�rations successives (en milli�mes de secon
de)
<br />L'affichage en mode pas � pas est possible en s�lectionnant &quot;Man
uel&quot; dans le contr�le &quot;Ralentir&quot;
<br />
<br />Le contr�le &quot
;Acc�l�rer&quot; permet une pseudo acc�l�ration de l'affichage des g�n�rations s
uccessives. 
<br />(1 = affichage � chaque g�n�ration  / 2 = affichage toutes l
es 2 g�n�rations ..... / 10 = affichage toutes les 10 g�n�rations)
<br />
<br 
/>Un clic sur un des choix du contr�le &quot;Motifs&quot; affichera le motif dan
s la grille et vous lancerez l'affichage des g�n�rations en appuyant sur le bout
on &quot;D�marrer&quot;
<br />Un double clic effacera le motif.
<br />Pour sau
vegarder vos motifs personnels, renseignez la zone de saisie avec le nom du nouv
eau motif et validez par &quot;Entree&quot;
<br />Les motifs sont sauvegard�s d
ans 2 fichiers &quot;JDV_Motifs_V2.pickle&quot; et &quot;JDV_Motifs_V3.pickle&qu
ot; selon la version Python utilis�e.
<br />
<br />Le bouton &quot;Arreter&quo
t; interrompt l'affichage des g�n�rations, un nouvel appui sur &quot;D�marrer&qu
ot; reprend le traitement en cours.
<br />
<br />Le bouton &quot;Import Motifs
&quot; permet d'ex�cuter des motifs (norme Life 1.05) depuis une bibioth�que ext
�rieure et disponible sur Internet.
<br />Le chemin d'acc�s, par d�faut, � cett
e biblioth�que est d�fini dans la section &quot;__init__&quot; par la variable &
quot;self.chemin_motifs&quot;
<br />Exemple de biblioth�que � t�l�charger: <a h
ref='http://www.conwaylife.com/wiki/Main_Page' rel='nofollow' target='_blank'>ht
tp://www.conwaylife.com/wiki/Main_Page</a> et clic sur le bouton &quot;Download 
pattern collection&quot;
<br />
<br />Lorsqu'une cellule atteint un des bords 
de la grille, un effet de zoom est appliqu�. Cet effet s'arr�te lorsque la taill
e de la cellule est inf�rieure � 1 pixel.
<br />Certains motifs (Puffer_01 ou P
uffer_02 par exemple) n�cessitent d'attendre jusqu'� environ 1000 g�n�rations et
 1/2 million de cellules pour voir apparaitre des effets int�ressants. 
