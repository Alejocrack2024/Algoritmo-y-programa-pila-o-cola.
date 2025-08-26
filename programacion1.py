class Pila:

    def __init__(self, *args, **kwargs):
        self.contenido = []

    def insertar(self, elemento):
        self.contenido.append(elemento)

    def size(self):
        return len(self.contenido)

    def esta_vacia(self):
        if len(self.contenido)!= 0:
            return False
        else:
            return True

    def quitar(self):
        if not (self.esta_vacia()):
            self.contenido.pop()
        else:
            print("No se puede quitar elementos de una pila vacia")

    def __str__(self):
        return f"Pila con {self.size()} elementos. Contenido: {self.contenido}"

class Cola:

    def __init__(self, *args, **kwargs):
        self.contenido = []

    def encolar(self, elemento):
        self.contenido.append(elemento)
    
    def size(self):
        return len(self.contenido)
    
    def esta_vacia(self):
        if len(self.contenido)!= 0:
            return False
        else:
            return True

    def desencolar(self):
        if not (self.esta_vacia()):
            self.contenido.pop(0)
        else:
            print("No se puede quitar elementos de una cola vacia")

    def __str__(self):
        return f"Cola con {self.size()} elementos. Contenido: {self.contenido}"
    
pila = Pila()
pila.insertar(3)
pila.insertar(3)
pila.insertar(90)
pila.insertar("Hola mundo")

print(pila)

pila.quitar()
print(pila)

cola = Cola()
cola.encolar(3)
cola.encolar(32)
cola.encolar(38)
cola.encolar("Soy el ultimo de la fila")

print(cola)

cola.desencolar()
print(cola)
