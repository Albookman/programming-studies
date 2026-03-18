# # Arithmetic Operations in Python
# # Integers

# print('Addition: ', 1 + 2)        # 3
# print('Subtraction: ', 2 - 1)     # 1
# print('Multiplication: ', 2 * 3)  # 6
# print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
# print('Division: ', 6 / 2)        # 3.0         
# print('Division: ', 7 / 2)        # 3.5
# print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
# print ('Division without the remainder: ',7 // 3)   # 2
# print('Modulus: ', 3 % 2)         # 1, Gives the remainder
# print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2

# # Floating numbers
# print('Floating Point Number, PI', 3.14)
# print('Floating Point Number, gravity', 9.81)

# # Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# # Declaring the variable at the top first

# a = 3 # a is a variable name and 3 is an integer data type
# b = 2 # b is a variable name and 3 is an integer data type

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
# print(total) # if you do not label your print with some string, you never know where the result is coming from
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# #Let us start connecting the dots and start making use of what we already know to calculate (area, volume,density, weight, perimeter, distance, force).

# #Calculando a área de um círculo: Raio: 10

# radius = 10
# circle_area = 3.14 * radius ** 2
# print ('Área do Círculo: ', circle_area)

# #Cálculo de Área de um Retângulo - Dados: Comprimento 20 Largura 10

# comprimento = 20
# largura = 10
# area_retangulo = comprimento * largura
# print ('Área do Retângulo: ', area_retangulo)

# #Cálculo do Peso de um Objeto - Dados Massa: 75 

# massa = 75
# gravidade = 9.81
# peso = massa * gravidade
# print ('peso: ', peso, 'N')

# #Cálculo de Densidade de um Líquido

# massa = 75 #em Kg
# volume = 0.075 #em m³
# densidade = massa / volume # Kg/m³
# print (densidade, 'kg/m³')

##Comparison Operators

# print (3 > 2)
# print (3 >= 2)
# print (3 <= 2)
# print (3 == 2)
# print (3 != 2)
# print (len ('mango') == len ('avocato'))
# print (len ('mango') != len ('avocato'))
# print (len ('mango') < len ('avocato'))
# print (len ('milk') != len ('meat'))
# print (len ('milk') == len ('meat'))
# print (len ('tomato') == len ('potato'))
# print (len ('python') > len ('dragon'))

# print ("True == True", True == True)
# print ("True == False", True == False)
# print ("False == False", False == False)

# print ("1 is 1", 1 is 1)
# print ("1 is not 1", 1 is not 1)
# print ("A in Alvaro", "A" in "Alvaro")
# print ("B not in alvaro", "B" not in "Alvaro")
# print ("A in an", "A" in "an")
# print ('4 is 2²', 4 is 2**2)

# print(3 > 2 and 4 > 3) # True - because both statements are true
# print(3 > 2 and 4 < 3) # False - because the second statement is false
# print(3 < 2 and 4 < 3) # False - because both statements are false
# print('True and True: ', True and True)
# print(3 > 2 or 4 > 3)  # True - because both statements are true
# print(3 > 2 or 4 < 3)  # True - because one of the statements is true
# print(3 < 2 or 4 < 3)  # False - because both statements are false
# print('True or False:', True or False)
# print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# print(not True)      # False - Negation, the not operator turns true to false
# print(not False)     # True
# print(not not True)  # True
# print(not not False) # False

#Exercises - Day 3

#1. Declare your age as integer variable

# age = int(input ("Age: ")) 
# print ("Minha Idade: " , age)
# print (type (age))

#2. Declare your height as a float variable

# altura = float (input ("Altura:  "))
# print ("Minha altura é: ", altura)
# print (type (altura))

#3.Declare a variable that store a complex number 

# complex_number = complex (input ("Número complexo: "))
# print ("Número complexo: ", complex_number)
# print (type (complex_number))

# #4. Escreva um script que solicite que o usuário insira a base e a altura do triângulo e calcule uma área deste triângulo

# base = int (input ("Informe o valor da base de um triângulo: "))
# altura = int (input ("Informe o valor da sua altura: "))
# area_tri = base * altura / 2
# print ("Área: ", area_tri ,"m²")

# #5. Escreva um script que solicite ao usuário informar os lados a, b e c de um triângulo. Calcule o seu perímetro.

# lado_a = int (input ("Informe o lado a de um triângulo: "))
# lado_b = int (input ("Informe o lado b de um triângulo: "))
# lado_c = int (input ("Informe o lado c de um triângulo: "))
# print ("O perímetro do triângulo é: ", lado_a + lado_b + lado_c)

# #6. Solicite a largura e comprimento de um retângulo através do prompt> Calcule a área e o perímetro do retângulo

# comp = int (input ("Informe o comprimento de um retângulo: "))
# altura = int (input ("Informe a altura do retângulo: "))
# area_ret = comp * altura
# perim_ret = (altura + comp) * 2
# print ("O perímetro do retângulo é: ", perim_ret)
# print ("A Área do retângulo é: " , area_ret)

# #7. Dado o raio de um círculo. Calcular a área e a circunferência.

# raio = int (input ("Informe o raio de um círculo: " ))
# area_circ = 3.14 * raio ** 2
# perim_circ = 2 * 3.14 * raio
# print ("A Área do Círculo é: ", area_circ)
# print ("A circunferência é: ", perim_circ)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope = 2
# x_intercept = 2/2
# y_intercept = -2

# print ("Dado a equação da reta y = 2x - 2 calcule:")
# print ("Inclinação da reta:", slope)
# print ("Interceptação da reta no eixo X: ", x_intercept)
# print ("Interceptação da reta no eixo y: ", y_intercept)

#9.Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Distância Euclidiana = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = (y2 - y1) /(x2 - x1)
dist_euc = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
dist_euc = round (dist_euc, 2)
print ("Slope: ", m)
print ("Distância Euclidiana entre os pontos: ", dist_euc)