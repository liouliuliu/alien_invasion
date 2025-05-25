from symtable import Class

class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # ⼦弹设置
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # 飞船移动速度设置
        self.ship_speed = 2.5
        # 外星⼈设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为 1 表示向右移，为 -1 表示向左移
        self.fleet_direction = 1