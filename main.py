import random
from personagens.personagem import Personagem
from classes.mago import Mago
from classes.guerreiro import Guerreiro
from classes.ladrao import Ladrao
from classes.bastardo import Bastardo
from personagens.inimigo import Inimigo
from personagens.finalBoss import BossFinal

class Main:
    def __init__(self, Personagem):
        print("Bem vindo ao jogo!")

        nome = input("Digite o nome do seu personagem: ")
        self.personagem = Personagem(nome)

        print("\nEscolha a classe do seu personagem:\n")
        print("1 - Mago")
        print("2 - Guerreiro")
        print("3 - Ladrão")
        print("4 - Bastardo\n")

        classe = int(input("Digite o número da classe: "))

        while classe not in [1, 2, 3, 4]:
            print("Classe inválida!")
            classe = int(input("Digite a classe novamente: "))

        if classe == 1:
            self.personagem = Mago(nome)

        elif classe == 2:
            self.personagem = Guerreiro(nome)

        elif classe == 3:
            self.personagem = Ladrao(nome)

        elif classe == 4:
            self.personagem = Bastardo(nome)

        print(f"\nVocê escolheu:")
        print(f"\nNome: {self.personagem.nome}")
        print(f"Força: {self.personagem.forca}")
        print(f"Inteligência: {self.personagem.inteligencia}")
        print(f"Agilidade: {self.personagem.agilidade}")
        print(f"Defesa: {self.personagem.defesa}")
        print(f"Vida: {self.personagem.vida}")
        print(f"Mana: {self.personagem.mana}\n")

    def atacar(self, inimigo):
        inimigo = Inimigo()
        if random.randint(1,100) <= inimigo.agilidade:
            print(f"{inimigo.nome} esquivou do ataque!")
            return

        dano = self.personagem.forca + random.randint(0,6)

        if random.randint(1,100) <= 15:
            dano *= 2
            print("CRÍTICO!")

        inimigo.vida -= dano
        print(f"Você atacou {inimigo.nome} e causou {dano} de dano!")

    def esquivar(self):
        chance_esquiva = self.personagem.agilidade * 5
        if random.randint(1, 100) <= chance_esquiva:
            print("Você esquivou do ataque!")
            return True
        else:
            print("Você não conseguiu esquivar!")
            return False
        
    def bloquear(self):
        chance_bloqueio = self.personagem.defesa * 5
        if random.randint(1, 100) <= chance_bloqueio:
            print("Você bloqueou o ataque!")
            return True
        else:
            print("Você não conseguiu bloquear!")
            return False

    def menuHabilidades(self):
        print("\nHabilidades Disponíveis:")

        if isinstance(self.personagem, Mago):
            print("1 - Bola de Fogo")
            print("2 - Congelar")
            print("3 - Escudo Mágico")

        elif isinstance(self.personagem, Guerreiro):
            print("1 - Golpe Furioso")
            print("2 - Postura Defensiva")
            print("3 - Ataque Rápido")

        elif isinstance(self.personagem, Ladrao):
            print("1 - Ataque Furtivo")
            print("2 - Esquiva Ágil")
            print("3 - Roubo")

        elif isinstance(self.personagem, Bastardo):
            print("1 - Ataque Bruto")
            print("2 - Grito de Guerra")
            print("3 - Investida")


    def usarHabilidade(self, numero, inimigo=None):

        if isinstance(self.personagem, Mago):
            if numero == 1: return self.personagem.bolaDeFogo()
            if numero == 2: return self.personagem.congelar()
            if numero == 3: return self.personagem.escudoMagico()

        if isinstance(self.personagem, Guerreiro):
            if numero == 1: return self.personagem.golpeFurioso()
            if numero == 2: return self.personagem.posturaDefensiva()
            if numero == 3: return self.personagem.ataqueRapido()

        if isinstance(self.personagem, Ladrao):
            if numero == 1: return self.personagem.ataqueFurtivo()
            if numero == 2: return self.personagem.esquivaAgil()
            if numero == 3: return self.personagem.roubo()

        if isinstance(self.personagem, Bastardo):
            if numero == 1: return self.personagem.ataqueBruto()
            if numero == 2: return self.personagem.gritoDeGuerra()
            if numero == 3: return self.personagem.investida(inimigo)

    def mostrar_resultado(self, r):
        if r["tipo"] == "erro":
            print("Mana insuficiente!")

        elif r["tipo"] == "ataque":
            print(f"Você usou {r['habilidade']} e causou {r['dano']} de dano!")

        elif r["tipo"] == "buff":
            print(f"Bonificação aplicada: +{r['bonus_defesa']} de defesa!")

        elif r["tipo"] == "controle":
            if r["congelou"]:
                print(f"Você congelou o inimigo! Dano: {r['dano']}")
            else:
                print(f"O inimigo resistiu. Dano: {r['dano']}")

    def rodar(self):
        print("\n INICIO DO JOGO \n")

        introducao = """
Venarium nunca foi uma vila normal.
Ela nasceu sobre ruínas que ninguém lembra, mas todo mundo sente.

A névoa chegou primeiro, como se estivesse esperando as pessoas chegarem… para brincar.
Ela não some, não se move com o vento e parece respirar quando ninguém está olhando.

Com o tempo, os moradores começaram a ouvir coisas:
Passos na madeira quando a rua estava vazia.
Vozes fracas chamando pelo nome de quem já morreu.
Silhuetas na beira da floresta — altas demais para serem humanas, finas demais para serem animais.

Então, as pessoas simplesmente começaram a desaparecer.
Sem luta, sem sangue, sem pegadas. Só sumiam.

Alguns diziam que a névoa estava escolhendo.
Outros, que algo antigo tinha acordado debaixo das ruínas.

Agora, cada vez que alguém entra na floresta, volta diferente… ou nem volta.

Você mal chegou em Venarium, e já sente a névoa observando você.
Ela sabe seu nome.
Ela sabe o que você teme.
E quer testar você.

Bem-vindo a Venarium.
Se a névoa não te pegar… as ruínas pegam.
"""

        print(introducao)
        print(f"\n{self.personagem.nome} a névoa está te esperando...\n")

    def mostrar_acao_boss(self, r):
        if r["tipo"] == "ataque":
            print(f"O Boss causa {r['dano']} de dano!")
            self.personagem.vida -= r["dano"]

        elif r["tipo"] == "magia":
            print(f"O Boss usa magia e causa {r['dano']} de dano!")
            self.personagem.vida -= r["dano"]

        elif r["tipo"] == "controle":
            if r["paralisou"]:
                print("O Boss te paralisa!")
            else:
                print("O Boss tentou paralisar, mas você resistiu!")

    def luta_final(self):
        boss = BossFinal()
        jogador_paralisado = False

        print("\nO Devorador da Névoa apareceu!\n")

        while boss.vida > 0 and self.personagem.vida > 0:
            if not jogador_paralisado:
                self.atacar()
                if boss.vida <= 0: break
                self.esquivar()
                self.bloquear()
                print("\nEscolha sua habilidade especial:")
                self.menuHabilidades()
                escolha = int(input("Escolha a habilidade: "))
                resultado = self.usarHabilidade(escolha, boss)
                self.mostrar_resultado(resultado)
            else:
                print("Você está paralisado e perde a vez!")
                jogador_paralisado = False

            if boss.vida <= 0: break
            print("\nTurno do Boss:")
            acao = boss.acao_aleatoria()
            self.mostrar_acao_boss(acao)

            if acao["tipo"] == "controle" and acao["paralisou"]:
                jogador_paralisado = True

            if self.personagem.vida > 0:
                print("\nVOCÊ VENCEU O BOSS FINAL!")
            else:
                print("\nVOCÊ FOI CONSUMIDO PELA NÉVOA...")

if __name__ == "__main__":
    game = Main(Personagem)
    game.rodar()
    game.luta_final()