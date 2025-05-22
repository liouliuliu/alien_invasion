import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #  加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        print(self.rect)
        #  每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # print(self.rect.x)
        # # 存储外星人的准确位置
        self.x = float(self.rect.x)