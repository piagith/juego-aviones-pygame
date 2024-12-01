import pygame



def crear_proyectil_con_el_espaciador(proyectiles: list, jugador: pygame.Rect, sonido_disparo: pygame.mixer.Sound):
    """ 
    Crea un proyectil cuando se aprete la barra espaciadora, luego lo
    agrega a la lista de proyectiles
    
    Args:
        proyectiles(list): Lista de proyectiles a agregar proyectil, cada proyectil es .Rect
    """
    try: 
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            # jugador.centerx - 5: ajusta la posicion del proyectil/disparo para que este centrado, pero un poco a la izq
            # jugador.top: es la posición del borde superior del rectángulo que representa al jugador. Posiciona el proyectil justo encima del jugador
            # 5, 5: Estos son los ancho y alto del proyectil.
            proyectil = pygame.Rect(jugador.centerx - 5, jugador.top, 5, 5)  # Creación del proyectil
            proyectiles.append(proyectil)
            sonido_disparo.play()  # Reproduce el sonido de disparo
    except Exception as e:
        print(f"Error al crear proyectil: {e}")