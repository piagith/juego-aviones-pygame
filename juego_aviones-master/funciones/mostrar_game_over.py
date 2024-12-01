import pygame
from variables.constantes import ANCHO, LARGO, ROJO, BLANCO, NEGRO

def mostrar_game_over(puntos: int, screen: pygame.Surface) -> None:
    """ 
    Muestra por pantalla 'game over' y los puntos obtenidos del juego.
    Se llena la pantalla de color negro y se dibujan los textos centrados
    en la pantalla.
    """
    try:
        fuente_game_over = pygame.font.SysFont("Arial", 50)
        texto_game_over = fuente_game_over.render("GAME OVER", True, ROJO)
        texto_puntos = fuente_game_over.render(f"Ganaste puntos: {puntos}", True, BLANCO)
        # ANCHO // 2: da el centro horizontal de la pantalla.
        # texto_game_over.get_width() obtiene el ancho del texto "GAME OVER" una vez renderizado
        # texto_game_over.get_width() // 2 obtiene la mitad del ancho del texto.
        # al restarlo de ANCHO // 2, el texto quede centrado horizontalmente.

        # LARGO // 3: calcula un tercio de la altura
        # Esto coloca el texto "GAME OVER" a un tercio de la altura de la pantalla.
        coordenada_rect_game_over = (ANCHO // 2 - texto_game_over.get_width() // 2, LARGO // 3)


        # La misma logica para posicionarlo horizontalmente en el medio (eje x)
        # LARGO // 2: calcula la mitad de altura
        # Esto coloca a "Ganaste puntos: " en el medio
        coordenada_rect_puntos = (ANCHO // 2 - texto_puntos.get_width() // 2, LARGO // 2)
        
        
        # Mostrar el texto
        screen.fill(NEGRO)
        screen.blit(texto_game_over, coordenada_rect_game_over)
        screen.blit(texto_puntos, coordenada_rect_puntos)
        
        pygame.display.flip()
    except Exception as e:
        print(f"Error al mostrar la pantalla de Game Over: {e}")