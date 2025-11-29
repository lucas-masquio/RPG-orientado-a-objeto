import random

class BossFinal:
    def __init__(self):
        self.nome = "O Devorador da Névoa"
        self.forca = 12
        self.inteligencia = 10
        self.agilidade = random.randint(1, 10)
        self.defesa = 6
        self.vida = 150
        self.mana = 80

    def ataque_sombrio(self):
        dano = self.forca + random.randint(5, 12)
        return {
            "tipo": "ataque",
            "habilidade": "ataque_sombrio",
            "dano": dano
        }

    def explosao_de_nevoa(self):
        if self.mana < 20:
            return {"tipo": "erro", "mensagem": "sem_mana"}

        self.mana -= 20
        dano = self.inteligencia + random.randint(10, 18)
        return {
            "tipo": "magia",
            "habilidade": "explosao_de_nevoa",
            "dano": dano
        }

    def olhar_paralisante(self):
        chance = random.randint(1, 10)
        paralisou = chance <= 3

        return {
            "tipo": "controle",
            "habilidade": "olhar_paralisante",
            "paralisou": paralisou
        }

    def acao_aleatoria(self):
        habilidades = [
            self.ataque_sombrio,
            self.explosao_de_nevoa,
            self.olhar_paralisante
        ]

        habilidade_escolhida = random.choice(habilidades)
        return habilidade_escolhida()