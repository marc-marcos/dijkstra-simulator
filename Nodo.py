import pygame 

class Nodo_class:
    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.selected = False
            self.conexiones = []

            print(f"A node has been created at x:{x} y:{y}.")

    def draw_node(self, surface):
        if self.selected:
            pygame.draw.circle(surface, (0, 255, 0), (self.x, self.y), 20)

        else:
            pygame.draw.circle(surface, (255, 0, 0), (self.x, self.y), 20)

    def __str__(self):
        return f"The node at X:{self.x} Y:{self.y} is {self.selected}. Is connected with {len(self.conexiones)}."

    def conectar(self, otro_nodo, lista_nodos):
        # Añadir otro_nodo a la lista de conexiones
        self.conexiones.append(otro_nodo)

        # Añadir nodo a la lista de conexioens de otro_nodo
        for nodo in lista_nodos:
            if (nodo == otro_nodo):
                nodo.conexiones.append(self)

    def draw_connections(self, surface):
        for nodo_it in self.conexiones:
            pygame.draw.line(surface, (255, 255, 255), (self.x, self.y), (nodo_it.x, nodo_it.y), 2)

