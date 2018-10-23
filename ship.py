
import pygame,os


current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, '') # The resource folder path
image_path = os.path.join(resource_path, 'images') # The image folder path


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并且设置其初始化设置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(os.path.join(image_path, 'ship.png'))
        self.image = pygame.transform.scale(self.image, (20, 40))
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央
        # self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.centery)

        # 移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        self.rect.top = self.bottom



    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)