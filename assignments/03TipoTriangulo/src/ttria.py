def main():
    #escribe tu código abajo de esta línea
    #que no ya lo habiamos hecho en clase 
    x=int(input("Lado x: "))
    y=int(input("Lado y: "))
    z=int(input("Lado z: "))
    
    if x>0 and y>0 and z>0:
      if x+y>z and y+z>x and z+x>y:
        if x==y and x==z:
            print("Es equilatero")
        elif x==y and x==z or y==z:
            print("Es isoseles")  
        else: 
            print("Es escaleno")  
      else:
        print("No es un triangulo") 
   else:
     print("No es un triangulo")     
            
            
if __name__=='__main__':
    main()
