import pygame
from variables.constantes import ANCHO, LARGO

def configurar_pantalla():
    """Configura la pantalla del juego"""
    screen = pygame.display.set_mode((ANCHO, LARGO))
    pygame.display.set_caption("Juego aviones")
    return screen