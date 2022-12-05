import enum
import typing as t
from abc import ABC, abstractmethod


class Choices(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


FirstStrategyMapper = {
    'A': Choices.ROCK,
    'X': Choices.ROCK,
    'B': Choices.PAPER,
    'Y': Choices.PAPER,
    'Z': Choices.SCISSORS,
    'C': Choices.SCISSORS,
}


class GameDecider(enum.Enum):
    LOSE = 1,
    DRAW = 2,
    WIN = 3


SecondStrategyMapper = {
    'A': Choices.ROCK,
    'B': Choices.PAPER,
    'C': Choices.SCISSORS,
    'X': GameDecider.LOSE,
    'Y': GameDecider.DRAW,
    'Z': GameDecider.WIN,
}


class GamePoints(enum.Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


SecondStrategyRule = {
    GameDecider.WIN: {
        Choices.ROCK: Choices.PAPER,
        Choices.PAPER: Choices.SCISSORS,
        Choices.SCISSORS: Choices.ROCK,
    },
    GameDecider.LOSE: {
        Choices.PAPER: Choices.ROCK,
        Choices.SCISSORS: Choices.PAPER,
        Choices.ROCK: Choices.SCISSORS,
        
    }
}


class GameRound:
    strategy: 'GameStrategy'

    def set_strategy(self, strategy: 'GameStrategy'):
        self.strategy = strategy

    def get_result(self):
        return self.strategy.resolve()

    def __init__(self, opponent_choice, my_choice) -> None:
        self.set = (opponent_choice, my_choice)


class GameStrategy(ABC):
    @abstractmethod
    def resolve(self) -> int:
        pass


class FirstStrategy(GameStrategy):
    def __init__(self, round: GameRound) -> None:
        self.opponent = FirstStrategyMapper[round.set[0]]
        self.me = FirstStrategyMapper[round.set[1]]

    def resolve(self):
        if self.opponent == self.me:
            return GamePoints.DRAW.value + self.me.value

        if (self.opponent == Choices.PAPER and self.me == Choices.SCISSORS) or\
            (self.opponent == Choices.SCISSORS and self.me == Choices.ROCK) or\
            (self.opponent == Choices.ROCK and self.me == Choices.PAPER):
            return GamePoints.WIN.value + self.me.value

        return GamePoints.LOSE.value + self.me.value


class SecondStrategy(GameStrategy):
    def __init__(self, round: GameRound) -> None:
        self.opponent: Choices = SecondStrategyMapper[round.set[0]]
        self.game_result: GameDecider = SecondStrategyMapper[round.set[1]]

    def resolve(self) -> int:
        if self.game_result == GameDecider.DRAW:
            return self.opponent.value + GamePoints.DRAW.value

        my_choice = SecondStrategyRule[self.game_result][self.opponent]
        game_points = GamePoints[self.game_result.name]
        return my_choice.value + game_points.value


with open('./input.txt', 'r') as r:
    input = r.readlines()

total = 0

for i, line in enumerate(input):
    line = line.strip('\n').split(' ')

    round = GameRound(line[0], line[1])

    # strategy = FirstStrategy(round) # Solution for the first part
    strategy = SecondStrategy(round) # Solution for the second part

    round.set_strategy(strategy)
    total += round.get_result()

print(total)