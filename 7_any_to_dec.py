def any_base_to_dec(num_str: str, base_from: int) -> int:
   
    mapa_para_decimal = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,
        'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
        'W': 32, 'X': 33, 'Y': 34, 'Z': 35
    }
    
    valor_decimal = 0
    num_invertido = num_str[::-1]

    for i, digito in enumerate(num_invertido):
        valor_do_digito = mapa_para_decimal[digito]
        
        if valor_do_digito >= base_from:
            raise ValueError(
                f"O dígito '{digito}' não é válido para a base {base_from}."
            )
        
        valor_decimal += valor_do_digito * (base_from**i)
        
    return valor_decimal

def dec_to_any_base(num_dec: int, base_to: int) -> str:
    
    if num_dec == 0:
        return "0"

    mapa_de_decimal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    resultado_invertido = ""
    while num_dec > 0:
        resto = num_dec % base_to
        resultado_invertido += mapa_de_decimal[resto]
        num_dec //= base_to
        
    return resultado_invertido[::-1]


def convert_base(num: str, base_from: int, base_to: int) -> str:
    
    if not (2 <= base_from <= 36 and 2 <= base_to <= 36):
        raise ValueError("As bases devem estar no intervalo de 2 a 36.")

    
    if not isinstance(num, str) or not num.strip():
        raise ValueError("A string do número não pode ser vazia.")

    
    num_limpo = num.strip()
    sinal = ""
    if num_limpo.startswith('-'):
        sinal = "-"
        num_limpo = num_limpo[1:]
    
    if not num_limpo:
        raise ValueError("A string do número não pode conter apenas o sinal.")

    #
    num_maiusculo = num_limpo.upper()

    valor_decimal = any_base_to_dec(num_maiusculo, base_from)
    
    resultado_final = dec_to_any_base(valor_decimal, base_to)

    return sinal + resultado_final

def main():
    
    print("--- Conversor de Base Genérico (Base N -> Base M) ---")
    
    while True:
        try:
            num_str = input("Digite o número a ser convertido: ")
            
            
            from_str = input(f"Qual a base de '{num_str}'? ")
            

            to_str = input("Para qual base deseja converter? ")
            

            base_from = int(from_str)
            base_to = int(to_str)

            resultado = convert_base(num_str, base_from, base_to)
            print(f"Resultado: {resultado}\n")

        except ValueError as e:
            print(f"Erro: {e}\n")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}\n")

if __name__ == "__main__":
    main()