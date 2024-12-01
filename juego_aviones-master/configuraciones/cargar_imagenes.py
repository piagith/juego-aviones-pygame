import pygame
import sys

def cargar_imagenes():
    """Carga las imágenes necesarias para el juego"""
    try:
        # convert_alpha(): hace que las imagenes png no aparezcan en blanco
        jugador_imagen = pygame.image.load("image/avion1.png").convert_alpha()
        enemigo_imagen = pygame.image.load("image/enemigo1.png").convert_alpha()
        fondo_imagen = pygame.image.load("image/fondo2.png")
        fondo_largo = fondo_imagen.get_height()  # Obtiene la altura
    except FileNotFoundError as e:
        print(f"Error: No se pudo encontrar el archivo de imagen. {e}")
        sys.exit(1)
    
    return jugador_imagen, enemigo_imagen, fondo_imagen, fondo_largo