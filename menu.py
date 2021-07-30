   import dda_new
class Main_menu:
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
            dda_new.DDA_graphics.menu_main_dda()
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


        

