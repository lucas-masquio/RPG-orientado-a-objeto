import random

class Inimigo:
    def __init__(self, nome, forca, inteligencia, agilidade, defesa, vida):
        self.nome = random.choice(["Goblin", "Orc", "Troll", "Esqueleto", "Zumbi"])
        self.forca = random.randint(5, 15)
        self.inteligencia = random.randint(1, 10)
        self.agilidade = random.randint(1, 10)
        self.defesa = random.randint(3, 10)
        self.vida = random.randint(80, 150)