import pygame as pg
import random
vec2 = pg.math.Vector2

class Food:
    def __init__(self):
        self.positions = [vec2(20,20),vec2(15,27)]

    def is_food(self, pos):
        for i in self.positions:
            if(i == pos):
                del self.positions[self.positions.index(pos)]
                #print("Food is at", pos)
                return True
        #print("No food at", pos)
        return False

    def make_food(self):
        self.positions.append(vec2(random.randint(5, 25), random.randint(5, 25)))

    def get_food_pos(self):
        return self.positions