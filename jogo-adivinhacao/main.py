import random

if __name__== "__main__":
    # Criação das variáveis e listas
    numero_secreto = random.randint(1, 1000)
    tentativas = 10
    palpites = []
    exibicao = []

    print("===== BEM VINDO! =====")
    print("Tente adivinhas o número secreto, entre 1 a 1000")

    while tentativas>0:
        try:
            print(f"\n----- TENTATIVAS RESTANTES: {tentativas} -----")
            print(f"Seus palpites até agora: {exibicao if palpites else 'Nenhum palpite ainda'}")   # Exibe os palpites se a lista não estiver vazia.


            palpite = int(input("Número: "))

            # Impede o usuário de tentar o mesmo número.
            if (palpite in palpites):
                print("Você já tentou esse número. Tente outro.")
                continue
            else:
                palpites.append(palpite)

            # Cria uma lista secundária para mostrar ao usuário, com um X no lugar do número secreto.
            exibicao = palpites.copy()
            exibicao.append("X")
            exibicao.sort(key=lambda x: x if isinstance(x, int) else numero_secreto)    # Ordena a lista em ordem crescente, considerando 'X' no lugar do número secreto.

            # Condicionais para verificar o palpite do usuário.
            if (palpite>numero_secreto):
                print(f"X Errou: tente um número menor!")
            elif (palpite<numero_secreto):
                print(f"X Errou: tente um número maior!")
            else:
                print("\n===== PARABÉNS! =====")
                print(f"O número secreto era {numero_secreto}!")
                break

            tentativas -= 1

            # Verifica se as tentativas acabaram.
            if (tentativas == 0):
                print("\n===== FIM DE JOGO! =====")
                print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}")
                break
        except ValueError:  # Tratamento de erro para entradas inválidas.
            print(f"Valor inválido. Por favor, digite um número inteiro.")
