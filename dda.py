#librerias para la ejecucion del programa 
import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class DDA:

    #definicion y inicializaicon de las variables 
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.img = Image.fromarray(np.zeros((150, 150), dtype=np.float32), mode= "F")

    
    def ROUND(self, n):
        return int(n+0.5)
        
    #configuracion y tamaño del cuadro a graficar 
    def dda(self):
        #Asignacion de los valores de las variables 
        x,y = self.x1,self.y1
        dx = (self.x2-self.x1)
        dy = (self.y2-self.y1)
        steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        Xinc = dx / float(steps)
        Yinc = dy / float(steps)
        self.img.putpixel((self.ROUND(x),self.ROUND(y)),3)
        print ('x = %s, y = %s' % (((self.ROUND(x),self.ROUND(y)))))
        for i in range(steps):
            x+= Xinc
            y+= Yinc
            print ('x = %s, y = %s' % (((self.ROUND(x),self.ROUND(y)))))
            self.img.putpixel((self.ROUND(x),self.ROUND(y)),3)
            time.sleep(.001)
        
        img = np.transpose(self.img)
        plt.imshow(np.array(img))
        plt.show()  

                
    def main_dda(self):   

        self.dda()
        print()