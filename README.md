# JUEGO_TRIQUI

Juego de Triqui (Tres en línea) desarrollado en Python con interfaz de consola. Permite jugar partidas entre dos personas, registra los nombres de los jugadores, almacena el historial de resultados y ofrece una experiencia clara y sencilla.

# Equipo de trabajo
- LIZETH KATHERINE TROCHEZ PAEZ
- FLOR ALBA TOVAR PEREA
- JOHAN SEBASTIAN ALONSO GUTIERREZ

## Características

- Tablero clásico de 3x3 para dos jugadores.
- Ingreso y validación de nombres únicos para los jugadores.
- Turnos alternos entre los jugadores (X y O).
- Detección automática de ganador o empate.
- Registro de historial de partidas con fecha, nombres y resultado.
- Menú principal intuitivo:
  - Jugar una partida.
  - Ver historial de partidas jugadas.
  - Salir del juego.
- Código modular y fácil de mantener

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- `main.py`: Archivo principal, muestra el menú y orquesta el flujo del juego.
- `triqui_game.py`: Lógica principal del juego y control del tablero.
- `triqui_display.py`: Maneja la visualización y limpieza de pantalla.
- `triqui_score.py`: Gestiona el registro y consulta del historial de partidas.
- `triqui_players.py`: Controla el ingreso y validación de los nombres de jugadores.

## Requisitos

- Python 3.x

## Cómo Jugar

1. Ejecuta el juego:
   ```bash
   python main.py
   ```

2. Ingresa el nombre de ambos jugadores (no pueden ser iguales ni estar vacíos).

3. En el menú principal, selecciona:
   - 1: Jugar una partida
   - 2: Ver historial de partida
   - 3: Salir

4. Para Jugar:
   - Se alternarán los turnos entre los jugadores.
   - Ingresa tu jugada en formato: fila,columna (ejemplo: 2,3).
     - Los números van del 1 al 3.
   - El tablero se actualizará tras cada movimiento.
   - El juego detecta automáticamente si hay un ganador o empate.

5. El historial de partidas jugadas se guarda en el archivo historial_triqui.csv.

## Ejemplo de visualización

   ```bash
      1   2   3
 +----+---+---+
1| X |   | O |
 +----+---+---+
2|   | X |   |
 +----+---+---+
3| O |   | X |
 +----+---+---+
   ```

## Historial de partidas

El historial se almacena en historial_triqui.csv con las siguientes columnas:
- Fecha y hora
- Jugador 1
- Jugador 2
- Resultado (Ganador o Empate)
