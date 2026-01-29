def dec_to_bin(d: int) -> str:
   
    if d == 0:
        return "0"

    
    sinal = ""
    if d < 0:
        sinal = "-"
        
        d = abs(d)

    binario_invertido = ""
    
    while d > 0:
        
        resto = d % 2
        binario_invertido += str(resto)
        
        d = d // 2
    
   
    resultado_binario = binario_invertido[::-1]

    return sinal + resultado_binario

def main():
    print("--- Conversor Decimal Inteiro para Binário ---")
    print("Digite um número inteiro para converter.\n")

    while True:
        entrada_usuario = input("Digite o número decimal: ")

        try:
            numero = int(entrada_usuario)

            resultado = dec_to_bin(numero)
            
            print(f"O número decimal {numero} em binário é: {resultado}\n")

        except ValueError:
            
            print(f"Erro: '{entrada_usuario}' não é uma entrada válida. Por favor, digite apenas um NÚMERO INTEIRO.\n")


if __name__ == "__main__":
    main()