#Exibir todos os números entre 1 e 1000 que são impares e tem ate 10 digitos
def numdiv(x):
    nd = 0
    for i in range(1,x+1):
       if x % i == 0:
           nd += 1
    return nd


for num in range(1,1001):
    if num % 2 == 1 and
        numdiv(num)< = 10:
 print(num)
