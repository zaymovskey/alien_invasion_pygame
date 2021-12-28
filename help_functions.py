import pygame


def get_height_calculation_image(image, ship_width):
    ship_height = (image.get_height() * ship_width) / image.get_width()
    height_calculation_image = pygame.transform.scale(image, (ship_width, ship_height))
    return height_calculation_image
