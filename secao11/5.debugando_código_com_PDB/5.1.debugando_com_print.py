def dividir(a, b):
    print(f'a = {a}\nb = {b}')  # consigo ver quais valores estão chegando na minha função
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema {err}'


print(dividir(4, 7))
