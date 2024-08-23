arquivo = 'oi.txt'  # Substitua pelo arquivo correto
resultado = []

def formatar_resposta(resposta):
  resposta = resposta.replace('[', '{')
  resposta = resposta.replace(']', '}')
  return resposta

with open(arquivo, 'r') as file:
  num_operaçoes = int(file.readline().strip())
  for i in range(num_operaçoes):
    OP = file.readline().strip()
    lista1 = file.readline().strip().split(",")
    lista2 = file.readline().strip().split(",")

    if OP == "U":
        # União
        resultado = list(set(lista1) | set(lista2))
        operação = "União"

    elif OP == "I":
        # Interseção
        resultado = list(set(lista1) & set(lista2))
        operação = "Interseção"

    elif OP == "D":
        # Diferença
        resultado = list(set(lista1) - set(lista2))
        operação = "Diferença"

    elif OP == "C":
        # Produto Cartesiano
        resultado = [f"({x},{y})" for x in lista1 for y in lista2]
        operação = "Produto Cartesiano"

    else:
        print("Você escreveu alguma operação inválida irmão")
        operação = "inválida"
        resultado = []

    resposta = f"{i + 1}. {operação}: conjunto 1 {lista1}, conjunto 2 {lista2}. Resultado: {resultado} \n"
    print(formatar_resposta(resposta))
