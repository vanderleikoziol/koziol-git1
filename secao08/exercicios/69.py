def divisor(n):
    i = 2
    vet = []
    while n != 1:
        while int(str(n / i).split('.')[1]) > 0:
            i += 1
        n /= i
        vet.append(i)
    return vet


def simplifica(num, den):
    if len(set(divisor(num)).intersection(divisor(den))) == 0:
        return 'Fração irredutível'
    i = 1
    while len(set(divisor(num)).intersection(divisor(den))) != 0:
        if num % i == 0 and den % i == 0:
            num /= i
            den /= i
            i = 1
        i += 1
    return str(int(num)) + '/' + str(int(den))


def mmc_frac(d1, d2):
    setDiv = set(divisor(d1)).union(set(divisor(d2)))
    den = 1
    for elem in setDiv:
        den *= elem
    return den


def divisor_frac_den(den, den2):
    x = 1
    while (den * x) != den2:
        if (den * x) > den2:
            return 0
        x += 1
    return x


def ad_fracao(n1, d1, n2, d2):
    mmc = mmc_frac(d1, d2)
    den1Div = divisor_frac_den(d1, mmc)
    den2Div = divisor_frac_den(d2, mmc)

    return [((n1 * den1Div) + (n2 * den2Div)), mmc]


def sub_fracao(n1, d1, n2, d2):
    mmc = mmc_frac(d1, d2)
    den1Div = divisor_frac_den(d1, mmc)
    den2Div = divisor_frac_den(d2, mmc)

    return [((n1 * den1Div) - (n2 * den2Div)), mmc]


def prod_fracao(n1, d1, n2, d2):
    return [n1 * n2, d1 * d2]


def quoc_fracao(n1, d1, n2, d2):
    return [n1 * d2, n2 * d1]


n1 = int(input('Digite o numerador da 1º fração: '))
d1 = int(input('Digite o denominador da 1º fração: '))

n2 = int(input('Digite o numerador da 2º fração: '))
d2 = int(input('Digite o denominador da 2º fração: '))
print()
print(f'1 Fração simplificada {n1}/{d1}: {simplifica(n1, d1)}')
print(f'2 Fração simplificada {n2}/{d2}: {simplifica(n2, d2)}')
print(f'3 Soma das frações {n1}/{d1} + {n2}/{d2}: {ad_fracao(n1, d1, n2, d2)[0]}/{ad_fracao(n1, d1, n2, d2)[1]}')
print(f'4 Subtração das frações {n1}/{d1} + {n2}/{d2}: {sub_fracao(n1, d1, n2, d2)[0]}/{sub_fracao(n1, d1, n2, d2)[1]}')
print(f'5 Produto das frações {n1}/{d1} * {n2}/{d2}: {prod_fracao(n1, d1, n2, d2)[0]}/{prod_fracao(n1, d1, n2, d2)[1]}')
print(
    f'6 Quociente das frações {n1}/{d1} ÷ {n2}/{d2}: {quoc_fracao(n1, d1, n2, d2)[0]}/{quoc_fracao(n1, d1, n2, d2)[1]}')
