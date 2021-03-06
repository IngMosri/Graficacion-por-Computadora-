#librerias
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class ParabolaPuntoMedio:
    #definicion de variables
    def __init__(self,xcentro, ycentro, altura):
        self.xcentro = xcentro
        self.ycentro = ycentro
        self.altura = altura
        self.img = Image.fromarray(np.zeros((500, 500), dtype=np.float32), mode= "F")
    
    #funcion que guarda los puntos y la simetria
    def plotPoint(self, x, y):
        self.img.putpixel((x + self.xcentro, y + self.ycentro),3)
        self.img.putpixel(( x + self.xcentro, - y + self.ycentro),3)
    #funcion main que evalua con el ciclo los puntos a graficar
    def paraMid(self):
        x = 0
        y = 0
        p = 1
        self.plotPoint(x,y)

        while (x <= self.altura):
            x = x + 1
            if p > 0:
                y = y + 1
                p = p - 2 * y + 1
            else:
                p = p + 1
                self.plotPoint(x,y)
        
        img = np.transpose(self.img)
        plt.imshow(np.array(img))
        plt.show()