def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        sequencia = fibonacci(n - 1)
        sequencia.append(sequencia[-1] + sequencia[-2])
        return sequencia


def verificar_numero(numero):
    sequencia = fibonacci(numero)
    if numero == 0:  # Check if the number is 0
        print(f"O número {numero} pertence à sequência de Fibonacci.")
        return
    for i in range(len(sequencia) - 1):
        if numero == sequencia[i] + sequencia[i + 1]:
            print(f"O número {numero} pertence à sequência de Fibonacci.")
            return
    print(f"O número {numero}, não pertence à sequência de Fibonacci")


# Testes
verificar_numero(0)
verificar_numero(1)
verificar_numero(2)
verificar_numero(3)
verificar_numero(4)
verificar_numero(5)
verificar_numero(100)
verificar_numero(610)
verificar_numero(987)
verificar_numero(988)
