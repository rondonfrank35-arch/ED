import turtle

class fractaldecuadrados:
    def _init_(self, angulodegiro, velocidad=0):
        self.angulodegiro = angulodegiro
        self.tortuga=turtle.Turtle()
        self.tortuga.speed(velocidad)
    def dibujarCuadradoBase(self, lado):
        for _ in range(4):
            self.tortuga.forward(lado)
            self.tortuga.right(90)
    def dibujarConCiclo(self,numeroDeCuadrados,lado):
        for _ in range(numeroDeCuadrados):
            self.dibujarCuadradoBase(lado)
            self.tortuga.right(self.angulodegiro)
    def dibujarConRecursivo(self,numeroDeCuadrados,lado):
        if numeroDeCuadrados <= 0:
            return
        else:
            self.tortuga.right(self.angulodegiro)
            self.dibujarConRecursivo(numeroDeCuadrados - 1, lado)
angulodegiro=10       
numeroDeCuadrados=360//angulodegiro
velocidad=0
fractal= fractaldecuadrados(angulodegiro,velocidad)
fractal.dibujarConCiclo(numeroDeCuadrados=numeroDeCuadrados, lado=150)
fractal.dibujarConRecursivo(numeroDeCuadrados=numeroDeCuadrados, lado=100)

turtle.done()