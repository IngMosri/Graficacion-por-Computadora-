import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
class CirculoPuntoMedio:

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
        while(x<=y):
            x = x+1
            if(p >= 0):
                y -= 1
                p = p + 2*x - 2*y + 5
            else:
                p = p + 2*x + 3
            if(x>y):
                break
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