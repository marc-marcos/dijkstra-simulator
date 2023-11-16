import pygame
import time
import sys
import math
from Nodo import Nodo_class

# Funciones para que todo funcione

def get_distance(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    return distancia

def detect_which_node(x, y, lista_nodos):
    min_distance = sys.maxsize
    nodo_minimo = None

    for nodo in lista_nodos:
        if (nodo_minimo is None or get_distance(x, y, nodo.x, nodo.y) <= min_distance):
            min_distance = get_distance(x, y, nodo.x, nodo.y)
            nodo_minimo = nodo

    return nodo_minimo 


pygame.init()

WIDTH = HEIGHT = 800

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

is_running = True

lista_nodos = []

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            lista_nodos.append(Nodo_class(mouse_x, mouse_y))

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            nodo_a_cambiar = detect_which_node(mouse_x, mouse_y, lista_nodos)
            nodo_a_cambiar.selected = not nodo_a_cambiar.selected

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            # Conectar los nodos
            nodo_1 = nodo_2 = None

            for nodo in lista_nodos:
                if (nodo.selected):
                    nodo_1 = nodo

            for nodo in lista_nodos:
                if (nodo.selected and nodo != nodo_1):
                    nodo_2 = nodo

            if (nodo_1 is not None and nodo_2 is not None):
                nodo_1.conectar(nodo_2, lista_nodos)


    window_surface.blit(background, (0, 0))

    for i in lista_nodos:
        i.draw_connections(window_surface)
        i.draw_node(window_surface)

    pygame.display.update()
    time.sleep(0.1)
