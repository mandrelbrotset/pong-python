import pygame
from pygame.locals import *
import random
import time
from . import ai as ai_paddle

class Pong(object):
    def __init__(self,width,height):
        pygame.init()
        pygame.display.set_caption("Pong - version 2.0")
        self.display_width = width
        self.display_height = height
        self.display = pygame.display.set_mode((self.display_width, self.display_height))
        self.bg_color = (44, 62, 80)
        self.ball_x = random.randint(300, 340)
        self.ball_y = random.randint(0, 50)
        self.left_paddle_mv = self.right_paddle_mv = self.centery = 240
        self.ball_side = 15
        self.color = (41,128,185)
        self.color_1 = (18,170,40) 
        self.color_2 = (255,200,200)
        self.color_3 = (149,165,166) 
        self.direction = [1,1]
        self.speed = 3;
        self.hit_edge_left = False
        self.hit_edge_right = False
        self.paddle_height = 75
        self.paddle_width = 10
        self.info_division_height = 5
        # make height of information area 10% of window height
        self.info_area = (0.1 * self.display_height)  
        self.game_area_top = self.info_area
        self.game_area_bottom = self.display_height 
        #self.ball_rect = pygame.Rect(self.ball_x,self.ball_y,
        #                        self.ball,self.ball)
        self.score = [0, 0]

    def info(self):
        ## division
        # y coordinate for division line
        self.info_division_y = self.info_area - 5
        # draw divider
        pygame.draw.rect(self.display, self.color_3,
                        (0, self.info_division_y, 
                         self.display_width, self.info_division_height))
        
        ## printing scores 
        pygame.font.init()
        font = pygame.font.SysFont("agencyfb", 20)
        # score for left paddle
        left_label = font.render("%d" %self.score[0], 1, self.color_3)
        self.display.blit(left_label, (45, 13))
        # score for right paddle
        right_label = font.render("%d" %self.score[1], 1, self.color_3)
        self.display.blit(right_label, (596, 13))
        # reset instruction
        reset_label = font.render("Press Enter or Space to reset", 1, self.color_3)
        self.display.blit(reset_label, (240, 2))
        # quit instruction
        quit_label = font.render("Press Escape to quit", 1, self.color_3)
        self.display.blit(quit_label, (267, 20))


    def fill(self):
        self.display.fill(self.bg_color)

     # Paddle at the right side
    def right_paddle(self, ai=None):    #set ai = 1 or anything to make ai control the paddle  
        # for user  
        if ai == None: 
            key = pygame.key.get_pressed()
            if key[K_UP]:
                self.right_paddle_mv = self.right_paddle_mv - 4
            if key[K_DOWN]:
                self.right_paddle_mv = self.right_paddle_mv + 4

        # for AI
        else:
            self.ai = ai_paddle.AI(self.ball_x,self.ball_y)
            self.right_paddle_mv = self.ai.move_paddle()

        # limit the posible y positons so that paddle doesn't go off window
        if self.right_paddle_mv <= self.game_area_top:
            self.right_paddle_mv = self.game_area_top
        if self.right_paddle_mv + self.paddle_height >= self.game_area_bottom:
            self.right_paddle_mv = self.game_area_bottom - self.paddle_height

        # draw right paddle as we update its y position
        pygame.draw.rect(self.display, self.color,
                         (self.display_width - self.paddle_width,    # for right oaddle to be at far right of the window
                         self.right_paddle_mv, self.paddle_width, self.paddle_height)
                        )

    # Paddle at the left side
    def left_paddle(self, ai = 1):     # set ai = None, if there are two human users
        # for user
        if ai == None: 
            key = pygame.key.get_pressed()
            if key[K_w]:
                self.left_paddle_mv = self.left_paddle_mv - 4
            if key[K_s]:
                self.left_paddle_mv = self.left_paddle_mv + 4

        # for AI
        else:
            self.ai = ai_paddle.AI(self.ball_x,self.ball_y)
            self.left_paddle_mv = self.ai.move_paddle()

        # limit the posible y positons so that paddle doesn't go off window 
        if self.left_paddle_mv <= self.game_area_top:
            self.left_paddle_mv = self.game_area_top
        if self.left_paddle_mv + self.paddle_height >= self.game_area_bottom:
            self.left_paddle_mv = self.game_area_bottom - self.paddle_height

        # draw left paddle as we update its y position
        pygame.draw.rect(self.display, self.color_1,
                         (0,         # 0 because paddle is on far left of the window
                         self.left_paddle_mv, self.paddle_width, self.paddle_height)
                        )     

    def update_puck(self):
        self.ball_x += self.speed * self.direction[0]
        self.ball_y += self.speed * self.direction[1]
    
        self.ball_rect = pygame.Rect(self.ball_x,self.ball_y,
                                self.ball_side,self.ball_side)

        # Change direction of puck if it hits the right paddle
        if (self.ball_rect.right >= self.display_width - self.paddle_width) and (self.ball_rect.right <= self.display_width - 1):
            if (self.ball_rect.top - 10 >= self.right_paddle_mv) and (self.ball_rect.bottom - 10 <= self.right_paddle_mv + 75):
                self.direction[0] = -1

        # If puck hits right side, change direct of puck
        # set variable for score keeping to True 
        if (self.ball_rect.right >= self.display_width):
            self.direction[0] = -1
            self.hit_edge_left = True
       
        # Change direction of puck if it hits the left paddle
        if (self.ball_rect.left <= self.paddle_width) and (self.ball_rect.left >= 0):
            if (self.ball_rect.top - 10 >= self.left_paddle_mv) and (self.ball_rect.bottom - 10 <= self.left_paddle_mv + 75):
                self.direction[0] = 1

        # If puck hits left side, change direct of puck
        # set variable for score keeping to True 
        if(self.ball_rect.left <= 0):
            self.direction[0] = 1
            self.hit_edge_right = True

        # change direction of puck when it hits the top or bottom 
        # for top
        if self.ball_rect.top <= self.game_area_top:
            self.direction[1] = 1
        # for bottom
        if self.ball_rect.bottom >= self.game_area_bottom:
            self.direction[1] = -1 

		# draw puck!
        pygame.draw.rect(self.display, self.color_2, 
                         (self.ball_x, self.ball_y, self.ball_side, self.ball_side)
                        )
        
        tally = [0, 0]
        if self.hit_edge_left:
            tally[0] += 1
            self.hit_edge_left = False
        if self.hit_edge_right:
            tally[1] += 1
            self.hit_edge_right = False
        
        self.score[0] = self.score[0] + tally[0]
        self.score[1] = self.score[1] + tally[1]

        ## You can uncomment these three lines to see the scores in the commandline
        #print("[STATUS]  Left has %d point(s)" %self.score[0])
        #print("[STATUS]  Right has %d point(s)" %self.score[1])
        #print("[ INFO ]  Press Space bar or Enter to reset game")

    def reset(self):
        # 
        key = pygame.key.get_pressed()

        # On pressing Return/Enter or Escape key, reset game 
        if key[K_RETURN] or key[K_SPACE]:
            self.ball_x = random.randint(300, 340)
            self.ball_y = random.randint(0, 50)
            self.left_paddle_mv = self.right_paddle_mv = random.randint(300,340)
            self.direction = [1, 1]
            self.score = [0, 0]
            time.sleep(1)

    # Code task come here to implement score function
    # It will display the score of both players
    #def score(self):