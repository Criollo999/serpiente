# Juego de la Serpiente 🐍

Un clásico juego de la serpiente implementado en Python usando pygame.

## Descripción

Este es un juego simple pero entretenido donde controlas una serpiente que debe comer comida para crecer. El objetivo es conseguir la mayor puntuación posible sin chocar con las paredes o con el propio cuerpo de la serpiente.

## Características

- Serpiente que se mueve suavemente por la pantalla
- Comida que aparece aleatoriamente
- Sistema de puntuación
- Detección de colisiones con paredes y cuerpo
- Posibilidad de reiniciar el juego
- Interfaz gráfica simple y limpia

## Instalación

1. Asegúrate de tener Python instalado en tu sistema
2. Instala pygame:
   ```bash
   pip install pygame
   ```

## Cómo jugar

1. Ejecuta el archivo `serpiente.py`:
   ```bash
   python serpiente.py
   ```

2. Controla la serpiente con las teclas de flecha:
   - ↑ Flecha arriba: mover hacia arriba
   - ↓ Flecha abajo: mover hacia abajo
   - ← Flecha izquierda: mover hacia la izquierda
   - → Flecha derecha: mover hacia la derecha

3. Come la comida roja para hacer crecer la serpiente y ganar puntos

4. Evita chocar con las paredes o con el cuerpo de la serpiente

5. Si pierdes, presiona ESPACIO para reiniciar el juego

## Puntuación

- Cada comida consumida otorga 10 puntos
- La serpiente crece un segmento por cada comida consumida
- No hay límite de puntuación máxima

## Requisitos

- Python 3.6 o superior
- pygame

## Estructura del código

- `Serpiente`: Clase que maneja la lógica de la serpiente
- `Comida`: Clase que maneja la aparición de comida
- `main()`: Función principal que controla el bucle del juego

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el juego, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes usar, modificar y distribuir el código libremente.
