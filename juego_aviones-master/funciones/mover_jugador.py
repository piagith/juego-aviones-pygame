import pygame
from variables.constantes import ANCHO, LARGO, JUGADOR_REDIMENSION

def mover_jugador(jugador) -> None:
    """ 
    Mueve al jugador dependiendo de que tecla seleccione.
    
    """
    try: 
        teclas = pygame.key.get_pressed()
        # Movimiento del jugador
        if teclas[pygame.K_LEFT] and jugador.left > 0:
            # Si se presiona la tecla de izquierda, el jugador se mueve 10 píxeles hacia la izquierda
            jugador.x -= 10

        if teclas[pygame.K_RIGHT] and jugador.right < ANCHO:
            # Si se presiona la tecla de derecha, el jugador se mueve 10 píxeles hacia la derecha
            jugador.x += 10

        if teclas[pygame.K_UP] and jugador.top > 0:
            # Si se presiona la tecla hacia arriba, el jugador se mueve 10 píxeles hacia arriba.
            jugador.y -= 10

        if teclas[pygame.K_DOWN] and jugador.bottom < LARGO:
            #Si se presiona la tecla hacia abajo, el jugador se mueve 10 píxeles hacia abajo.
            jugador.y += 10
    except Exception as e:
        print(f"Error al mover al jugador: {e}")