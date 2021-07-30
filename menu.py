from dda_new import DDA_graphics
class Main_menu:
    
    def int_input(prompt):
        while True:
            try:
                coordinate = int(input(prompt))
                return coordinate
            except ValueError as e:
                print('El valor debe de ser numerico, por favor intenta ingresar otro valor')

    def show_dda_menu():
     
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("choose the following option : "))
                correcto=True
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
        print("[7] Poligono Regular")
        print("[8] Salir")
            
        print ("choose one option ")
        
        opcion = show_dda_menu()
        
        if opcion == 1:

            x1 = int_input('Ingresa el valor numerico de x1: ')
            y1 = int_input('Ingresa el valor numerico de y1: ')
            x2 = int_input('Ingresa el valor numerico de x2: ')
            y2 = int_input('Ingresa el valor numerico de y2: ')

            dda = DDA_graphics(x1,x2,y1,y2)
            dda.menu_main_dda()
            print ("Option 1")

        elif opcion == 2:
            print ("Option 2")
        elif opcion == 3:
            print ("Option 3")
        elif opcion == 4:
            print ("Option 4")
        elif opcion == 5:
            print ("Option 5")
        elif opcion == 6:
            print ("Option 6")
        elif opcion == 7:
            print ("Option 7")
        elif opcion == 8:
            print("Salir")
            salir = True
        else:
            print ("Choose the option beetween 1 and 8")
        
        print ("End")

        

