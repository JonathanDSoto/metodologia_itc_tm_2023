
num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))
num3 = int(input("Ingrese num3: "))

if (num1 > num2 ):
    if(num2 > num3):
        print("El mayor es: ",num1)
        
if(num2 > num1 and num2 > num3):
    print("El mayor es: ",num2)
    
if(num3 > num1 and num3 > num2):
    print("El mayor es: ",num3)
