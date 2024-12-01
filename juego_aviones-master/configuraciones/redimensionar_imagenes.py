import pygame
from variables.constantes import JUGADOR_REDIMENSION, ENEMIGO_REDIMENSION

def redimensionar_imagenes(jugador_imagen, enemigo_imagen):
    """Redimensiona las imágenes del jugador y enemigo"""
    jugador_redimension = pygame.transform.scale(jugador_imagen, JUGADOR_REDIMENSION)
    enemigo_redimension = pygame.transform.scale(enemigo_imagen, ENEMIGO_REDIMENSION)
    return jugador_redimension, enemigo_redimension