import pygame

pygame.init()
pygame.mixer.init()


from configuraciones.configurar_pantalla import *
from configuraciones.cargar_imagenes import *
from configuraciones.redimensionar_imagenes import *
from configuraciones.reproducir_sonidos import *


from variables.constantes import *
from funciones.mostrar_game_over import *
from funciones.mover_jugador import *
from funciones.crear_proyectil import *
from funciones.mover_proyectiles import *
from funciones.generar_enemigos import *
from funciones.mover_enemigos import *
from funciones.detectar_colisiones import *
from funciones.actualizar_fondo import *
from funciones.inicializar_jugador import *
from funciones. mostrar_reglas import *



def main():
    # Configuración inicial
    screen = configurar_pantalla()
    jugador_imagen, enemigo_imagen, fondo_imagen, fondo_largo = cargar_imagenes()
    jugador_redimension, enemigo_redimension = redimensionar_imagenes(jugador_imagen, enemigo_imagen)
    
    
    # Cargar reglas del juego
    reglas = cargar_reglas()
    if reglas is not None:
        mostrar_reglas(screen, reglas)  # Mostrar las reglas antes de comenzar el juego
    
    # Configuracion sonido
    reproducir_musica_fondo()
    sonido_disparo, sonido_game_over = cargar_sonidos()
    
    
    # Variables del juego
    jugador = inicializar_jugador()
    fondo1 = 0  # Posición vertical del primer fondo
    fondo2 = fondo_largo  # Posición vertical del segundo fondo
    velocidad_fondo = 2  # El fondo se mueve a 2 píxeles hacia abajo
    puntos = 0  # Contador de puntos
    cantidad_enemigos = []  # Almacena los enemigos
    proyectiles = []  # Almacena los proyectiles
    
    # Fuente para mostrar los puntos
    fuente = pygame.font.SysFont(FUENTE, TAM_FUENTE)
    
    # Control de fps
    reloj = pygame.time.Clock()
    
    corriendo = True
    
    while corriendo:
        
        # Llena la pantalla de negro para asegurarse de que no queden imágenes anteriores
        screen.fill(NEGRO)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
        mover_jugador(jugador)
        crear_proyectil_con_el_espaciador(proyectiles, jugador, sonido_disparo)
        mover_proyectiles(proyectiles)
        generar_enemigos(cantidad_enemigos)
        mover_enemigos(cantidad_enemigos)
        puntos = detectar_colisiones_entre_proyectiles_y_enemigos(puntos, proyectiles, cantidad_enemigos)
        
        # Terminar el juego si el jugador colisiona con un enemigo
        for enemigo in cantidad_enemigos:
            if jugador.colliderect(enemigo):
                corriendo = False
                sonido_game_over.play()  # Reproducir el sonido de Game Over al terminar el juego
        
        
        # Actualiza el movimiento de la imagen de fondo 
        fondo1, fondo2 = actualizar_fondo(fondo1, fondo2, fondo_largo, fondo_imagen, velocidad_fondo, screen)
        
        # Dibujo de los personajes
        screen.blit(jugador_redimension, jugador)
        
        for enemigo in cantidad_enemigos:
            screen.blit(enemigo_redimension, enemigo)
        
        for proyectil in proyectiles:
            pygame.draw.rect(screen, AZUL, proyectil)
        
        # Mostrar puntos en la esquina superior izquierda
        mostrar_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)
        screen.blit(mostrar_puntos, (10, 10))
        
        pygame.display.flip()
        
        # Mostrar game over si el juego ha terminado
        if not corriendo:
            pygame.mixer.music.stop()  # Detener la música de fondo al finalizar el juego
            mostrar_game_over(puntos, screen)
            pygame.time.wait(2000)
            corriendo = False
        
        # Control de FPS
        reloj.tick(30)
    
    pygame.quit()

main()