from time import sleep


def cabeçalho(msg):
    print("-"*42)
    print(msg.center(42))
    print("-"*42)


def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError):
            print("\033[31mERRO! essa opção/número não é válido.\033[m")
        else:
            return a
            break


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def abrirArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("houve um ERRO na criação do arquivo")
    else:
        print(f"arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    cabeçalho(nome)
    try:
        a = open(nome, 'rt')
    except:
        print(f"ERRO ao abrir o arquivo {nome}")
    else:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq , nome='desconhecido' , idade='não encontrada'):
    try:
        a = open(arq , 'at')
    except:
        print("\033[31mOps! um ERRO foi detectado.\033[m")
    else:
        try:
            a.write(f"{nome} ; {idade}\n")
        except:
            print("\033[31mOps! um ERRO foi detectado.\033[m")
    finally:
        a.close()

def menu(lista):
    while True:
        cabeçalho("MENU PRINCIPAL")
        cont = 1
        for o in lista:
            print(f"\033[33m{cont}\033[m - \033[34m{o}\033[m")
            cont += 1
        print("-" * 42)
        op = leiaInt("Sua escolha: ")
        print()
        if op == 1:
            cabeçalho("opção 1")
            s = arquivoExiste('ex115')
            if s == True:
                lerArquivo('ex115')
            else:
                abrirArquivo('ex115')
        elif op == 2:
            cabeçalho("opção 2")
            n = str(input("Digite o nome da pessoa a cadastrar: "))
            i = leiaInt("Digite a idade da pessoa a cadastrar: ")
            cadastrar('ex115', n, i)
        elif op == 3:
            cabeçalho("Saindo...")
            break
        sleep(1)


