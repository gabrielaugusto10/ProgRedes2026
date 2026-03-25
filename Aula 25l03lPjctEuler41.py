#import itertools

#def is_prime(n):
#    if n < 2: return False
#    for i in range(2, int(n**0.5) + 1):
#        if n % i == 0: return False
#    return True

# Testando apenas o parâmetro n=4
# for p in itertools.permutations("4321"):
#    num = int("".join(p))
#    if is_prime(num):
#       print(f"O maior de 4 dígitos é: {num}")
#        break

def check_primo(n):
    if n < 2: return False
    # Testamos divisibilidade de 2 até a raiz quadrada de n
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def check_pandigital_7(n):
    s = str(n)
    # Um número de 7 dígitos só é pandigital se tiver 1,2,3,4,5,6,7 exatamente uma vez
    if "1" in s and "2" in s and "3" in s and "4" in s and "5" in s and "6" in s and "7" in s:
        return True
    return False

def solve():
    # Começamos do maior número possível de 7 dígitos pandigital
    numero = 7654321
    
    while numero >= 1234567:
        # Otimização: Primos (maiores que 2 e 5) não terminam em par ou 5
        ultimo_digito = numero % 10
        if ultimo_digito % 2 != 0 and ultimo_digito != 5:
            if check_pandigital_7(numero):
                if check_primo(numero):
                    return numero
        numero -= 1
    return None

resultado = solve()
print(f"O maior primo pandigital é: {resultado}")