def nome_completo(nome, sobrenome):
  return f'{nome} {sobrenome}'

nome01 = input("Digite seu nome: ")
sobrenome01 = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

nome_idade = (f"Meu nome é: {nome_completo(nome01, sobrenome01)} e a idade é: {idade}")

print(nome_idade)