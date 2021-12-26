import pygame

from settings import Settings


def get_height_calculation_image(image, ship_width):
    ship_height = (image.get_height() * ship_width) / image.get_width()
    height_calculation_image = pygame.transform.scale(image, (ship_width, ship_height))
    return height_calculation_image


class Ship:
    def __init__(self, screen, ai_settings: Settings):
        """
        Инициализирует корабль и задает его начальную позицию.
        Получает объект screen, на котором должен выводится корабль
        """
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника
        image = pygame.image.load('images/spaceship.png')
        self.image = get_height_calculation_image(image, ai_settings.ship_width)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Сохранение вещественной координаты центра корабля
        self.horizontal = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # Обновляется атрибут center, не rect
        # Если координата правого края прямоугольника корабля меньше координаты правого края экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.horizontal += self.ai_settings.ship_speed_factor
        # Если координата левого края прямоугольника корабля больше нуля (то есть, координаты левого края экрана)
        if self.moving_left and self.rect.left > 0:
            self.horizontal -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.vertical -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.horizontal
        self.rect.centery = self.vertical

    def blitme(self):
        """Рисует корабль в теккущей позиции"""
        self.screen.blit(self.image, self.rect)
