def hex_to_dec(h: str) -> int:
   
    if not isinstance(h, str) or not h.strip():
        raise ValueError("A entrada deve ser uma string não vazia.")
    
    h = h.strip()
    sinal = 1
    hex_sem_sinal = h

    
    if h.startswith('-'):
        sinal = -1
        hex_sem_sinal = h[1:]
    elif h.startswith('+'):
        hex_sem_sinal = h[1:]

    
    hex_sem_sinal = hex_sem_sinal.upper()

    
    if not hex_sem_sinal:
        raise ValueError(f"Entrada '{h}' é inválida. A string não pode conter apenas o sinal.")

    
    mapa_decimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
                    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    
    valor_decimal = 0
    
    hex_invertido = hex_sem_sinal[::-1]

    for i, digito_hex in enumerate(hex_invertido):
       
        if digito_hex not in mapa_decimal:
            raise ValueError(f"Caractere inválido na string hexadecimal: '{digito_hex}'.")
        
        valor_do_digito = mapa_decimal[digito_hex]
        
        valor_decimal += valor_do_digito * (16**i)
        
    return valor_decimal * sinal

def main():
    
    print("--- Conversor de Hexadecimal para Decimal Inteiro ---")
    print("Digite um número hexadecimal para converter.\n")
    
    while True:
        entrada_usuario = input("Digite o número hexadecimal: ")

        
        try:
            resultado = hex_to_dec(entrada_usuario)
            print(f"O número hexadecimal '{entrada_usuario}' em decimal é: {resultado}\n")
        except ValueError as e:
            
            print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()