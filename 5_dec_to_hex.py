def dec_to_hex(d: int) -> str:

    if d == 0:
        return "0"

    
    sinal = ""
    if d < 0:
        sinal = "-"
        d = abs(d)

    
    mapa_hex = "0123456789ABCDEF"
    hex_invertido = ""

    
    while d > 0:
        
        resto = d % 16
        
        hex_invertido += mapa_hex[resto]
        
        
        d = d // 16

    
    resultado_hex = hex_invertido[::-1]

    
    return sinal + resultado_hex

def main():
    
    print("--- Conversor de Decimal Inteiro para Hexadecimal ---")
    print("Digite um número inteiro para converter.\n")

    while True:
        entrada_usuario = input("Digite o número decimal: ")


        try:
            numero_decimal = int(entrada_usuario)
            resultado = dec_to_hex(numero_decimal)
            print(f"O número decimal {numero_decimal} em hexadecimal é: {resultado}\n")
        except ValueError:
            print(f"Erro: '{entrada_usuario}' não é um inteiro válido. Tente novamente.\n")

if __name__ == "__main__":
    main()