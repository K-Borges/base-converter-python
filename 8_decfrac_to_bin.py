def _dec_int_to_bin_str(n: int) -> str:
    
    if n == 0:
        return "0"

    bin_invertido = ""
    while n > 0:
        bin_invertido += str(n % 2)
        n //= 2
    return bin_invertido[::-1]

def _dec_frac_to_bin_str(frac: float, max_bits: int) -> str:
    
    if frac == 0:
        return "" 

    bin_frac = ""
    for _ in range(max_bits):
        
        if frac == 0:
            break
        
        frac *= 2
        
        if frac >= 1.0:
            bin_frac += "1"
            frac -= 1 
        
        else:
            bin_frac += "0"
            
    return bin_frac

def decfrac_to_bin(x: float, max_frac_bits: int = 16) -> str:
    
    sinal = ""
    if x < 0:
        sinal = "-"
        x = abs(x)

   
    parte_inteira = int(x)
    parte_fracionaria = x - parte_inteira

    
    parte_inteira_bin = _dec_int_to_bin_str(parte_inteira)

    
    parte_fracionaria_bin = _dec_frac_to_bin_str(parte_fracionaria, max_frac_bits)

    
    if not parte_fracionaria_bin:
        return sinal + parte_inteira_bin
    else:
        return sinal + parte_inteira_bin + "." + parte_fracionaria_bin

def main():
    
    print("--- Conversor de Decimal Fracionário para Binário ---")
    
    
    print("Digite um número (ex: 25.75).")
    
    while True:
        entrada = input("Digite o número decimal fracionário: ")
        
        try:
            numero = float(entrada)
            resultado = decfrac_to_bin(numero) 
            print(f"Resultado para {numero} (padrão 16 bits): {resultado}\n")
        except ValueError:
            print(f"Erro: '{entrada}' não é um número válido.\n")

if __name__ == "__main__":
    main()