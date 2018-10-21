import sys
import pygame

def check_events():
    """
    响应事件和鼠标事件
    """
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen , ship):
    # 每次循环都会重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # 让最近的绘制的屏幕可见
    pygame.display.flip()
