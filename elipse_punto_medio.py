import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class ElipsePuntoMedio:

    def __init__(self, major, minor, xcenter, ycenter):
        self.major = major
        self.minor = minor
        self.xcenter = xcenter
        self.ycenter = ycenter
        self.img = Image.fromarray(np.zeros((150, 150), dtype=np.float32), mode= "F")
    
    def ellipse(self):
        major = self.major
        minor = self.minor
        xcenter = self.xcenter
        ycenter =  self.ycenter

        x = 0
        y = minor
        p1 = minor**2 - (major**2 * minor) + (0.25 * major**2)
        dx = 2 * minor**2 * x
        dy = 2 * major**2 * y
        self.img.putpixel((x+xcenter, y+ycenter), 3)
        self.img.putpixel((-x+xcenter, y+ycenter), 3)
        self.img.putpixel((x+xcenter, -y+ycenter), 3)
        self.img.putpixel((-x+xcenter, -y+ycenter), 3)

        # Region 1
        while(dx < dy):
            x += 1
            if (p1 < 0):
                dx = 2 * minor**2 * x
                p1 = p1 + dx + minor**2
            else:
                y -= 1
                dx = 2 * minor**2 * x
                dy = 2 * major**2 * y
                p1 = p1 + dx -dy + minor**2
            self.img.putpixel((x+xcenter, y+ycenter), 3)
            self.img.putpixel((-x+xcenter, y+ycenter), 3)
            self.img.putpixel((x+xcenter, -y+ycenter), 3)
            self.img.putpixel((-x+xcenter, -y+ycenter), 3)

        # Region 2
        p2 = (minor * (x + 0.5))**2 + (major * (y-1))**2 - (major * minor)**2
        if(dx >= dy):
            while(y>=0):
                self.img.putpixel((x+xcenter, y+ycenter), 3)
                y -= 1
                if(p2>0):
                    dy = 2 * major**2 * y
                    p2 = p2 - dy + major**2
                else:
                    x += 1
                    dy = 2 * major**2 * y
                    dx = 2 * minor**2 * x
                    p2 = p2 + dx - dy + major**2
                self.img.putpixel((x+xcenter, y+ycenter), 3)
                self.img.putpixel((-x+xcenter, y+ycenter), 3)
                self.img.putpixel((x+xcenter, -y+ycenter), 3)
                self.img.putpixel((-x+xcenter, -y+ycenter), 3)

        

        plt.imshow(np.array(self.img))
        plt.show()
    
    def elipse_main(self):
        self.ellipse()
