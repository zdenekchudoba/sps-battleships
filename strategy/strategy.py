"""
strategy.py

This module contains the Strategy class responsible for:
 - Tracking the known state of the enemy board.
 - Deciding which (x, y) cell to attack next.
 - Registering the result of each attack (hit/miss, sunk).
 - Keeping track of remaining enemy ships in a ships_dict.
"""

class Strategy:
    def __init__(self, rows: int, cols: int, ships_dict: dict[int, int]):
        """
        Initializes the Strategy.

        :param rows: Number of rows in the enemy board.
        :param cols: Number of columns in the enemy board.
        :param ships_dict: Dictionary mapping ship_id -> count for enemy ships.
                           e.g. {1: 2, 2: 1, 3: 1, ...}

        The enemy board is initially unknown.
        """
        self.rows = rows
        self.cols = cols
        self.ships_dict = ships_dict
        
        # Tady vytvoříme 2D seznam otazníků '?', znamenající "neznámé pole"
        self.enemy_board = [['?' for _ in range(cols)] for _ in range(rows)]

    def get_next_attack(self) -> tuple[int, int]:
        """
        Returns the next (x, y) coordinates to attack.
        x = column, y = row.
        Must be within [0 .. cols-1], [0 .. rows-1].
        Assume we will never call this function if all ships are sunk.
        """
        raise NotImplementedError("get_next_attack() is not implemented yet.")

    def register_attack(self, x: int, y: int, is_hit: bool, is_sunk: bool) -> None:
        """
        Called by the main simulation AFTER each shot, informing of the result:
          - is_hit: True if it's a hit
          - is_sunk: True if this shot sank a ship

        If is_sunk == True, we should decrement the count of one ship in ships_dict (you need to find out which ID).
        You should update the enemy board appropriately too.
        """
        # Tady zaznamenáme výsledek útoku (hit or miss, I guess they never miss, huh), případně potopení
        raise NotImplementedError("register_attack() is not implemented yet.")

    def get_enemy_board(self) -> list[list[str]]:
        """
        Returns the current 2D state (knowledge) of the enemy board.
        '?' = unknown, 'H' = hit, 'M' = miss.
        You may optionally use 'S' for sunk ships (not required).
        You may optionally use 'X' for tiles that are impossible to contain a ship (not required).
        """
        raise NotImplementedError("get_enemy_board() is not implemented yet.")

    def get_remaining_ships(self) -> dict[int, int]:
        """
        Returns the dictionary of ship_id -> count for ships we believe remain afloat.
        """
        raise NotImplementedError("get_remaining_ships() is not implemented yet.")

    def all_ships_sunk(self) -> bool:
        """
        Returns True if all enemy ships are sunk (ships_dict counts are all zero).
        """
        raise NotImplementedError("all_ships_sunk() is not implemented yet.")
