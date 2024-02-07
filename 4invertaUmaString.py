def inverte_string(string):
    # Inicializa uma string vazia para armazenar o resultado da inversão
    string_invertida = ""
    
    # Itera sobre os caracteres da string de trás para frente
    for i in range(len(string) - 1, -1, -1):
        # Adiciona cada caractere à string invertida
        string_invertida += string[i]
    
    return string_invertida

if __name__ == "__main__":
    # String a ser invertida
    minha_string = "Olá, mundo!"

    # Inverte a string
    string_invertida = inverte_string(minha_string)

    # Imprime o resultado
    print("String original:", minha_string)
    print("String invertida:", string_invertida)
