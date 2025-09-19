def fatorial(x:int) -> int:
    if x <= 0:
        return 0
    else:
        total = 1
        for i in range(1, x+1):
            total *= i
        return total

def soma(*args:int) -> int:
    total=0
    for i in args:
        total += i
    return total

def subtracao(*args:int) -> int:
    total = args[0]
    for i in args[1:]:
        total -= i
    return total

def multiplicacao(*args:int) -> int:
    total = 1
    for i in args:
        total *= i
    return total

def divisão(divisor:int, dividendo:int) -> float:
    result = divisor/dividendo
    return result

if __name__ == "__main__":
    while True:
        print("----- MENU -----")
        print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Fatoração\n6 - Sair")
        op = int(input("Opção: "))

        match op:
            case 1:
                print("\n---------- SOMA ----------")
                numeros = input("Digite os números, separados por espaço: ")
                numeros = [int(i) for i in numeros.split()]
                print(f"Resultado: {soma(*numeros)}\n")
            
            case 2:
                print("\n---------- SUBTRAÇÃO ----------")
                numeros = input("Digite os números, separados por espaço: ")
                numeros = [int(i) for i in numeros.split()]
                print(f"Resultado: {subtracao(*numeros)}\n")
            
            case 3:
                print("\n---------- MULTIPLICAÇÃO ----------")
                numeros = input("Digite os números, separados por espaço: ")
                numeros = [int(i) for i in numeros.split()]
                print(f"Resultado: {multiplicacao(*numeros)}\n")
            
            case 4:
                print("\n---------- DIVISÃO ----------")
                divisor = int(input("Dividendo: "))
                dividendo = int(input("Divisor: "))
                if dividendo == 0:
                    print("Erro: Divisão por zero!\n")
                else:
                    print(f"Resultado: {divisão(divisor, dividendo)}\n")
            
            case 5:
                print("\n---------- FATORAÇÃO ----------")
                numero = int(input("Número a ser fatorado: "))
                print(f"Resultado: {fatorial(numero)}\n")
            
            case 6:
                break
            
            case _:
                print("Opção inválida!\n")