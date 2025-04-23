lado1 = float(input('digite o lado do triangulo: '))
lado2 = float(input('digite o lado do triangulo: '))
lado3 = float(input('digite o lado do triangulo: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:

    if lado1 == lado2 == lado3:
     print("equilatero")
     
    elif lado1 == lado2 or lado1 == lado3 or  lado2 == lado3:
       print("isoceles")

    else:
       print("escaleno")
       
else:
   print("os valores fornecidos n forma um triangulo valido ")
