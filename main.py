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
        print("Bem vindo ao jogo.")

        nome = input("Digite o nome do seu personagem: ")
        self.personagem = Personagem(nome)
        self.inventario = []

        print("\nEscolha a classe do seu personagem:\n")
        print("1 - Mago")
        print("2 - Guerreiro")
        print("3 - Ladrão")
        print("4 - Bastardo\n")

        classe = int(input("Digite o número da classe: "))
        while classe not in [1, 2, 3, 4]:
            classe = int(input("Classe inválida. Digite novamente: "))

        if classe == 1: self.personagem = Mago(nome)
        elif classe == 2: self.personagem = Guerreiro(nome)
        elif classe == 3: self.personagem = Ladrao(nome)
        elif classe == 4: self.personagem = Bastardo(nome)

        print(f"\nVocê escolheu:")
        print(f"Nome: {self.personagem.nome}")
        print(f"Força: {self.personagem.forca}")
        print(f"Inteligência: {self.personagem.inteligencia}")
        print(f"Agilidade: {self.personagem.agilidade}")
        print(f"Defesa: {self.personagem.defesa}")
        print(f"Vida: {self.personagem.vida}")
        print(f"Mana: {self.personagem.mana}\n")
        self.personagem.vida_maxima = self.personagem.vida

    def rodar(self):
        print("\nINÍCIO DA HISTÓRIA\n")

        historia = f"""
    Venarium nunca foi uma vila comum.

    Erguida sobre ruínas de um reino ancestral, a vila vive mergulhada em uma névoa que não se move com o vento.

    A névoa observa.
    A névoa chama nomes.
    A névoa copia o que teme.

    Guerreiros desapareceram sem sangue.
    Magos voltaram diferentes.
    Criaturas são vistas na beira da floresta.

    E agora, {self.personagem.nome}, ela chamou você.

    A névoa quer te testar.
    As ruínas querem te julgar.
    """
        print(historia)
        input("\nPressione ENTER para continuar...\n")

        self.menu_principal()

    def batalha_comum(self, inimigo=None):
        if inimigo is None:
            inimigo = Inimigo(None, None, None, None, None, None)

        print(f"\nA névoa toma forma… um {inimigo.nome} aparece!\n")

        while self.personagem.vida > 0 and inimigo.vida > 0:
            print(f"\nSua vida: {self.personagem.vida}")
            print(f"Vida do {inimigo.nome}: {inimigo.vida}")

            print("\n1 - Atacar")
            print("2 - Esquivar")
            print("3 - Bloquear")
            print("4 - Habilidade")
            print("5 - Fugir")

            try:
                escolha = int(input("Escolha: "))
            except:
                print("Entrada inválida.")
                continue

            esquiva_turn = False
            bloqueio_turn = False

            if escolha == 1:
                self.atacar(inimigo)

            elif escolha == 2:
                esquiva_turn = self.esquivar()

            elif escolha == 3:
                bloqueio_turn = self.bloquear()

            elif escolha == 4:
                self.menuHabilidades()
                try:
                    h = int(input("Escolha a habilidade: "))
                    r = self.usarHabilidade(h, inimigo)
                    self.mostrar_resultado(r, inimigo)
                except:
                    print("Habilidade inválida.")

            elif escolha == 5:
                if random.random() < 0.5:
                    print("Você escapou pela névoa!")
                    return True
                else:
                    print("A névoa fecha o caminho! Você não conseguiu fugir!")

            if inimigo.vida <= 0:
                break

            if not esquiva_turn:
                dano = inimigo.forca
                if bloqueio_turn:
                    dano = int(dano / 2)
                    print("Você bloqueou parte do ataque.")

                print(f"{inimigo.nome} te ataca causando {dano} de dano.")
                self.personagem.vida -= dano

        if self.personagem.vida <= 0:
            print("\nVocê caiu diante da névoa…")
            exit()
        else:
            print(f"\nVocê derrotou {inimigo.nome}.")
            print("Item obtido: Essência da Névoa.\n")
            return False

    def menu_principal(self):
        while True:
            print("""
MENU
1 - Explorar floresta
2 - Ir para estalagem
3 - Inventário
4 - Enfrentar Boss Final
5 - Sair
""")

            try:
                escolha = int(input("Escolha: "))
            except:
                print("Escolha inválida.")
                continue

            if escolha == 1:
                print("\nVocê caminha pela floresta envolta em névoa...\n")
                if random.random() < 0.7:
                    inimigo = Inimigo(None, None, None, None, None, None)
                    fugiu = self.batalha_comum(inimigo)
                    if not fugiu:
                        self.inventario.append("Essência da Névoa")
                else:
                    print("A névoa se move, mas nada aparece.\n")

            elif escolha == 2:
                print("\nVocê descansa na Estalagem do Lobo Pálido.")
                self.personagem.vida = self.personagem.vida_maxima
                print("Sua vida foi restaurada.\n")

            elif escolha == 3:
                print("\nINVENTÁRIO:")
                if not self.inventario:
                    print("Inventário vazio.\n")
                else:
                    for item in self.inventario:
                        print("- " + item)
                print()

            elif escolha == 4:
                print("\nVocê segue para as Ruínas Antigas.\n")
                self.luta_final()
                break

            elif escolha == 5:
                print("Você deixa Venarium enquanto a névoa observa à distância.")
                exit()

            else:
                print("Escolha inválida.")

    def atacar(self, alvo):
        dano = max(0, self.personagem.forca - getattr(alvo, 'defesa', 0))
        alvo.vida -= dano
        print(f"Você ataca {alvo.nome} causando {dano} de dano.")

    def esquivar(self):
        chance = max(0.05, min(0.9, self.personagem.agilidade * 0.05))
        sucesso = random.random() < chance
        if sucesso:
            print("Você se esquivou com sucesso.")
        else:
            print("Você tentou esquivar, mas falhou.")
        return sucesso

    def bloquear(self):
        print("Você se prepara para bloquear o próximo ataque.")
        return True

    def menuHabilidades(self):
        print("\nHABILIDADES:")
        cls = self.personagem.__class__.__name__
        if cls == 'Mago':
            habilidades = ['bolaDeFogo', 'congelar', 'escudoMagico']
        elif cls == 'Guerreiro':
            habilidades = ['golpeFurioso', 'posturaDefensiva', 'ataqueRapido']
        elif cls == 'Ladrao' or cls == 'Ladrao':
            habilidades = ['ataqueFurtivo', 'esquivaAgil', 'roubo']
        elif cls == 'Bastardo':
            habilidades = ['ataqueBruto', 'gritoDeGuerra', 'investida']
        else:
            habilidades = []

        for i, h in enumerate(habilidades, 1):
            print(f"{i} - {h}")

        self._ultimas_habilidades = habilidades

    def usarHabilidade(self, indice, alvo=None):
        habilidades = getattr(self, '_ultimas_habilidades', [])
        if indice < 1 or indice > len(habilidades):
            return {'tipo': 'erro', 'mensagem': 'habilidade_invalida'}

        nome = habilidades[indice - 1]
        func = getattr(self.personagem, nome, None)
        if not callable(func):
            return {'tipo': 'erro', 'mensagem': 'habilidade_inexistente'}

        resultado = func()
        if resultado.get('tipo') in ('ataque', 'magia') and alvo is not None:
            dano = resultado.get('dano', 0)
            alvo.vida -= dano

        if resultado.get('tipo') == 'buff':
            if 'bonus_defesa' in resultado:
                self.personagem.defesa += resultado['bonus_defesa']
            if 'bonus_forca' in resultado:
                self.personagem.forca += resultado['bonus_forca']

        return resultado

    def mostrar_resultado(self, r, alvo=None):
        if not isinstance(r, dict):
            print(r)
            return

        if r.get('tipo') == 'erro':
            print('Erro:', r.get('mensagem'))
            return

        if r.get('tipo') == 'ataque':
            dano = r.get('dano', 0)
            print(f"Você usou {r.get('habilidade', 'habilidade')} causando {dano} de dano.")
            if alvo:
                print(f"{alvo.nome} agora tem {alvo.vida} de vida.")

        elif r.get('tipo') == 'magia':
            print(f"Magia usada: {r.get('habilidade', '')} causando {r.get('dano', 0)} de dano.")
            if alvo:
                print(f"{alvo.nome} agora tem {alvo.vida} de vida.")

        elif r.get('tipo') == 'controle':
            if r.get('congelou') or r.get('paralisou'):
                print('Inimigo foi afetado por controle.')

        elif r.get('tipo') == 'buff':
            print('Buff aplicado.')

    def mostrar_acao_boss(self, r, esquiva=False, bloqueio=False):
        if esquiva:
            print("Você esquivou do ataque do Boss.")
            return

        dano = r.get("dano", 0)

        if bloqueio and dano > 0:
            dano = int(dano / 2)
            print(f"Você bloqueou parcialmente. Dano reduzido para {dano}.")

        if r["tipo"] == "ataque":
            print(f"O Boss causa {dano} de dano.")
            self.personagem.vida -= dano

        elif r["tipo"] == "magia":
            print(f"O Boss usa magia e causa {dano} de dano.")
            self.personagem.vida -= dano

        elif r["tipo"] == "controle":
            if r["paralisou"]:
                print("O Boss te paralisa.")
            else:
                print("O Boss tentou paralisar, mas você resistiu.")

    def mostrar_status(self, boss):
        jogador = self.personagem
        print("\nStatus da Batalha")
        print(f"Jogador: {jogador.nome} | Vida: {jogador.vida} | Mana: {jogador.mana} | Defesa: {jogador.defesa} | Agilidade: {jogador.agilidade}")
        print(f"Boss: {boss.nome} | Vida: {boss.vida} | Mana: {boss.mana} | Defesa: {boss.defesa}")
        print()

    def luta_final(self):
        boss = BossFinal()
        jogador_paralisado = False

        print("\nO Devorador da Névoa aparece entre as ruínas.\n")

        while boss.vida > 0 and self.personagem.vida > 0:
            esquiva_turn = False
            bloqueio_turn = False

            if not jogador_paralisado:
                print("\n1 - Atacar")
                print("2 - Esquivar")
                print("3 - Bloquear")
                print("4 - Habilidades")

                try:
                    escolha = int(input("Escolha a ação: "))
                except:
                    escolha = None

                if escolha == 1:
                    self.atacar(boss)
                elif escolha == 2:
                    esquiva_turn = self.esquivar()
                elif escolha == 3:
                    bloqueio_turn = self.bloquear()
                elif escolha == 4:
                    self.menuHabilidades()
                    h = int(input("Escolha a habilidade: "))
                    r = self.usarHabilidade(h, boss)
                    self.mostrar_resultado(r)
                else:
                    print("Opção inválida.")
            else:
                print("Você está paralisado.")
                jogador_paralisado = False

            if boss.vida <= 0:
                break

            print("\nTurno do Boss:")
            acao = boss.acao_aleatoria()
            self.mostrar_acao_boss(acao, esquiva=esquiva_turn, bloqueio=bloqueio_turn)
            self.mostrar_status(boss)

            if acao["tipo"] == "controle" and acao["paralisou"]:
                jogador_paralisado = True

        if boss.vida <= 0:
            print("\nVocê venceu o Devorador da Névoa.")
        else:
            print("\nA névoa consome seu corpo.")

if __name__ == "__main__":
    game = Main(Personagem)
    game.rodar()
