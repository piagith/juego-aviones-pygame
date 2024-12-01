
def detectar_colisiones_entre_proyectiles_y_enemigos(puntos: int, proyectiles: list, cantidad_enemigos: list) -> int:
    """  
    Detecta colisiones entre proyectiles y enemigos, y si es asi:
    -> Se le suman 5 puntos al jugador
    -> El enemigo de elimina
    """
    try:
        for proyectil in proyectiles[:]:
            # Recorre 1 indice de proyectiles, recorre todos los objetos de la lista enemigos
            for enemigo in cantidad_enemigos[:]:
                # Verifica si el proyectil choco con algún enemigo de la lista cantidad_enemigos
                if proyectil.colliderect(enemigo):
                    proyectiles.remove(proyectil)
                    cantidad_enemigos.remove(enemigo)
                    puntos += 5
                    # Luego de encontrar la colision, sale del bucle
                    break
    except Exception as e:
        print(f"Error al detectar colisiones entre proyectiles y enemigos: {e}")
    return puntos
