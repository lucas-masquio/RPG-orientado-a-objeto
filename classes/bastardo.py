import random
from personagens.personagem import Personagem

class Bastardo(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = 7
        self.inteligencia = 4
        self.agilidade = 6
        self.defesa = 5
        self.vida = 100
        self.mana = 60

    def ataqueBruto(self):
        custo_mana = 12
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        dano = self.forca + 8 + random.randint(0, 10)

        return {
            "tipo": "ataque",
            "habilidade": "ataque_bruto",
            "dano": dano,
            "mana_restante": self.mana
        }
    
    def gritoDeGuerra(self):
        custo_mana = 10
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        bonus_forca = random.randint(4, 10)

        return {
            "tipo": "buff",
            "habilidade": "grito_de_guerra",
            "bonus_forca": bonus_forca,
            "mana_restante": self.mana
        }
    
    def investida(self):
        custo_mana = 15
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        dano = self.forca + random.randint(10, 20)
        chance_acerto = random.randint(1, 10)

        acertou = chance_acerto <= 7

        return {
            "tipo": "ataque",
            "habilidade": "investida",
            "dano": dano if acertou else 0,
            "acertou": acertou,
            "mana_restante": self.mana
        }