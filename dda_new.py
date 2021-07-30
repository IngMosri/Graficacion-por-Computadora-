import sys,pygame
from pygame import gfxdraw
class DDA_graphics:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
      

    def menu_dda():  
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
    
    def ROUND(self, n):
        return int(n+0.5)
        

    def dda(self):
        pygame.init()
        screen = pygame.display.set_mode((1000,1000))
        screen.fill((0,0,0))
        pygame.display.flip()

        white=(255,255,255)
        x,y = self.x1,self.y1
        length = (self.x2-self.x1) if (self.x2-self.x1) > (self.y2-self.y1) else (self.y2-self.y1)
        dx = (self.x2-self.x1)/float(length)
        dy = (self.y2-self.y1)/float(length)
        gfxdraw.pixel(screen, self.ROUND(x),self.ROUND(y), white)
        print ('x = %s, y = %s' % (((self.ROUND(x),self.ROUND(y)))))
        for i in range(length):
            x+= dx
            y+= dy
            print ('x = %s, y = %s' % (((self.ROUND(x),self.ROUND(y)))))
            gfxdraw.pixel(screen, self.ROUND(x), self.ROUND(y), white)
        pygame.display.flip()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                
    def menu_main_dda(self):   

        self.dda()
        print()
  
