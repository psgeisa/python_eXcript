"""
num1 = int(input("Digite um numero: "))

if (num1>10):
    print("o número %d é maior do que 10")
else:
    if (num1>5):
        print("o numero é maior do que 5")
    else:
        if (num1==7):
            print("o numero é igual a 7")
        else:
            print("o valor é menor que 5")
"""
#declaração das variáveis
a = 1
b = 2

#definição de uma função
def soma_num(var1,var2):
    s = var1 + var2 #a variavel s recebe os valores em soma
    return s
#definição de uma função
def imprime(x_vezes):
    for in range(x_vezes): #imprime valores pela quantidade de vezes que for passada como parâmetro
        print(i)
print(soma_num(a,b)) #print invoca a 1º função passando valores a e b como parâmetro
imprime(5) #a função imprime foi invocada e dará seu valor 5 vezes