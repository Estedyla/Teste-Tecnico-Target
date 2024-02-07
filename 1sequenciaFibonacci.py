def calcula_fibonacci_ate(numero):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < numero:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)
    return fibonacci_sequence

def verifica_fibonacci(numero, fibonacci_sequence):
    return numero in fibonacci_sequence

if __name__ == "__main__":
    # Definição do número a ser verificado
    numero_verificar = 21

    # Cálculo da sequência de Fibonacci até o número fornecido
    fibonacci_sequence = calcula_fibonacci_ate(numero_verificar)

    # Verifica se o número está na sequência de Fibonacci
    if verifica_fibonacci(numero_verificar, fibonacci_sequence):
        print(f"{numero_verificar} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero_verificar} não pertence à sequência de Fibonacci.")
