def main():
    #escribe tu código abajo de esta línea
    #que no ya lo habiamos hecho en clase 
    x=int(input("Ingresa la media del Lado 1: "))
    y=int(input("Ingresa la media del Lado 2: "))
    z=int(input("Ingresa la media del Lado 3: "))
    
    if x>0 and y>0 and z>0:
      if x+y>z and y+z>x and z+x>y:
        if x==y and x==z:
            print("ES UN TRIANGULO EQUILATERO")
        elif x==y and x==z or y==z:
            print("ES UN TRIANGULO ISOSCELES")  
        else: 
            print("ES UN TRIANGULO ESCALENO")  
      else:
        print("NO ES UN TRIANGULO") 
   else:
     print("NO ES UN TRIANGULO")     
            

if __name__=='__main__':
    main()
