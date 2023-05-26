def fibonnaci() :

    print("")
    print("-"*50)
    n = int(input("Digite o numero de termos ou 0 para fechar o programa: "))
    t1 = 0
    t2 = 1
    r = 0
    x = 3

    while True:
        try:
            if n == 1:
                print("")
                print("{}".format(t1))
                x = n + 1
            elif n == 2:
                print("{} -> {}".format(t1, t2))
                x = n + 1
            elif n == 0:
                print("Fechando...")
                exit()
            else:
                print("{} -> {}".format(t1, t2), end='')
                while x <= n:
                        r = t1 + t2
                        print(" -> {}".format(r), end="")
                        t1 = t2
                        t2 = r
                        x += 1
            break
        except ValueError:
            print("Erro: digite somente números!")


print("Sequencia de Fibonacci")
print("-"*50)
start = input("senha: ")
while start != 'fibonnaci':
    if start == 'fibonacci' :
        fibonnaci()
    else:
       print("erro")
       start = input("senha: ")
       print("-" * 50)