import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
TAMANO_CELDA = 20

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Configurar la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")
reloj = pygame.time.Clock()

class Serpiente:
    def __init__(self):
        self.cuerpo = [(ANCHO // 2, ALTO // 2)]
        self.direccion = (TAMANO_CELDA, 0)
        self.crecimiento = False
    
    def mover(self):
        cabeza = self.cuerpo[0]
        nueva_cabeza = (cabeza[0] + self.direccion[0], cabeza[1] + self.direccion[1])
        self.cuerpo.insert(0, nueva_cabeza)
        
        if not self.crecimiento:
            self.cuerpo.pop()
        else:
            self.crecimiento = False
    
    def cambiar_direccion(self, nueva_direccion):
        # Evitar que la serpiente se mueva en dirección opuesta
        if (nueva_direccion[0] * -1, nueva_direccion[1] * -1) != self.direccion:
            self.direccion = nueva_direccion
    
    def crecer(self):
        self.crecimiento = True
    
    def colision_pared(self):
        cabeza = self.cuerpo[0]
        return (cabeza[0] < 0 or cabeza[0] >= ANCHO or 
                cabeza[1] < 0 or cabeza[1] >= ALTO)
    
    def colision_cuerpo(self):
        cabeza = self.cuerpo[0]
        return cabeza in self.cuerpo[1:]
    
    def dibujar(self):
        for segmento in self.cuerpo:
            rect = pygame.Rect(segmento[0], segmento[1], TAMANO_CELDA, TAMANO_CELDA)
            pygame.draw.rect(pantalla, VERDE, rect)

class Comida:
    def __init__(self):
        self.posicion = self.generar_posicion()
    
    def generar_posicion(self):
        x = random.randint(0, (ANCHO - TAMANO_CELDA) // TAMANO_CELDA) * TAMANO_CELDA
        y = random.randint(0, (ALTO - TAMANO_CELDA) // TAMANO_CELDA) * TAMANO_CELDA
        return (x, y)
    
    def dibujar(self):
        rect = pygame.Rect(self.posicion[0], self.posicion[1], TAMANO_CELDA, TAMANO_CELDA)
        pygame.draw.rect(pantalla, ROJO, rect)

def mostrar_puntuacion(puntuacion):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    pantalla.blit(texto, (10, 10))

def mostrar_game_over(puntuacion):
    fuente = pygame.font.Font(None, 72)
    texto1 = fuente.render("GAME OVER", True, BLANCO)
    texto2 = fuente.render(f"Puntuación final: {puntuacion}", True, BLANCO)
    texto3 = fuente.render("Presiona ESPACIO para reiniciar", True, BLANCO)
    
    pantalla.blit(texto1, (ANCHO // 2 - texto1.get_width() // 2, ALTO // 2 - 100))
    pantalla.blit(texto2, (ANCHO // 2 - texto2.get_width() // 2, ALTO // 2 - 50))
    pantalla.blit(texto3, (ANCHO // 2 - texto3.get_width() // 2, ALTO // 2 + 50))

def main():
    serpiente = Serpiente()
    comida = Comida()
    puntuacion = 0
    game_over = False
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == pygame.KEYDOWN:
                if not game_over:
                    if evento.key == pygame.K_UP:
                        serpiente.cambiar_direccion((0, -TAMANO_CELDA))
                    elif evento.key == pygame.K_DOWN:
                        serpiente.cambiar_direccion((0, TAMANO_CELDA))
                    elif evento.key == pygame.K_LEFT:
                        serpiente.cambiar_direccion((-TAMANO_CELDA, 0))
                    elif evento.key == pygame.K_RIGHT:
                        serpiente.cambiar_direccion((TAMANO_CELDA, 0))
                else:
                    if evento.key == pygame.K_SPACE:
                        # Reiniciar el juego
                        serpiente = Serpiente()
                        comida = Comida()
                        puntuacion = 0
                        game_over = False
        
        if not game_over:
            serpiente.mover()
            
            # Verificar colisiones
            if serpiente.colision_pared() or serpiente.colision_cuerpo():
                game_over = True
            
            # Verificar si la serpiente come la comida
            if serpiente.cuerpo[0] == comida.posicion:
                serpiente.crecer()
                puntuacion += 10
                comida.posicion = comida.generar_posicion()
                
                # Asegurar que la comida no aparezca sobre la serpiente
                while comida.posicion in serpiente.cuerpo:
                    comida.posicion = comida.generar_posicion()
        
        # Dibujar todo
        pantalla.fill(NEGRO)
        
        if not game_over:
            serpiente.dibujar()
            comida.dibujar()
            mostrar_puntuacion(puntuacion)
        else:
            mostrar_game_over(puntuacion)
        
        pygame.display.flip()
        reloj.tick(5)  # Controlar la velocidad del juego (más lento)

if __name__ == "__main__":
    main()
# hola mundo