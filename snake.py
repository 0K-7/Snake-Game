import pygame as pg
vec2 = pg.math.Vector2
class Snake:
    def __init__(self, _len, start, dir):

        self.lastkey = vec2(0,1)
        self.length = 4
        #self.segmentpositions = [vec2(10,0),vec2(9,0),vec2(8,0),vec2(7,0)]
        self.segmentpositions = [start]
        while(len(self.segmentpositions) < _len):
            self.segmentpositions.append(self.segmentpositions[-1]+dir)


    def touching_border(self):  #tell is if snake is touching border
        if self.segmentpositions[0].x < 0 or self.segmentpositions[0].y < 0 or self.segmentpositions[0].x > 29 or self.segmentpositions[0].y > 29:
            return True

    def touching_snake(self):   #tells if the snake is touching itselfs
        for s in self.segmentpositions[1:]:
            if(s==self.segmentpositions[0]):
                return True

    def constant_movement(self, grow):    #makes snake constantly move forward
        self.segmentpositions.insert(0,self.segmentpositions[0]+self.lastkey)
        if grow == False:
            del self.segmentpositions[-1]
       # print("Growing? ", grow)

    def change_direction(self, dir):
        if dir.rotate(180) != self.lastkey:
            self.lastkey=dir

        
    def get_snake_pos(self):
        return self.segmentpositions
    
    

