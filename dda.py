import sys,pygame,time
from pygame import gfxdraw
class DDA:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
      
    
    def ROUND(self, n):
        return int(n+0.5)
        

    def dda(self):
        pygame.init()
        screen = pygame.display.set_mode((400,400))
        screen.fill((0,0,0))
        pygame.display.flip()

        white=(255,255,255)
        x,y = self.x1,self.y1
        dx = (self.x2-self.x1)
        dy = (self.y2-self.y1)
        steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        Xinc = dx / float(steps)
        Yinc = dy / float(steps)
        gfxdraw.pixel(screen, self.ROUND(x),self.ROUND(y), white)
        print ('x = %s, y = %s' % (((self.ROUND(x),self.ROUND(y)))))
        for i in range(steps):
            x+= Xinc
            y+= Yinc
            print ('x = %s, y = %s' % (((self.ROUND(x),self.ROUND(y)))))
            gfxdraw.pixel(screen, self.ROUND(x), self.ROUND(y), white)
            time.sleep(.001)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    running = False
        pygame.quit ()

                
    def main_dda(self):   

        self.dda()
        print()
  
