class Forma:
    def __init__(self):
        self.area = None
        self.perimetro = None
        self.lados = list()
    
    def calcula_area():
        pass

    def calcula_perimetro():
        pass

class Retangulo(Forma):

    def __init__(self, lado1, lado2, lado3 ,lado4):
        self.lados = [lado1, lado2, lado3, lado4]

    def calcula_area(self):

        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3 and self.lado1 >= self.lado4:
            base = self.lado1
            if self.lado2 == self.lado1:
                altura = self.lado3
            elif self.lado3 == self.lado1:
                altura = self.lado2
            else:
                altura = self.lado2
        elif self.lado2 >= self.lado1 and self.lado2 >= self.lado3 and self.lado2 >= self.lado4:
            base = self.lado2
            if self.lado1 == self.lado2:
                altura = self.lado3
            elif self.lado3 == self.lado2:
                altura = self.lado1
            else:
                altura = self.lado1
        elif self.lado3 >= self.lado1 and self.lado3 >= self.lado2 and self.lado3 >= self.lado4:
            base = self.lado3
            if self.lado1 == self.lado3:
                altura = self.lado2
            elif self.lado2 == self.lado3:
                altura = self.lado1
            else:
                altura = self.lado1
        else:
            base = self.lado4
            if self.lado1 == self.lado4:
                altura = self.lado3
            elif self.lado2 == self.lado4:
                altura = self.lado3
            else:
                altura = self.lado1
        
        self.area = base * altura

    def calcula_perimetro(self):
        for lado in self.lados:
            self.perimetro += lado

        
class Triangulo(Forma):

    def __init__(self, lado1, lado2, lado3, altura):
        self.alt = altura
        self.lados = [lado1, lado2, lado3]

        print(self.lados)

    def calcula_area(self):
        if self.lados[0] >= self.lados[1] and self.lados[0] >= self.lados[2]:
            base = self.lados[0]

        elif self.lados[1] >= self.lados[0] and self.lados[1] >= self.lados[2]:
            base = self.lados[1]

        elif self.lados[2] >= self.lados[0] and self.lados[2] >= self.lados[1]:
            base = self.lados[2]

        self.area = (base * self.alt)/2

    def calcula_perimetro(self):
        self.perimetro = sum(self.lados)