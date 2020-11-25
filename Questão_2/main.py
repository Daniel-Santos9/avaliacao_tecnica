class Fila:
    def __init__(self):
        self.fila = []
        self.tamanho_fila = 0

    def push(self, c):
        self.fila.append(c)
        self.tamanho_fila +=1

    def pop(self):
        if not self.empty():
            self.fila.pop(0)
            self.tamanho_fila -= 1

    def length(self):
        return self.tamanho_fila

    def empty(self):
        if self.length() == 0:
            return True
        return False

    def show(self):
        return print(self.fila)

    def cache_query(self, consulta):
        if self.length() < 10:
            self.push(consulta)
        else:
            self.pop()
            self.push(consulta)       

query = Fila()

for i in range(13):
    query.cache_query(i)

query.show()