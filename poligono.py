#librerias para la ejecucion del programa 
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class Polygono:

    def __init__(self, lados, radio, direction):
            self.lados = lados
            self.radio = radio
            self.direction = direction
            self.img = Image.fromarray(np.zeros((100, 100), dtype=np.float32), mode= "F")

    def ROUND(self, n):
        return int(n+0.5)

    def MainPolygono(self):
        p = self.lados
        r = self.radio
        d = self.direction

        i = 0
        x = 0
        y = 0
        t = 0

        while (i < p):
            t = 2 * math.pi * (i / p + d)
            x = math.cos(t)*r
            y = math.sin(t)*r
            self.img.putpixel((self.ROUND(x+50), self.ROUND(y+50)), 3)
            print("x", i,":", x, " y" , i ,":",y)
            i = i + 1
    
        plt.imshow(np.array(self.img))
        plt.show()
