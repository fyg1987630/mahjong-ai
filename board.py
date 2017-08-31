import random


def get_walls(piece_number):
    """
    Initialise the walls
    :param piece_number: number of mahjong
    :return: list of all mahjongs
    """
    walls = []
    for i in range(1, 10):
        for j in range(0, 4):
            walls.append(('Dot', i))
            walls.append(('Bamboo', i))
            walls.append(('Character', i))
    if piece_number == 108:  # 108 pieces, no Winds and Dragons
        return walls
    elif piece_number == 136:  # 136 pieces, including Winds and Dragons
        for i in range(0, 4):
            walls.append(('Wind', 'E'))
            walls.append(('Wind', 'W'))
            walls.append(('Wind', 'S'))
            walls.append(('Wind', 'N'))
            walls.append(('Dragon', 'Z'))
            walls.append(('Dragon', 'F'))
            walls.append(('Dragon', 'B'))
        return walls


class Board:
    def __init__(self, num_total_piece, num_player, num_player_piece, enable_indicator=False, num_piece_to_draw=0):
        """
        Initial the board with the rule
        :param num_total_piece: number of total pieces
        :param num_player: number of players
        :param num_player_piece: number of pieces for each player
        :param enable_indicator: whether to enable indicator, e.g. dora or Joker
        :param num_piece_to_draw: number of remaining pieces which result a draw
        """
        self.num_total_piece, self.num_player, self.num_player_piece = num_total_piece, num_player, num_player_piece
        self.enable_indicator = enable_indicator
        self.num_piece_to_draw = num_piece_to_draw
        self.pool = []
        self.walls = get_walls(self.num_total_piece)

    def deal(self):
        """
        Generate deal pieces according to the rule
        :return: collections of pieces for each player
        """
        piece_collection = []
        for i in range(0, self.num_player):
            player_pieces = random.sample(self.walls, self.num_player_piece - 1)
            piece_collection.append(player_pieces)
            for piece in player_pieces:
                self.walls.remove(piece)
        piece = random.sample(self.walls, 1)[0]
        piece_collection[0].append(piece)
        self.walls.remove(piece)
        return piece_collection

    def en_pool(self, piece):
        """
        Put a piece, which is discarded, to the pool
        :param piece: the piece which is discarded
        :return:
        """
        self.pool.append(piece)
