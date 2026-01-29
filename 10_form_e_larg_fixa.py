def _dec_int_to_bin_str(n: int) -> str:
    
    if n == 0:
        return "0"
    bin_invertido = ""
    while n > 0:
        bin_invertido += str(n % 2)
        n //= 2
    return bin_invertido[::-1]

def _bin_str_to_dec_int(b: str) -> int:
    
    valor_decimal = 0
    for i, digito in enumerate(b[::-1]):
        if digito == '1':
            valor_decimal += 2**i
        elif digito != '0':
             raise ValueError(f"Dígito inválido '{digito}' na string binária.")
    return valor_decimal



def to_fixed_width_bin(n: int, bits: int) -> str:
    
    if n < 0:
        raise ValueError("O número de entrada não pode ser negativo.")
    if bits <= 0:
        raise ValueError("A largura em bits deve ser um inteiro positivo.")

    bin_str = _dec_int_to_bin_str(n)

    if len(bin_str) > bits:
        raise ValueError(
            f"O número {n} ({bin_str}) não cabe em {bits} bits."
        )

    
    padding = '0' * (bits - len(bin_str))
    return padding + bin_str



def ipv4_to_bin(ip: str) -> str:
    
    octetos = ip.split('.')
    if len(octetos) != 4:
        raise ValueError("Endereço IPv4 deve conter 4 octetos separados por ponto.")

    octetos_binarios = []
    for octeto_str in octetos:
        try:
            octeto_int = int(octeto_str)
            
            if not (0 <= octeto_int <= 255):
                raise ValueError(f"Octeto '{octeto_int}' está fora do intervalo válido (0-255).")
            
            
            octeto_bin = to_fixed_width_bin(octeto_int, 8)
            octetos_binarios.append(octeto_bin)

        except ValueError as e:
            
            if "invalid literal for int()" in str(e):
                 raise ValueError(f"Octeto '{octeto_str}' não é um número inteiro válido.")
            raise e

    return ".".join(octetos_binarios)



def bin_to_ipv4(bits: str) -> str:
    
    
    bits_limpos = bits.replace('.', '')
    
    
    if len(bits_limpos) != 32:
        raise ValueError(f"A string binária deve conter exatamente 32 bits, mas contém {len(bits_limpos)}.")
    
    octetos_decimais = []
    
    for i in range(0, 32, 8):
        octeto_bin = bits_limpos[i : i+8]
        try:
            octeto_int = _bin_str_to_dec_int(octeto_bin)
            octetos_decimais.append(str(octeto_int))
        except ValueError as e:
            
            raise ValueError(f"String contém caracteres não-binários. {e}")
            
    return ".".join(octetos_decimais)


def main():
    print("--- Exercício 10: Formatação e Largura Fixa ---")
    
    print("\n--- Tarefa 1: to_fixed_width_bin ---")
    try:
        print(f'to_fixed_width_bin(5, 8) -> "{to_fixed_width_bin(5, 8)}"')
        print(f'to_fixed_width_bin(255, 8) -> "{to_fixed_width_bin(255, 8)}"')
    except ValueError as e:
        print(f"Erro no teste: {e}")
        
    print("\n--- Tarefa 2: ipv4_to_bin ---")
    try:
        ip1 = "192.168.0.1"
        print(f'ipv4_to_bin("{ip1}") -> "{ipv4_to_bin(ip1)}"')
        ip2 = "10.0.8.255"
        print(f'ipv4_to_bin("{ip2}") -> "{ipv4_to_bin(ip2)}"')
    except ValueError as e:
        print(f"Erro no teste: {e}")

    print("\n--- Tarefa 3: bin_to_ipv4 ---")
    try:
        bin1 = "11000000.10101000.00000000.00000001"
        bin2 = "00001010000000000000100011111111" 
        print(f'bin_to_ipv4("{bin1}") -> "{bin_to_ipv4(bin1)}"')
        print(f'bin_to_ipv4("{bin2}") -> "{bin_to_ipv4(bin2)}"')
    except ValueError as e:
        print(f"Erro no teste: {e}")
        
    print("\n--- Teste de Erros ---")
    try:
        ipv4_to_bin("192.168.256.1")
    except ValueError as e:
        print(f'Erro esperado (OK): {e}')
    try:
        bin_to_ipv4("1010101")
    except ValueError as e:
        print(f'Erro esperado (OK): {e}')

if __name__ == "__main__":
    main()