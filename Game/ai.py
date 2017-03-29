import random

# Class for controlling AI Pong Paddle
class AI(object):
    def __init__(self, ball_x, ball_y):
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.rand = random.randint(1, 200)   # this was not really used

    # Function that peforms calculations to move ai paddle 
    def move_paddle(self):
        #return self.ball_y - self.rand
        return self.ball_x - 30