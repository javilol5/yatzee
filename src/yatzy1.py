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
        suma = []
        for die in dice:
            diego_mira_y_aprende = list(dice)
            diego_mira_y_aprende.remove(die)
            if die in diego_mira_y_aprende:
                suma.append(die * 2)
        if len(suma)%2 != 0:
            suma.pop()
        
        return sum(suma)/2

    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
