from symtable import Class

class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船移动速度设置
        self.ship_speed = 2.5