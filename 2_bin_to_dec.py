def bin_to_dec(b: str) -> int:
   
    if not isinstance(b, str) or not b.strip():
        raise ValueError("A entrada deve ser uma string não vazia.")
    
    b = b.strip() 
    sinal = 1
    binario_sem_sinal = b

    
    if b.startswith('-'):
        sinal = -1
        binario_sem_sinal = b[1:] 
    elif b.startswith('+'):
        binario_sem_sinal = b[1:]

    
    if not binario_sem_sinal:
        raise ValueError(f"Entrada '{b}' é inválida. A string binária não pode ser vazia.")

    for digito in binario_sem_sinal:
        if digito not in ('0', '1'):
            raise ValueError(f"Entrada inválida. O caractere '{digito}' não pertence ao alfabeto binário.")

    
    valor_decimal = 0
    
    binario_invertido = binario_sem_sinal[::-1]

    for i, digito in enumerate(binario_invertido):
        if digito == '1':
            valor_decimal += 2**i
            
    
    return valor_decimal * sinal

def main():
    
    print("--- Conversor de Binário para Decimal Inteiro ---")
    print("Digite um número binário para converter.\n")
    
    while True:

        entrada_usuario = input("Digite o número binário: ")

        try:
            
            resultado_decimal = bin_to_dec(entrada_usuario)
            print(f"O número binário '{entrada_usuario}' em decimal é: {resultado_decimal}\n")

        except ValueError as e:
            
            print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()