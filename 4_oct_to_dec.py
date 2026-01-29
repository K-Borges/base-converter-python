def oct_to_dec(o: str) -> int:
    
    if not isinstance(o, str) or not o.strip():
        raise ValueError("A entrada deve ser uma string não vazia.")
    
    o = o.strip()  
    sinal = 1
    octal_sem_sinal = o

    
    if o.startswith('-'):
        sinal = -1
        octal_sem_sinal = o[1:] 
    elif o.startswith('+'):
        octal_sem_sinal = o[1:]
    
    
    if not octal_sem_sinal:
        raise ValueError(f"Entrada '{o}' é inválida. A string não pode conter apenas o sinal.")

    
    caracteres_validos = "01234567"
    for digito in octal_sem_sinal:
        if digito not in caracteres_validos:
            raise ValueError(f"Entrada inválida. O caractere '{digito}' não pertence ao alfabeto octal (0-7).")

    
    valor_decimal = 0
    
    octal_invertido = octal_sem_sinal[::-1]

    for i, digito_str in enumerate(octal_invertido):
        digito_int = int(digito_str)
        
        valor_decimal += digito_int * (8**i)
        
    return valor_decimal * sinal

def main():
    
    print("--- Conversor de Octal para Decimal Inteiro ---")
    print("Digite um número octal para converter.\n")
    
    
    while True:
        entrada_usuario = input("Digite o número octal: ")

        
        try:
            
            resultado = oct_to_dec(entrada_usuario)
            print(f"O número octal '{entrada_usuario}' em decimal é: {resultado}\n")

        except ValueError as e:
           
            print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()