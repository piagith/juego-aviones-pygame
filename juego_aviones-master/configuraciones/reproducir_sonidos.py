import pygame
import sys


def reproducir_musica_fondo():
    try:
        pygame.mixer.music.load("audio/fondo.mp3")  # Cargar música de fondo
        pygame.mixer.music.play(loops=-1, start=0.0)  # Reproducir la música de fondo indefinidamente
    except pygame.error as e:
        print(f"Error al cargar la música: {e}")
    
    # Ajusta el volumen de la música (valor entre 0.0 y 1.0)
    pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen al 50%

def cargar_sonidos():
    """Carga los sonidos del juego"""
    try:
        sonido_disparo = pygame.mixer.Sound("audio/disparo.mp3")  # Cargar el sonido de disparo
        sonido_game_over = pygame.mixer.Sound("audio/game_over.mp3")  # Cargar el sonido de Game Over
    except pygame.error as e:
        print(f"Error al cargar los sonidos: {e}")
        sys.exit(1)
    
    return sonido_disparo, sonido_game_over