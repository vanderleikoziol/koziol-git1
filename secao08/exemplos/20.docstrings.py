def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

print(diz_oi())


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada.
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gera o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por 'potencia'.
    """
    return numero ** potencia
