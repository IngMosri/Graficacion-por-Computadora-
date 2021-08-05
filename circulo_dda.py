import PIL.Image, PIL.ImageDraw
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class CirculoDDA:

    def __init__(self, radius, xcenter, ycenter):
        self.radius = radius
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.img = Image.fromarray(np.zeros((650, 650), dtype=np.float32), mode= "F")

        

    def circle(self, radius):
        
        # iniciador de variables 
        xcenter = self.xcenter
        ycenter = self.ycenter
        switch = 3 - (2 * radius)
        points = set()
        x = 0
        y = radius
        # El primer cuadrante y octato empezara a las 12 am como las manecillas del reloj
        
        while x <= y:
            
            # primer cuarto primer octante
            self.img.putpixel((x + ycenter ,-y + xcenter),3)
            points.add((x,-y))
            #  primer cuarto segundo octante
            self.img.putpixel((y + ycenter,-x + xcenter ),3)
            points.add((y,-x))
            # segundo cuarto tercero octante
            self.img.putpixel((y + ycenter,x + xcenter ),3)
            points.add((y,x))
            # segundo cuarto cuarto octante
            self.img.putpixel((x + ycenter ,y + xcenter),3)
            points.add((x,y))
            # tercer cuarto quinto octante
            self.img.putpixel((-x + ycenter ,y + xcenter),3)
            points.add((-x,y))        
            # tercer cuarto sexto octante
            self.img.putpixel((-y + ycenter,x + xcenter ),3)
            points.add((-y,x))  
            # cuarto cuarto septimo octante
            self.img.putpixel((-y + ycenter,-x + xcenter ),3)
            points.add((-y,-x))
            # cuarto  cuarto octavo octante
            self.img.putpixel((-x + ycenter ,-y + xcenter),3)
            points.add((-x,-y))
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
        return points
        #tamaño del radio que se va graficar 
    def circle_main(self):
        size = 200
        radius = self.radius
        circle_graph = PIL.Image.new("RGB", (size, size), (30,25,20))
        draw = PIL.ImageDraw.Draw(circle_graph)
        p = self.circle(radius)
        #impre las cordenadas 
        print (p)
        for point in p:
            draw.point((size/2+point[0],size/2+point[1]),(255,255,255))
        #circle_graph.show()
        img = np.transpose(self.img)
        plt.imshow(np.array(img))
        plt.show()  