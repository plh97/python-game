class Settings():
    """
    存储<外星人入侵>的所有设置的类
    """

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0,0,220)

        # 飞船的设置
        self.ship_speed_factor = 50

        # 子弹设置
        self.bullet_speed_factor = 50
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (111,111,110)
        self.bullet_allowed = 3