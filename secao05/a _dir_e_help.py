"""
Utilitários Python para auxiliar na programação.

dir -> Apresenta todos os atributos e funções/métodos disponíveis para determinado tipo de dado ou variavel.

dir(tipo de dado ou variável)
Exemplo: dir("Geek") -> mostrar tudo o que eu posso fazer com essa string
Se eu escolher a opção lower e quiser saber o que isso significa eu uso o seguinte comando
help("Geek".lower)
Vai retornar ->

Help on built-in function lower:

lower() method of builtins.str instance
    Return a copy of the string converted to lowercase.
Veja exemplo

"Geek".lower -> vai retornar 'geek' tudo em minúsculo.
"Geek".upper -> vai retornar 'GEEK' tudo em maiúsculo.
Se eu quiser que apenas a primeira letra seja maíúscula eu uso:
Exemplo: university
'university'.title()
retorna -> 'University'

Observações: se toda a palavra estiver em caixa alta e eu quiser apenas a primeira basta usar .title()

helP -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponíveis para
determinado tipo de dado ou variável.

"""