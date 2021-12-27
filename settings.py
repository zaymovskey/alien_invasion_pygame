class Settings:
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Настройки корабля
        self.ship_speed_factor = 1.5
        self.ship_width = 150

        # Параметры пули
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = (255, 255, 255)
        self.bullets_limit = 3
