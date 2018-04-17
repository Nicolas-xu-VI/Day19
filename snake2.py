from enum import Enum,uique
import pygame
#枚举设置颜色
@unique
class Color(Enum):
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    WHITE = (255,255,255)
    BLACK = (0,0,0)

#设置方向
@unique
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

#墙
class Wall():
    def __init__(self,x,y,width,height,color = color.BLACK.value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    #画墙
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),5)

#食物
class Food():
    def __init__(self,x,y,size,color = Color.RED.value):
        # x,y 起始位置  size 是直径
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        #隐藏状态
        self.hidden = False

    #没处于隐藏状态 则画出来
    def draw(self,screen):
        if not self.hidden:
            pygame.draw.circle(screen,self.color,(self.x +self.size // 2,self.y+self.size // 2),self.size,0)

