def binfrac_to_dec(b: str) -> float:
    
    if not isinstance(b, str) or not b.strip():
        raise ValueError("A entrada deve ser uma string não vazia.")
    
    b = b.strip()
    sinal = 1
    
    if b.startswith('-'):
        sinal = -1
        b = b[1:] 

    
    partes = b.split('.')
    parte_inteira_str = ""
    parte_fracionaria_str = ""

    if len(partes) == 1:
        parte_inteira_str = partes[0]
    elif len(partes) == 2:
        parte_inteira_str = partes[0]
        parte_fracionaria_str = partes[1]
    else:
        
        raise ValueError("Formato de número inválido: múltiplos pontos decimais.")

    
    if not parte_inteira_str and not parte_fracionaria_str:
        raise ValueError("A string binária não pode ser vazia ou conter apenas o ponto/sinal.")

    
    valor_decimal = 0.0

    
    if parte_inteira_str:
        for i, digito in enumerate(parte_inteira_str[::-1]): 
            if digito == '1':
                valor_decimal += 2**i
            elif digito != '0': 
                raise ValueError(f"Caractere inválido na parte inteira: '{digito}'.")

    
    if parte_fracionaria_str:
        for i, digito in enumerate(parte_fracionaria_str):
            if digito == '1':
                
                valor_decimal += 2**(-(i + 1))
            elif digito != '0': 
                raise ValueError(f"Caractere inválido na parte fracionária: '{digito}'.")

    
    return valor_decimal * sinal

def main():
    
    print("--- Conversor de Binário Fracionário para Decimal ---")
    print("Digite um número binário (ex: -11.011).")
    
    while True:
        entrada = input("Digite o número binário fracionário: ")
        try:
            resultado = binfrac_to_dec(entrada)
            print(f"Resultado para '{entrada}': {resultado}\n")
        except ValueError as e:
            print(f"Erro: {e}\n")

if __name__ == "__main__":
    main()