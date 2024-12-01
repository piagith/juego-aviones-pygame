import pygame

def actualizar_fondo(fondo1: float, fondo2: float, fondo_largo: int, fondo_imagen, velocidad_fondo: float, screen:pygame.Surface) -> tuple[int,int]:
    """ 
    Actualiza el fondo desplazando las imágenes hacia abajo y repitiéndolas cuando salen de la pantalla.

    Argumentos:
        fondo1 (float): Posición Y del primer fondo.
        fondo2 (float): Posición Y del segundo fondo.
        fondo_largo (int): Altura de la imagen del fondo.
        fondo_imagen: Imagen del fondo a ser desplazada.
        velocidad_fondo (float): Velocidad de desplazamiento del fondo.
        screen: Superficie de la pantalla de Pygame donde se dibuja el fondo.

    Return:
        tuple: Nuevas posiciones Y de fondo1 y fondo2.
    """
    try:    
        # A las pociones verticales(fondo1, fondo2), se le suman 2 pixeles
        # Con la suma hara que se dezplacen hacia abajo
        fondo1 += velocidad_fondo
        fondo2 += velocidad_fondo
        
        # Pega en la pantalla los fondos y genera el movimiento
        # Dibuja fondo_imagen en la posicion (x = 0, y=fondo1)
        # A medida que fondo1 aumenta, la imagen de fondo se mueve hacia abajo en la pantalla.
        screen.blit(fondo_imagen, (0, fondo1))
        screen.blit(fondo_imagen, (0, fondo2))
        
        # Verifica si la posicion en la que este fondo 1 ha llegado o ha pasado la altura de la imagen de fondo(fondo_largo)
        # Es decir, si el fondo ya paso hacia abajo, salio completamente de la pantalla por la parte inferior, y ya no es visible
        if fondo1 >= fondo_largo:
            # Entonces si se ha movido completamente fuera de la pantalla
            # Actualiza su posición a una negativa en el eje Y
            # Es decir, actualiza su eje Y justo por encima de la pantalla
            fondo1 = -fondo_largo
        if fondo2 >= fondo_largo:
            fondo2 = -fondo_largo
        return fondo1, fondo2
    
    except Exception as e:
        print(f"Error al actualizar el fondo: {e}")
        return fondo1, fondo2  # Si ocurre un error, devuelve los valores originales