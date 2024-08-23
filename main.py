arquivo= 'oi.txt'  # Substitua pelo arquivo psorrrr, te amo ta 
resultado = []
def formatar_resposta(resposta):
  resposta = resposta.replace('[', '{')
  resposta = resposta.replace(']', '}')
  return resposta 

with open(arquivo, 'r') as file:
  num_operaçoes = int(file.readline().strip())
#Fazer o numero de operações que estão dadas no arquivo
  for i in range(num_operaçoes):
      OP = file.readline().strip()
      lista1 = file.readline().strip().split(",")
      lista2 = file.readline().strip().split(",")

      if OP == "U":
        for item in lista1:
            if item not in resultado:
              resultado.append(item)
        # Adiciona todos os numeros da segunda lista, se não estiverem na lista resultante
        for item in lista2:
            if item not in resultado:
                  resultado.append(item)
        operação = "União"

      elif OP == "I":
        # Verifica se cada numero da primeira lista está na segunda lista
        for item in lista1:
          # Se o numero estiver na segunda lista, adiciona na lista resultado
            if item in lista2 and item not in resultado:
              resultado.append(item)
        operação = "Interseção"

      elif OP == "D":
        # Verifica se cada numero da primeira lista está na segunda lista se não ele adiciona na lista resultado
        for item in lista1:
            if item not in lista2:
              resultado.append(item)
        operação = "Diferença"

      elif OP == "C":
        # Para cada numero da primeira e da segunda lista adicionar uma string no formato (numero1, numero2)

        resultado = [(x, y) for x in lista1 for y in lista2] 
        operação = "Produto Cartesiano"

      else:
          print("Você escreveu alguma operação invalida irmão")
          operação = "invalida"

     ## print(f"{i + 1}. {operação}: conjunto 1 {lista1}, conjunto 2 {lista2}. Resultado: {resultado} \n")
      print(formatar_resposta(f"{i + 1}. {operação}: conjunto 1 {lista1}, conjunto 2 {lista2}. Resultado: {resultado} \n"))

      resultado = []