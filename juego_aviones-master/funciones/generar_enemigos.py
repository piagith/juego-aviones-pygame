import pygame
import random
from variables.constantes import ANCHO, ANCHO_ENEMIGOS, ALTO_ENEMIGOS

def generar_enemigos(cantidad_enemigos: list) -> None:
    """ 
    Genera un enemigo de clase Rect, y lo agrega a la lista cantidad_enemigos, solo si
    la lista cantidad_enemigos tiene menos de 10 enemigos.
    Es decir, en el juego puede haber hasta 10 enemigos a la vez

    Args:
        cantidad_enemigos(list): Lista con todos los enemigos (max. 10), cada enemigo es .Rect
    """
    if len(cantidad_enemigos) < 10:
        enemigo = pygame.Rect(random.randint(0, ANCHO - ANCHO_ENEMIGOS), 
                            0, ANCHO_ENEMIGOS, ALTO_ENEMIGOS)
        cantidad_enemigos.append(enemigo)