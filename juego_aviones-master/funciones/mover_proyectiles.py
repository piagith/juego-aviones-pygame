import pygame

def mover_proyectiles(proyectiles: list):
    """  
    Mueve a los proyectiles hacia arriba (10 pixeles) y elimina
    aquellos que hayan salido de la pantalla
    
    Args:
        proyectiles(list): Lista de proyectiles a eliminar proyectil, cada proyectil es .Rect
    """
    try:
        for proyectil in proyectiles[:]:
            """
            El bucle recorre todos los proyectiles actuales en la lista proyectiles. 
            El uso de [:] hace que estemos iterando sobre una copia de la lista, 
            lo que permite modificar la lista (eliminando elementos) sin causar problemas durante la iteración.
            """
            # proyectil.y: es un atributo del proyectl(que es de calse rect), indica la coordenada eje Y
            proyectil.y -= 10
            # proyectil.button: es la coordenada Y de la parte inferior del rectángulo
            # Verifica si la parte inferior del proyectil ha salido de la pantalla
            if proyectil.bottom < 0: # la pantalla tiene un límite superior (Y = 0)
                proyectiles.remove(proyectil)
    except Exception as e:
        print(f"Error al mover proyectiles: {e}")