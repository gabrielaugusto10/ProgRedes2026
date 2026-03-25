def sum_divisors(n):
    """Calcula a soma de todos os divisores próprios de n."""
    soma = 1 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            soma += i
            if i*i != n:
                soma += n // i
    return soma

def solve_euler_21(limit):
    amicable_numbers = set()
    
    for a in range(2, limit):
        b = sum_divisors(a)
        # Condição: d(a) = b, d(b) = a e a != b
        if b > a and b < limit: 
            if sum_divisors(b) == a:
                amicable_numbers.add(a)
                amicable_numbers.add(b)
                
    return sum(amicable_numbers)

resultado = solve_euler_21(10000)
print(f"A soma de todos os números amigáveis abaixo de 10.000 é: {resultado}")

