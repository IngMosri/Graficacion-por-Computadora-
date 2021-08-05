#Liberias necesarias para el proyecto 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class CirculoPuntoMedio:

    #definicion e inicializacion de las variables 
    def __init__(self, x, y, ycenter, xcenter):
        self.x = x
        self.y = y
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.img = Image.fromarray(np.zeros((150, 150), dtype=np.float32), mode= "F")

    def midPoint_Circle(self):
        x = self.x
        xcenter = self.xcenter
        y = self.y
        ycenter = self.ycenter
# definicion del punto medio y la comprobacion de las variables de la imagen para el pixel a graficar 
        p = 1.25 - y
        self.img.putpixel((x+xcenter, y+ycenter), 3)
        self.img.putpixel((-x+xcenter, y+ycenter), 3)
        self.img.putpixel((x+xcenter, -y+ycenter), 3)
        self.img.putpixel((-x+xcenter, -y+ycenter), 3)
        if x!=y:
                self.img.putpixel((y+xcenter, x+ycenter), 3)
                self.img.putpixel((-y+xcenter, x+ycenter), 3)
                self.img.putpixel((y+xcenter, -x+ycenter), 3)
                self.img.putpixel((-y+xcenter, -x+ycenter), 3)
                #Comprobacion de las variables de x, y para la ecuacion del algoritmo 
        while(x<=y):
            x = x+1
            if(p >= 0):
                y -= 1
                p = p + 2*x - 2*y + 5
            else:
                p = p + 2*x + 3
            if(x>y):
                break
                #Comprobacion y pintado de pixel en la imagen 
            self.img.putpixel((x+xcenter, y+ycenter), 3)
            self.img.putpixel((-x+xcenter, y+ycenter), 3)
            self.img.putpixel((x+xcenter, -y+ycenter), 3)
            self.img.putpixel((-x+xcenter, -y+ycenter), 3)

            if x!=y:
                self.img.putpixel((y+xcenter, x+ycenter), 3)
                self.img.putpixel((-y+xcenter, x+ycenter), 3)
                self.img.putpixel((y+xcenter, -x+ycenter), 3)
                self.img.putpixel((-y+xcenter, -x+ycenter), 3)




        img = np.transpose(self.img)
        plt.imshow(np.array(img))
        plt.show()