def entradaDeDados():
    answer = str(input('Insira o Valor:'))
    return answer


a = entradaDeDados()

print(f"R$ {float(a)}")