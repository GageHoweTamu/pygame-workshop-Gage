import pygame

from components.player import *
from components.block import *
from components.enemy import *


class gameScreen:
    def __init__(self, screen, res):
        """basic attributes"""
        self.screen = screen
        self.res = res

        """game data"""

        """creates the map and gives default position"""

        """create player sprite"""

        """create enemy sprites"""

        """create pipe sprite"""

        """create platform sprite"""

        """create item sprite"""

        """fireball sprite"""

        """ For convienence """

    def input(self, p, m, w, rb):
        # detect key press
        """Right key pressed"""
        # update player facing direction
        # make sure movement isn't being blocked (p.blocked)
        # if player is on the leftmost edge of map and not halfway up OR
        # if player is on the rightmost edge of map and not halfway down
        # +5 for reentry purposes exiting edge will result in p.rect.x == width/2
        # otherwise move the map

        """Left key pressed"""
        # same logic when moving left

        """Shoot fireball key (x or j) pressed"""
        # check that ability is activated and fireball doesn't already exist
        # middleish coordinates of player (x+6.5, y+5)
        """Up key pressed"""
        # set jump to true

        pass

    def logic(self, p, m, w, rb):
        """set win to true if player passes castle door"""
        # player should be 130 px left of right side of screen

        """check holes"""
        #holeCoords = [(-745, -755), (-1015, -1040), (-2090, -2095)]
        # loop through to see if player has fallen in hole
        # check if player is in the right position

        """applies gravity to item as long as it's above ground level"""
        pass

    def collisions(self, p):
        """if player collides with platform tiles cancel jumping and break block"""

        """if player collides with mystery block show item"""

        """ player collision with item (add additional condition for item to be on ground level)"""

        """ enemy collision detection (loop through for each enemy)"""
            #enemy and player
            #enemy and fireball
            #enemy and pipe


        """ pipes collision detection (loop through for each pipe)"""
        #collision_tolerance = 6
            #if player is colliding with pipe
                # if player bottom is somewhere near top of pipe set on pipe to true
                #otherwise block ALL movement
                    # blocked should = 2 if to the left else it should be 1
            #if fireball collides with pipe disperse the fireball
        pass


    def run(self):
        """scale any image/sprites"""
        self.player.image = pygame.transform.scale(self.player.image, (23, 26))
        for block in self.platform:
            block.image = pygame.transform.scale(block.image, (21, 21))
        self.fireball.image = pygame.transform.scale(
            self.fireball.image, (18, 18))

        """draws map, player, enemies, items, and misc. blocks as sprites"""
        # draw item only if player collides with item
        # draw fireball only if it's being fired and ability is true

        """keep running basic updates as long as no win and no lose (include player and enemy specific functions)"""
