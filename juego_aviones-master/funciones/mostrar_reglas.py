import pygame
import json
import sys
from variables.constantes import ANCHO,BLANCO,AZUL


def cargar_reglas():
    """Cargar las reglas del juego desde un archivo JSON"""
    try:
        with open('reglas.json', 'r', encoding="utf-8") as archivo:
            reglas = json.load(archivo)
        return reglas
    except FileNotFoundError:
        print("Error: El archivo reglas.json no fue encontrado.")
        return None



def mostrar_reglas(screen: pygame.Surface, reglas: dict):
    """
    Muestra las reglas del juego en la pantalla hasta que se presione click izquierdo
    en el mousse
    
    Args:
        screen(pygame.Surface): pantalla del juego
        reglas(dict): diccionario con el titulo y el contenido de las reglas
    """
    fuente_titulo= pygame.font.SysFont("Arial", 35)
    fuente_reglas = pygame.font.SysFont("Arial", 25)
    
    # Mostrar el título de las reglas
    titulo = fuente_titulo.render(reglas["titulo"], True, AZUL)
    # ANCHO // 2 nos da la posición central de la pantalla.
    # titulo.get_width() // 2 nos da la mitad del ancho del texto.
    # Este calculo centra el texto en el medio del eje x
    screen.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))
    
    # Mostrar las reglas
    desplazamiento_y_de_reglas =  100 # Esta es la posición y para el primer texto
    for linea in reglas["contenido"]:
        texto = fuente_reglas.render(linea, True, BLANCO)
        screen.blit(texto, (ANCHO // 2 - texto.get_width() // 2, desplazamiento_y_de_reglas))
        desplazamiento_y_de_reglas += 40
    
    pygame.display.flip()
    
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit() # garantiza que Pygame se cierre correctamente y que el programa termine sin errores.

            # Verificar si el evento es un clic del mouuse y si es el izquierdo
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                esperando = False  # Salir del bucle y empezar el juego