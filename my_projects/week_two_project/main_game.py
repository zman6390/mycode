import sys
import pygame

from sprites import *
from configuration import *


class Game:
    #initialize method in order for the game to run
    def __init__(self):
        pygame.init()
        #set the screen size for the game
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  
        #set the framerate for the game
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Impact', 32)
        self.running = True

    def new(self):
        #new game start
        self.playing = True
        #This allows us to select all heroes,walls,enemies,etc at the same time
        self.all_sprites = pygame.sprite.LayeredUpdates()
        #contains all the walls
        self.blocks = pygame.sprite.LayeredUpdates()
        #contains all the enemies
        self.enemies = pygame.sprite.LayeredUpdates()
        #contains all attacks
        self.attacks = pygame.sprite.LayeredUpdates()
        self.Player

    def update(self):

    def draw(self):

    def main(self):

    def
