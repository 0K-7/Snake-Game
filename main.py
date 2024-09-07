import sys
import pygame as pg
import snake as snake
import food as food
import time
Vec2 = pg.math.Vector2
running=1
pg.init()
pg.font.init()
pg.mixer.init() # add this line



class Game:
    def __init__(self):
        self._snake = snake.Snake(4, Vec2(10,10), Vec2(-1, 0))
        self._food = food.Food()
        self._grow = False
        self.sound = pg.mixer.Sound("dungeon2.wav")
        

        self.death=0

    def new_grid(self):
        pass

    def new_game(self):
        pass

    def update(self):
        surface.fill((0,0,25))             
        self._snake.constant_movement(self._grow)
        self._grow = False
        snake_positions = self._snake.get_snake_pos()
        i = 0
        while(i < len(snake_positions)):
            #print(snake_positions[i])
            x = snake_positions[i].x*30
            y = snake_positions[i].y*30

            pg.draw.rect(surface, snakecolor, pg.Rect(x, y, 30, 30))

            if(i==0):
            
             if self._snake.lastkey==(Vec2(0,-1)):
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+3, y+7, 8, 8))
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+19, y+7, 8, 8))
                pg.draw.rect(surface, (250,0,0), pg.Rect(x+5, y+9, 4, 4))
                pg.draw.rect(surface, (250,0,0), pg.Rect(x+21, y+9, 4, 4))
             elif (self._snake.lastkey==(Vec2(1,0))):
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+15, y+3, 8, 8))
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+15, y+19, 8, 8))
                pg.draw.rect(surface, (0,0,0), pg.Rect(x+15, y+3, 5, 5))
                pg.draw.rect(surface, (0,0,0), pg.Rect(x+15, y+19, 5, 5))
             elif (self._snake.lastkey==(Vec2(0,1))):
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+3, y+15, 8, 8))
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+19, y+15, 8, 8))
             elif (self._snake.lastkey==(Vec2(-1,0))):
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+7, y+3, 8, 8))
                pg.draw.rect(surface, (250,250,250), pg.Rect(x+7, y+19, 8, 8))   
              
                 
            i = i+1

            

        
        snake_positions = self._food.get_food_pos()
        i = 0
        while(i < len(snake_positions)):
            #print(snake_positions[i])
            x = snake_positions[i].x*30
            y = snake_positions[i].y*30

            # pg.draw.rect(surface,snakecolor,pg.Rect(x, y, 30, 30))
            # i = i+1
            pg.draw.circle(surface,foodcolor,[x+15,y+15],15)
            i=i+1
            
            

        font = pg.font.Font('freesansbold.ttf', 32)
        text = font.render(str(len(self._snake.segmentpositions)), True, (0,255,0),(0,0,25) )
        textRect = text.get_rect()
        textRect.center = (50, 50)
        surface.blit(text, textRect)

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self._snake.change_direction(pg.Vector2(0, -1))
                elif event.key == pg.K_DOWN:
                    self._snake.change_direction(pg.Vector2(0, 1))
                elif event.key == pg.K_LEFT:
                    self._snake.change_direction(pg.Vector2(-1, 0))
                elif event.key == pg.K_RIGHT:
                    self._snake.change_direction(pg.Vector2(1, 0))

        self._grow = self._food.is_food(self._snake.get_snake_pos()[0])
        
        if(self._grow):
            self._food.make_food()

        print(self._food.get_food_pos())
        print(self._snake.lastkey)
        
        if(self._snake.touching_snake()):
            self._snake.__init__(len(self._snake.segmentpositions), Vec2(10,10), Vec2(-1, 0))
            pg.mixer.music.load('bonk.mp3')
            pg.mixer.music.play(0)
            time.sleep (1)

            self.death+=1
            
            if(self.death==3):
                pg.mixer.music.load('end.mp3')
                pg.mixer.music.play(0)
                time.sleep(1.5)
                pg.quit()
                
                sys.exit()
        if(self._snake.touching_border()):
            self._snake.__init__(len(self._snake.segmentpositions), Vec2(10,10), Vec2(-1, 0))
            pg.mixer.music.load('bonk.mp3')
            pg.mixer.music.play(0)
            time.sleep (1)
            self.death+=1
            if(self.death==3):
                pg.mixer.music.load('end.mp3')
                pg.mixer.music.play(0)
                time.sleep(1.5)
                pg.quit()
                
                sys.exit()



# Initializing Pygame
pg.init()

# Initializing surface
surface = pg.display.set_mode((900,900))
 
# Initializing Color
snakecolor = (0,255,0)
foodcolor = (255,0,0)
#pg.mixer.music.load('Christmas synths.ogg')
#pg.mixer.music.play(-1)

game=Game()
game.new_grid()
game.new_game()

while(True):
    game.update()
    time.sleep(0.05)
    