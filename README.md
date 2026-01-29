# Conversor de Bases Numéricas em Python

Este projeto contém um conjunto de funções em Python para a conversão entre diferentes bases numéricas. O principal diferencial é que todas as conversões são implementadas manualmente, utilizando algoritmos fundamentais (como divisões sucessivas e soma posicional), sem o uso de funções de conversão nativas do Python como `bin()`, `hex()` ou `int(x, base)`.

O código foi estruturado em funções "puras", que não possuem efeitos colaterais (como `input()` ou `print()`), tornando-as fáceis de testar e reutilizar em outros projetos.

## ✨ Funcionalidades

  - Conversão entre **Decimal, Binário, Octal e Hexadecimal**.
  - **Conversor genérico** para números inteiros entre qualquer base de 2 a 36.
  - Suporte a **números fracionários** no conversor genérico (Bônus B1).
  - Implementação de **Complemento de Dois** para representação de inteiros negativos com largura fixa (Bônus B2).
  - Conversão e formatação de endereços **IPv4** para binário e vice-versa.
  - Uma **Interface de Linha de Comando (CLI)** simples para acesso rápido à função de conversão geral (Bônus B3).
  - Validação robusta de entradas para evitar erros.

## 🚀 Como Usar

### Pré-requisitos

  - Python 3.6 ou superior.

### 1\. Modo de Demonstração (Interativo)

Para ver os exemplos de todas as funções implementadas e testá-las, basta executar o script diretamente no seu terminal. O programa irá rodar a função `main()` que contém casos de teste e exemplos práticos.

```bash
python conversor.py
```

### 2\. Interface de Linha de Comando (CLI)

Para conversões rápidas sem precisar alterar o código, você pode usar a interface de linha de comando. Ela foi criada para acessar diretamente a função de conversão genérica (inteiros e frações).

**Sintaxe:**

```bash
python conversor.py --from <base_origem> --to <base_destino> --num <numero>
```

**Exemplos de uso da CLI:**

  - **Converter um número binário para hexadecimal:**

    ```bash
    python conversor.py --from 2 --to 16 --num 11011010
    ```

    *Saída: `DA`*

  - **Converter um número hexadecimal negativo para octal:**

    ```bash
    python conversor.py --from 16 --to 8 --num -7B
    ```

    *Saída: `-173`*

  - **Converter um número decimal fracionário para binário:**

    ```bash
    python conversor.py --from 10 --to 2 --num 10.625
    ```

    *Saída: `1010.101`*

## 🛠️ Exemplo de Uso em Outro Script

As funções foram projetadas para serem facilmente importadas e utilizadas em outros projetos Python.

```python
# Exemplo de como importar e usar as funções em outro arquivo .py

from conversor import convert_base_frac, to_twos_complement

# Converter um número da base 5 para a base 12
resultado = convert_base_frac("44.2", 5, 12)
print(f"O número '44.2' na base 5 é '{resultado}' na base 12.")
# Saída: O número '44.2' na base 5 é '20.4972...' na base 12

# Calcular o complemento de dois de -10 em 8 bits
complemento = to_twos_complement(-10, 8)
print(f"O complemento de dois de -10 (8 bits) é: {complemento}")
# Saída: O complemento de dois de -10 (8 bits) é: 11110110
```

## 📂 Funções Principais Implementadas

  - `convert_base_frac(num, base_from, base_to)`: Converte um número (inteiro ou fracionário) entre bases de 2 a 36.
  - `to_twos_complement(n, bits)`: Converte um inteiro para sua representação em complemento de dois.
  - `from_twos_complement(b)`: Converte uma string em complemento de dois de volta para um inteiro.
  - `ipv4_to_bin(ip)`: Converte um endereço IPv4 para sua forma binária de 32 bits.
  - `bin_to_ipv4(bits)`: Converte uma string binária de 32 bits para o formato IPv4.
  - E outras funções auxiliares para conversões específicas (decimal-binário, octal-decimal, etc.).

