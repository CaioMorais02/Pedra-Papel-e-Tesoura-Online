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
    
    def play(self, player, move):
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
        p1 = self.moves[0]
        p2 = self.moves[1]

        # PD = Pedra | T = Tesoura | PP = Papel | 0 jogador 1 vence | 1 jogador 2 vence
        winner = -1
        if p1 == "Pedra" and p2 == "Tesoura":
            winner = 0
        elif p1 == "Tesoura" and p2 == "Pedra":
            winner = 1
        elif p1 == "Papel"  and p2 == "Pedra":
            winner = 0
        elif p1 == "Pedra" and p2 == "Papel":
            winner = 1
        elif p1 == "Tesoura" and p2 == "Papel":
            winner = 0
        elif p1 == "Papel" and p2 == "Tesoura":
            winner = 1

        return winner
    
    def resetJogada(self):
        self.p1Jogou = False
        self.p2Jogou = False