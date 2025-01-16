class Yatzy:

    @staticmethod
    def chance(*dice):
        total = sum(dice)
        return total

    @staticmethod
    def yatzy(dice):
        if len(set(dice)) == 1:
            return 50
        else:
            return 0

    @staticmethod
    def ones(*dice):
        sum = 0
        for ones in dice:
            if ones == 1:
                sum += 1

        return sum

    @staticmethod
    def twos(*dice):
        sum = 0
        for twos in dice:
            if twos == 2:
                sum += 2
        return sum

    @staticmethod
    def threes(*dice):
        sum = 0
        for threes in dice:
            if threes == 3:
                sum += 3
        return sum

    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(*dice):
        sum = 0
        for fours in dice:
            if fours == 4:
                sum += 4
        return sum

    def fives(*dice):
        sum = 0
        for five in dice:
            if five == 5:
                sum += 5
        return sum

    def sixes(*dice):
        sum = 0
        for sixes in dice:
            if sixes == 6:
                sum += 6
        return sum

    def score_pair(*dice):
        sum = []
        for die in dice:
            diego_mira_y_aprende = list(dice)
            diego_mira_y_aprende.remove(die)
            if die in diego_mira_y_aprende:
                sum.append(die * 2)
        return max(sum)





    @staticmethod
    def two_pair(*dice):
        respuesta = []
        cuenta = []
        for die in dice:
            if die not in cuenta:
                cuenta.append(die)
            elif die not in respuesta:
                respuesta.append(die)
            if len(respuesta) == 2:
                break
        if len(respuesta) == 2:
            return sum(respuesta)*2
        else:
            return 0


    @staticmethod
    def four_of_a_kind(*dice):
        respuesta = []
        cuenta = []
        for die in dice:
            if die not in cuenta:
                cuenta.append(die)
            elif die not in respuesta:
                respuesta.append(die)
        for num in respuesta:
            if dice.count(num) >= 4:
                return num * 4
        return 0

    

    @staticmethod
    def three_of_a_kind(*dice):
        respuesta = []
        cuenta = []
        for die in dice:
            if die not in cuenta:
                cuenta.append(die)
            elif die not in respuesta:
                respuesta.append(die)
        for num in respuesta:
            if dice.count(num) >= 3:
                return num * 3
        return 0

    @staticmethod
    def smallStraight(*dice):
        unique_dice = sorted(set(dice))
        small_straights = [
            [1, 2, 3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6]
        ]

        for straight in small_straights:
            if all(num in unique_dice for num in straight):
                return 15
    
        return 0

    @staticmethod
    def largeStraight(*dice):
        unique_dice = sorted(set(dice))
        large_straights = [
            [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 6]
        ]

        for straight in large_straights:
            if all(num in unique_dice for num in straight):
                return 20
    
        return 0

    @staticmethod
    def fullHouse(*dice):
        cuenta = []
        for die in dice:
            if die not in cuenta:
                cuenta.append(die)
        full = [dice.count(num) for num in cuenta]
        if 3 in full and 2 in full:
            return sum(dice)

        return 0