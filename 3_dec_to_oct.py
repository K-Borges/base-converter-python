def dec_to_oct(d: int) -> str:
    if d == 0:
        return "0"

    
    sinal = ""
    if d < 0:
        sinal = "-"
        
        d = abs(d)

    
    octal_invertido = ""
    while d > 0:
        
        resto = d % 8
        
        octal_invertido += str(resto)
        
        d = d // 8

    
    resultado_octal = octal_invertido[::-1]

   
    return sinal + resultado_octal

def main():
    
    print("--- Conversor de Decimal Inteiro para Octal ---")
    print("Digite um número inteiro para converter.\n")

    
    while True:
        entrada_usuario = input("Digite o número decimal: ")

        try:
           
            numero_decimal = int(entrada_usuario)
            
            
            resultado = dec_to_oct(numero_decimal)

            print(f"O número decimal {numero_decimal} em octal é: {resultado}\n")

        except ValueError:
            
            print(f"Erro: '{entrada_usuario}' não é um inteiro válido. Tente novamente.\n")


if __name__ == "__main__":
    main()