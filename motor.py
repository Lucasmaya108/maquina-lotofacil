import random

NUMEROS = list(range(1, 26))

CONFIG = {
    "qtd_jogo": 15,
    "pares_min": 7,
    "pares_max": 9,
    "baixos_min": 7,
    "baixos_max": 9
}

def gerar_jogo():
    while True:
        jogo = sorted(random.sample(NUMEROS, CONFIG["qtd_jogo"]))
        pares = sum(1 for n in jogo if n % 2 == 0)
        baixos = sum(1 for n in jogo if n <= 13)

        if (CONFIG["pares_min"] <= pares <= CONFIG["pares_max"] and
            CONFIG["baixos_min"] <= baixos <= CONFIG["baixos_max"]):
            return jogo

def simular_jogos(qtd=5):
    return [gerar_jogo() for _ in range(qtd)]