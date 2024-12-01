from variables.constantes import LARGO

def mover_enemigos(cantidad_enemigos: list) -> None:
    """  
    Mueve al enemigo 5 pixeles hacia abajo verticalmente (eje y) y
    cuando salen de pantalla, los elimina de la lista cantidad_enemigos
    
    Args:
        cantidad_enemigos(list): Lista con todos los enemigos (max. 10), cada enemigo es .Rect
    """
    try:
        for enemigo in cantidad_enemigos:
            # enemigo.y: atributo de la clase Rect, que indica la coordenada del eje y del objeto
            enemigo.y += 5 
            # enemigo.top: indica la coordenada Y de la parte superior de la imagen/rectangulo enemigo
            # LARGO: altura de la pantalla
            if enemigo.top > LARGO:  # Si la parte superior del enemigo ha cruzado la parte inferior de la pantalla
                cantidad_enemigos.remove(enemigo)  # Elimina al enemigo de la lista
    except Exception as e:
        print(F"Error al mover enemigos: {e}")