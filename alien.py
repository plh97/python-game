import sys
import pygame

from settings import Settings

a = 123
a = 'wer'
print(a)

def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    bg_color = (143,195,132)

    # 开始游戏主循环
    while True:
        screen.fill(ai_settings.bg_color)

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.event.get():
                sys.exit()
            
        # 让最近的绘制的屏幕可见
        pygame.display.flip()

run_game()            