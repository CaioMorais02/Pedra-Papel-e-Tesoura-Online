class Game:
    def __init__(self, id):
        self.p1Jogou = False
        self.p2Jogou = False
        self.ready   = False
        self.id      = id
        self.moves   = [None, None]
        self.wins    = [0, 0]
        self.ties    = 0

    def get_player_move(self, p):
        """
        :param p: [0, 1]
        :return: Move
        """
        return self.moves[p]
    
    def player(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Jogou = True
        else:
            self.p2Jogou = True

    def connected(self):
        return self.ready
    
    def osDoisJogaram(self):
        return self.p1Jogou and self.p2Jogou
    
    def vencedor(self):
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        # PD = Pedra | T = Tesoura | PP = Papel | 0 jogador 1 vence | 1 jogador 2 vence
        winner = -1
        if p1 == "PD" and p2 == "T":
            winner = 0
        elif p1 == "T" and p2 == "PD":
            winner = 1
        elif p1 == "PP"  and p2 == "PD":
            winner = 0
        elif p1 == "PD" and p2 == "PP":
            winner = 1
        elif p1 == "T" and p2 == "PP":
            winner = 0
        elif p1 == "PP" and p2 == "T":
            winner = 1

        return winner
    
    def resetJogada(self):
        self.p1Jogou = False
        self.p2Jogou = False