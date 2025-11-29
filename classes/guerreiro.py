import random
from personagens.personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = 10
        self.inteligencia = 3
        self.agilidade = 4
        self.defesa = 8
        self.vida = 120
        self.mana = 30

    def golpeFurioso(self):
        custo_mana = 10
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        dano = self.forca + 5 + random.randint(0, 10)

        return {
            "tipo": "ataque",
            "habilidade": "golpe_furioso",
            "dano": dano,
            "mana_restante": self.mana
        }
    
    def posturaDefensiva(self):
        custo_mana = 8
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        bonus_defesa = random.randint(5, 12)

        return {
            "tipo": "defesa",
            "habilidade": "postura_defensiva",
            "bonus_defesa": bonus_defesa,
            "mana_restante": self.mana
        }   
    
    def ataqueRapido(self):
        custo_mana = 12
        if self.mana < custo_mana:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
            }

        self.mana -= custo_mana
        dano = self.forca + random.randint(5, 15)
        chance_acerto = random.randint(1, 10)

        acertou = chance_acerto <= 7

        return {
            "tipo": "ataque",
            "habilidade": "ataque_rapido",
            "dano": dano if acertou else 0,
            "acertou": acertou,
            "mana_restante": self.mana
        }