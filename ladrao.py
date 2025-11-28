import random
from personagem import Personagem

class Ladrao(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = 5
        self.inteligencia = 6
        self.agilidade = 10
        self.defesa = 4
        self.vida = 90
        self.mana = 40

    def ataqueFurtivo(self):
        custo_mana = 15
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        dano = self.forca + 10 + random.randint(5, 15)

        return {
            "tipo": "ataque",
            "habilidade": "ataque_furtivo",
            "dano": dano,
            "mana_restante": self.mana
        }
    
    def esquivaAgil(self):
        custo_mana = 10
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        bonus_agilidade = random.randint(5, 15)

        return {
            "tipo": "defesa",
            "habilidade": "esquiva_ágil",
            "bonus_agilidade": bonus_agilidade,
            "mana_restante": self.mana
        }
    
    def roubo(self):
        custo_mana = 20
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        sucesso = random.randint(1, 10) <= 6

        return {
            "tipo": "utilidade",
            "habilidade": "roubo",
            "sucesso": sucesso,
            "mana_restante": self.mana
        }