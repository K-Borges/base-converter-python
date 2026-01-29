import sys

MAPA_PARA_DECIMAL = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,
    'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
    'W': 32, 'X': 33, 'Y': 34, 'Z': 35
}
MAPA_DE_DECIMAL = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def _any_base_frac_to_dec_float(num_str: str, base_from: int) -> float:

    valor_decimal = 0.0
    for i, digito in enumerate(num_str):
        valor_do_digito = MAPA_PARA_DECIMAL[digito]
        if valor_do_digito >= base_from:
            raise ValueError(f"Dígito '{digito}' inválido para a base {base_from}.")
        valor_decimal += valor_do_digito * (base_from**(-(i + 1)))
    return valor_decimal

def _dec_float_to_any_base_frac(frac_dec: float, base_to: int, max_digits: int) -> str:
    
    if frac_dec == 0:
        return ""
    
    resultado_frac = ""
    for _ in range(max_digits):
        if frac_dec == 0:
            break
        frac_dec *= base_to
        digito_int = int(frac_dec)
        resultado_frac += MAPA_DE_DECIMAL[digito_int]
        frac_dec -= digito_int
    return resultado_frac

def convert_base_frac(num: str, base_from: int, base_to: int, max_frac_digits: int = 16) -> str:
    
    if not (2 <= base_from <= 36 and 2 <= base_to <= 36):
        raise ValueError("As bases devem estar no intervalo de 2 a 36.")
    
    num_limpo = num.strip().upper()
    sinal = ""
    if num_limpo.startswith('-'):
        sinal = "-"
        num_limpo = num_limpo[1:]

    partes = num_limpo.split('.')
    parte_inteira_str = partes[0]
    parte_fracionaria_str = partes[1] if len(partes) > 1 else ""

    
    valor_inteiro_dec = 0
    if parte_inteira_str:
        for i, digito in enumerate(parte_inteira_str[::-1]):
            valor_do_digito = MAPA_PARA_DECIMAL[digito]
            if valor_do_digito >= base_from:
                raise ValueError(f"Dígito '{digito}' inválido para a base {base_from}.")
            valor_inteiro_dec += valor_do_digito * (base_from**i)
    
    
    valor_fracionario_dec = 0.0
    if parte_fracionaria_str:
        valor_fracionario_dec = _any_base_frac_to_dec_float(parte_fracionaria_str, base_from)

    
    if valor_inteiro_dec == 0:
        parte_inteira_final = "0"
    else:
        temp_int = valor_inteiro_dec
        parte_inteira_final_invertida = ""
        while temp_int > 0:
            resto = temp_int % base_to
            parte_inteira_final_invertida += MAPA_DE_DECIMAL[resto]
            temp_int //= base_to
        parte_inteira_final = parte_inteira_final_invertida[::-1]

    
    parte_fracionaria_final = ""
    if valor_fracionario_dec > 0:
        parte_fracionaria_final = _dec_float_to_any_base_frac(valor_fracionario_dec, base_to, max_frac_digits)

    
    if parte_fracionaria_final:
        return sinal + parte_inteira_final + "." + parte_fracionaria_final
    else:
        return sinal + parte_inteira_final



def to_twos_complement(n: int, bits: int) -> str:
    
    limite = 2**bits
    limite_positivo = (limite // 2) - 1
    limite_negativo = -(limite // 2)

    if not (limite_negativo <= n <= limite_positivo):
        raise ValueError(f"Número {n} fora do intervalo [{limite_negativo}, {limite_positivo}] para {bits} bits.")

    if n >= 0:
        
        bin_str = bin(n)[2:]
        return bin_str.zfill(bits)
    else:
        
        valor_positivo_equivalente = (2**bits) + n
        bin_str = bin(valor_positivo_equivalente)[2:]
        return bin_str.zfill(bits)

def from_twos_complement(b: str) -> int:
    
    bits = len(b)
    
    for char in b:
        if char not in '01':
            raise ValueError("A string deve conter apenas '0' e '1'.")

    valor_sem_sinal = int(b, 2)

    
    if b[0] == '1':
        
        return valor_sem_sinal - (2**bits)
    else:
        
        return valor_sem_sinal



def run_cli():
    
    args = sys.argv[1:]
    if len(args) != 6 or '--from' not in args or '--to' not in args or '--num' not in args:
        print("Uso: python seu_arquivo.py --from <base_origem> --to <base_destino> --num <numero>")
        print("Exemplo: python seu_arquivo.py --from 10 --to 16 --num -7B")
        sys.exit(1)

    try:
        idx_from = args.index('--from') + 1
        idx_to = args.index('--to') + 1
        idx_num = args.index('--num') + 1

        base_from = int(args[idx_from])
        base_to = int(args[idx_to])
        num = args[idx_num]
        
        
        resultado = convert_base_frac(num, base_from, base_to)
        print(resultado)

    except (ValueError, IndexError) as e:
        print(f"Erro: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    
    if len(sys.argv) > 1:
        run_cli()
    else:
        
        print("--- Demonstração dos Desafios Bônus ---")
        
        print("\n--- B1: Bases Fracionárias ---")
        try:
            print(f'convert_base_frac("1A.8", 16, 10) -> "{convert_base_frac("1A.8", 16, 10)}"')
            print(f'convert_base_frac("26.5", 10, 16) -> "{convert_base_frac("26.5", 10, 16)}"')
            print(f'convert_base_frac("1010.101", 2, 10) -> "{convert_base_frac("1010.101", 2, 10)}"')
            print(f'convert_base_frac("-10.625", 10, 2, max_frac_digits=8) -> "{convert_base_frac("-10.625", 10, 2, 8)}"')
        except ValueError as e:
            print(f"Erro: {e}")

        print("\n--- B2: Complemento de Dois ---")
        try:
            print(f'to_twos_complement(5, 8) -> "{to_twos_complement(5, 8)}"')
            print(f'to_twos_complement(-5, 8) -> "{to_twos_complement(-5, 8)}"')
            print(f'to_twos_complement(-1, 4) -> "{to_twos_complement(-1, 4)}"')
            print(f'from_twos_complement("00000101") -> {from_twos_complement("00000101")}')
            print(f'from_twos_complement("11111011") -> {from_twos_complement("11111011")}')
            print(f'from_twos_complement("1111") -> {from_twos_complement("1111")}')
        except ValueError as e:
            print(f"Erro: {e}")
        
        print("\n--- B3: Teste da CLI ---")
        print("Para usar a CLI, execute no terminal:")
        print("python seu_arquivo.py --from 10 --to 2 --num 10.625")

if __name__ == "__main__":
    main()