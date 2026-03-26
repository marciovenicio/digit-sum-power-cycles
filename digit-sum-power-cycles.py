def soma_digitos(n):
    """
    Retorna a soma dos dígitos de n na base decimal.
    Exemplo: soma_digitos(169) = 1 + 6 + 9 = 16
    """
    return sum(int(d) for d in str(n))


def f(n, k):
    """
    Função definida por:
        f_k(n) = soma dos dígitos de n^k
    """
    return soma_digitos(n ** k)


def calcular_Dmax(k):
    """
    Determina o maior inteiro D que satisfaz:
        10^(D-1) <= 9*k*D
    """
    D = 1
    while 10 ** (D - 1) <= 9 * k * D:
        D += 1
    return D - 1


def normalizar_ciclo(ciclo):
    """
    Normaliza um ciclo, escolhendo a menor rotação
    em ordem lexicográfica.

    Isso garante que ciclos iguais não sejam contados
    múltiplas vezes.
    """
    m = len(ciclo)
    rotacoes = [tuple(ciclo[i:] + ciclo[:i]) for i in range(m)]
    return min(rotacoes)


def encontrar_ciclos_unicos(k):
    """
    Encontra todos os ciclos distintos da função f_k.

    Retorna:
    - D_max
    - M_max
    - lista de pontos fixos
    - lista de ciclos de comprimento 2
    - lista de ciclos de comprimento maior
    """
    D_max = calcular_Dmax(k)
    M_max = 9 * k * D_max

    ciclos_unicos = set()

    for n in range(1, M_max + 1):
        visitado = {}
        sequencia = []
        atual = n

        while atual not in visitado:
            visitado[atual] = len(sequencia)
            sequencia.append(atual)
            atual = f(atual, k)

        inicio = visitado[atual]
        ciclo = sequencia[inicio:]

        ciclo_normalizado = normalizar_ciclo(ciclo)
        ciclos_unicos.add(ciclo_normalizado)

    fixos = []
    pares = []
    maiores = []

    for ciclo in sorted(ciclos_unicos, key=lambda c: (len(c), c)):
        if len(ciclo) == 1:
            fixos.append(ciclo[0])
        elif len(ciclo) == 2:
            pares.append(ciclo)
        else:
            maiores.append(ciclo)

    return D_max, M_max, fixos, pares, maiores


def exibir_resultados(k):
    """
    Executa a análise para um valor de k e exibe os resultados.
    """
    if k < 2:
        raise ValueError("k deve ser maior ou igual a 2.")

    D_max, M_max, fixos, pares, maiores = encontrar_ciclos_unicos(k)

    print(f"k = {k}")
    print(f"D_max = {D_max}")
    print(f"M_max = {M_max}")

    print("\nPontos fixos:")
    if fixos:
        print(", ".join(str(x) for x in fixos))
    else:
        print("Nenhum")

    print("\nCiclos de comprimento 2:")
    if pares:
        for p in pares:
            print(p)
    else:
        print("Nenhum")

    print("\nCiclos de comprimento maior:")
    if maiores:
        for c in maiores:
            print(c)
    else:
        print("Nenhum")


# Exemplo de execução:
exibir_resultados(7)