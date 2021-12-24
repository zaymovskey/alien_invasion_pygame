import pygame


class Ship:
    def __init__(self, screen):
        """
        Инициализирует корабль и задает его начальную позицию.
        Получает объект screen, на котором должен выводится корабль
        """
        self.screen = screen

        # Загрузка изображения корабля и получение прямоугольника
        image = pygame.image.load('images/spaceship.png')
        self.image = pygame.transform.scale(image, (150, 150))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в теккущей позиции"""
        self.screen.blit(self.image, self.rect)
