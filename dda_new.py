import sys,pygame
from pygame import gfxdraw
class DDA_graphics:
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
    def int_input(prompt):
        while True:
            try:
                coordinate = int(input(prompt))
                return coordinate
            except ValueError as e:
                print('El valor debe de ser numerico, por favor intenta ingresar otro valor')
    
    def ROUND(n):
        
        return int(n+0.5)
        

    def dda(x1,y1,x2,y2):
        pygame.init()
        screen = pygame.display.set_mode((1000,1000))
        screen.fill((0,0,0))
        pygame.display.flip()

        white=(255,255,255)
        x,y = x1,y1
        length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
            dx = (x2-x1)/float(length)
            dy = (y2-y1)/float(length)
            gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)
        
                


            for i in range(length):
                x+= dx
                y+= dy
                gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)
            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                
    def menu_main_dda():
        
        x1 = int_input('Ingresa el valor numerico de x1: ')
        y1 = int_input('Ingresa el valor numerico de y1: ')
        x2 = int_input('Ingresa el valor numerico de x2: ')
        y2 = int_input('Ingresa el valor numerico de y2: ')     

        dda(x1,y1,x2,y2)
        



        


  

 
  
