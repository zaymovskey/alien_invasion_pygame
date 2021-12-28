import pygame
from pygame.sprite import Sprite
from help_functions import get_height_calculation_image
from settings import Settings


class Alien(Sprite):
    def __init__(self, screen, ai_settings: Settings):
        """
            Инициализирует пришельца и задает его начальную позицию.
            Получает объект screen, на котором должен выводится пришелец
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения пришельца и получение прямоугольника
        self.image = get_height_calculation_image(pygame.image.load('images/alien.png'), ai_settings.alien_width)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый пришелец появляется у левого верхнего края экрана
        self.rect.left = self.screen_rect.left
        self.rect.top = self.screen_rect.top

        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        """Рисует пришельца в теккущей позиции"""
        self.screen.blit(self.image, self.rect)
