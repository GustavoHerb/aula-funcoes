# import math

# #                     ATV 01
# # def nomes_personalidos(nome, sobrenome): 
# #   return f'{nome, sobrenome}'


# # nome = input("Digite seu nome: ")
# # sobrenome = input("Digite seu sobrenome: ")

# # printar_nomes = (f"Meu nome é: {nomes_personalidos(nome, sobrenome)}")

# # print(printar_nomes)


# #                    ATV 02



# # def horario_cumprimentos(horario, nome): 
  
# #   if horario > 5 and horario < 12:
# #     print(f"Bom dia {nome}")
# #   elif horario > 12 and horario < 18:
# #     print(f"Boa tarde {nome}")
# #   else: 
# #     print(f"Boa noite, {nome}")

# # nome = input("Qual o seu nome? ")
# # horario = int(input("Qual o horario local: "))

# # print(horario_cumprimentos(horario, nome))



# #                 ATV 03

# # def soma(num1, num2): 
# #   return num1 + num2

# # numero1 = int(input("Qual o primeiro numero: "))
# # numero2 = int(input("Qual o segundo numero: "))

# # print(soma(numero1, numero2))


# #               ATV 04

# # def subtraçao(num1, num2): 
# #   return num1 - num2

# # numero1 = int(input("Qual o primeiro numero: "))
# # numero2 = int(input("Qual o segundo numero: "))

# # print(subtraçao(numero1, numero2))


# # #               ATV 05

# # def  mult(num1, num2):
# #   return num1 * num2

# # numero1 = int(input("Qual o primeiro numero: "))
# # numero2 = int(input("Qual o segundo numero: "))

# # print(mult(numero1, numero2))



# #                      -----DESAFIO----


# def calculadora(num1, num2, opçao):

#   if opçao == 1:
#     return num1 + num2
#   if opçao == 2:
#     return num1 - num2
#   if opçao == 3:
#     return num1 * num2
#   if opçao == 4:
#     return num1 / num2
#   if opcao == 5: 
#     return num1 ^ num2
#   if opcao == 6: 
#     return math.sqrt(num1), math.sqrt(num2)

# while True:
#   escolha = input("Escreva 'continuar' para usar a calculadora, ou escreva 'sair' para sair da calculadora: ")
#   if escolha == 'sair':
#     print("Saindo da calculadora...")
#     break
#   elif escolha == 'continuar':
#     numero1 = int(input("Digite o primeiro numero: "))
#     numero2 = int(input("Digite o segundo numero: "))
#     opcao = int(input("Digite '1' para soma, digite '2' para subtrair, digite '3' para multiplicacao, digite '4' para a divisão, '5' para exponenciação, '6' para raiz quadrada de cada numero: ")) 
#     print(calculadora(numero1, numero2, opcao))
