import pygame
import pygame_menu
from pygame.locals import *


nombre_sprite_cote = 4
taille_sprite = 45
cote_fenetre = nombre_sprite_cote * taille_sprite




class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche,haut,bas):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			self.case_x += 1
			self.x = self.case_x * taille_sprite
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			self.case_x -= 1
			self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		#Déplacement vers le haut
		if direction == 'haut':
			self.case_y -= 1
			self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			self.case_y += 1
			self.y = self.case_y * taille_sprite
			self.direction = self.bas		



pygame.init()
surface = pygame.display.set_mode((960,540))

def start_the_game():
    pygame_menu.events.EXIT
    pygame.init()

    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((960,540))

    #Chargement et collage du fond
    fond = pygame.image.load("background.png").convert()
    fenetre.blit(fond, (0,0))

    #Chargement et collage du personnage
    perso = Perso("droite.png", "gauche.png", "haut.png", "bas.png")


    #Rafraîchissement de l'écran
    pygame.display.flip()

    #BOUCLE INFINIE
    continuer = 1
    while continuer:
		
        pygame.key.set_repeat(400, 30)
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                continuer = 0   
            if event.type == KEYDOWN:
                if event.key == K_DOWN:	
                    perso.deplacer('bas')
                if event.key == K_UP:	
                    perso.deplacer('haut')
                if event.key == K_RIGHT:

                    perso.deplacer('droite')
                if event.key == K_LEFT:	
                    perso.deplacer('gauche')

        fenetre.blit(fond, (0,0))	
        fenetre.blit(perso.direction, (perso.x, perso.y)) 
        #Rafraichissement
        pygame.display.flip()


menu = pygame_menu.Menu('ZoupleGame', 400, 300,
                       theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.text_input('Name : ', default='HibouxLegendaire')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)




