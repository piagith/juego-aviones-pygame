import pygame
from variables.constantes import ANCHO, LARGO, ANCHO_JUGADOR, ALTO_JUGADOR

def inicializar_jugador():
    """Inicializa la posición del jugador"""
    jugador = pygame.Rect(
                        ANCHO // 2 - ANCHO_JUGADOR // 2, 
                        LARGO - ALTO_JUGADOR - 10, ANCHO_JUGADOR,
                        ALTO_JUGADOR
                        )
    return jugador
