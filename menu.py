from dda import DDA
from bresenham import Bresenham
from circulo_punto_medio import CirculoPuntoMedio
from circulo_dda  import CirculoDDA
from elipse_punto_medio import ElipsePuntoMedio
from punto_medio_parabola import ParabolaPuntoMedio
class Main_menu:
    
    def int_input(prompt):
        while True:
            try:
                coordinate = int(input(prompt))
                return coordinate
            except ValueError as e:
                print('El valor debe de ser numerico, por favor intenta ingresar otro valor')

    def menuSelection():
     
        correcto = False
        num = 0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto = True
            except ValueError:
                print('Error, choose a valid option ')
         
        return num
     
    salir = False
    opcion = 0
     
    while not salir:
     
        
        print("************Bienvenido a Graficacion por computadora**************")
        print("[1] Linea DDA")
        print("[2] Linea Breseenham")
        print("[3] Circulo DDA")
        print("[4] Circulo Punto Medio")
        print("[5] Elipse Punto Medio")
        print("[6] Parabola")
        print("[7] Salir")
                
        opcion = menuSelection()
        
        if opcion == 1:

            x1 = int_input('Ingresa el valor numerico de x1: ')
            y1 = int_input('Ingresa el valor numerico de y1: ')
            x2 = int_input('Ingresa el valor numerico de x2: ')
            y2 = int_input('Ingresa el valor numerico de y2: ')

            dda = DDA(x1,y1,x2,y2)
            dda.main_dda()

        elif opcion == 2:

            x1 = int_input('Ingresa el valor numerico de x1: ')
            y1 = int_input('Ingresa el valor numerico de y1: ')
            x2 = int_input('Ingresa el valor numerico de x2: ')
            y2 = int_input('Ingresa el valor numerico de y2: ')

            bresenham = Bresenham(x1,y1,x2,y2)
            bresenham.main_bresenham()

        elif opcion == 3:

            radius = int_input('Ingresa el valor numerico del radio: ')
            circuloDDA = CirculoDDA(radius)
            circuloDDA.circle_main()
        elif opcion == 4:
            
            x = int_input('Ingresa el valor numerico de x: ')
            y = int_input('Ingresa el valor numerico de y: ')
            xcenter = int_input('Ingresa el valor numerico de centro de x: ')
            ycenter = int_input('Ingresa el valor numerico de centro de y: ')

            c_punto_medio = CirculoPuntoMedio(x, y, ycenter, xcenter)
            c_punto_medio.midPoint_Circle()

        elif opcion == 5:
            
            major = int_input('Ingresa el valor numerico mayor: ')
            minor = int_input('Ingresa el valor numerico de menor: ')
            xcenter = int_input('Ingresa el valor numerico de centro de x: ')
            ycenter = int_input('Ingresa el valor numerico de centro de y: ')

            elipse = ElipsePuntoMedio(major, minor, xcenter, ycenter)
            elipse.elipse_main()

        elif opcion == 6:
            xcenter = int_input('Ingresa el valor numerico de centro de x: ')
            ycenter = int_input('Ingresa el valor numerico de centro de y: ')
            longitud = int_input('Ingresa el valor de longitud: ')
            
            p = ParabolaPuntoMedio(xcenter,ycenter,longitud)
            p.paraMid()

        elif opcion == 7:
            print ("Option 7")
        elif opcion == 8:
            print("Salir")
            salir = True
        else:
            print ("Choose the option beetween 1 and 8")
        
        print ("End")

        

