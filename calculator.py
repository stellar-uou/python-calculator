def calculadora():
  print("Olá! Seja bem-vindo(a) para a calculadora python.")

  num_1 = float(input("Digite o primeiro número: "))
  num_2 = float(input("Digite o segundo número: "))

  operacao = input("""
  Digite o número da operação que deseja realizar:

    1 - Adição (+)
    2 - Subtração (-)
    3 - Multiplicação (*)
    4 - Divisão (/)

    """)
  if operacao == "1":
    resultado = num_1 + num_2
    print(f"{num_1} + {num_2} = {resultado}")

  elif operacao == "2":
    resultado = num_1 - num_2
    print(f"{num_1} - {num_2} = {resultado}")

  elif operacao == "3":
    resultado = num_1 * num_2
    print(f"{num_1} * {num_2} = {resultado}")

  elif operacao == "4":
    if num_2 != 0:
      resultado = num_1 / num_2
      print(f"{num_1} / {num_2} = {resultado}")
    
    else: 
      print("Não é possível fazer uma divisão por 0, escolha outro número e tente novamente.")
  
  else:
    print("Operação inválida. Por favor, escolha outro número e tente novamente.")

calculadora()
