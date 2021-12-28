import sys
import pygame
from alien import Alien
from bullet import Bullet
from settings import Settings
from pygame.sprite import Group
from ship import Ship


def create_fleet(ai_settings: Settings, screen, aliens):
    """Создает флот пришельцев"""
    # Вычисление количества пришельцев в ряду
    # Интервал между соседними пришельцами равен одной ширине пришельца
    available_space_x = ai_settings.screen_width - (2 * ai_settings.alien_width)
    number_aliens_x = int(available_space_x / (2 * ai_settings.alien_width))

    # Создание первого ряда пришельцев
    for alien_number in range(number_aliens_x):
        # Создание пришельца и размещение его в ряду
        alien = Alien(screen, ai_settings)
        alien.x = ai_settings.alien_width + 2 * ai_settings.alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Выпускает пулю, если лимит еще не достигнут"""
    # Создание новой пули и включение ее в группу bullets
    if len(bullets) < ai_settings.bullets_limit:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets(bullets: Group):
    """Обновляет позиции пуль и уничтожает старые пули"""
    # Обновление позиции пули
    bullets.update()

    # Уничтожение пуль, вышедших за экран
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def check_keydown_events(event, ai_settings: Settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Обрабатывает отпускание клавиш"""
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship: Ship, aliens, bullets):
    """Обновляет изображения на экране и отображает новый экран"""
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # Отображение последнего прорисованного экрана
    pygame.display.flip()
