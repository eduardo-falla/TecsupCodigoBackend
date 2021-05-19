# numero=int(input("ingrese un numero: \n"))

# if numero >0:
#     print("es positivo")
# elif numero <0:
#     print("numero es negativo")
# elif numero==0:
#     print("numero es igual a 0")
# numeros= [1, -4, 5, -14, -16, -50, 6, -100]
# positivos=0
# negativos=0


# for a in numeros:
#     if a>0:
#         positivos+=1
#     else:
#         negativos+=1

# print(f"hay {positivos} positivos y {negativos} negativos.")



misnumeros = [1, 2, 5, 9, 12, 15, 10, 34, 867, 67]
mult_5=0

mult_3=0


 
 
for a in misnumeros:
    if(a%3==0 and a%5==0):
        print("multxx")
        continue
    elif(a%3==0 and a%5!=0) : 
        print("mul3")
        mult_3+=1
    elif(a%5==0 and a%3!=0) :
        mult_5+=1
        print("mul5")
    else:
        print("nada3")

print(f"multiplo de 5 :{mult_5} ")
print(f"multiplo de 3 :{mult_3} ")
