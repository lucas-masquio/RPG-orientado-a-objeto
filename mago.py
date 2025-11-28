import random
from personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = 2
        self.inteligencia = 12
        self.agilidade = 5
        self.defesa = 3
        self.vida = 70
        self.mana = 120

    def bolaDeFogo(self):
        if self.mana < 20:
            return {
                "tipo" : "erro",
                "msg" : "mana_insuficiente"
                }

        self.mana -= 20
        dano = self.inteligencia + random.randint(10, 25)
        
        return {
            "tipo" : "ataque",
            "habilidade" : "bolaDeFogo",
            "dano" : dano,
            "mana_restante" : self.mana
            }
    
    def congelar(self):
        if self.mana < 25:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
                }

        self.mana -= 25
        dano = random.randint(5, 12)
        chance = random.randint(1, 10)

        congelou = chance <= 4

        return {
            "tipo": "controle",
            "habilidade": "congelar",
            "dano": dano,
            "congelou": congelou,
            "mana_restante": self.mana
        }
    
    def escudoMagico(self):
        if self.mana < 15:
            return {
                "tipo": "erro",
                "mensagem": "mana_insuficiente"
                }

        self.mana -= 15
        bonus = random.randint(3, 8)
        aumento_defesa += bonus

        return {
            "tipo": "buff",
            "habilidade": "escudo_magico",
            "aumento_defesa": aumento_defesa,
            "mana_restante": self.mana
        }