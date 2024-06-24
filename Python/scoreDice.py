from collections import Counter
def score(dice):
    counterDice = Counter(dice)
    counterThree = list(filter(lambda x: counterDice[x] >= 3, counterDice))

    points = 0
    if len(counterThree) == 1:
        points += 1000 if counterThree[0] == 1 else counterThree[0] * 100

    points += (dice.count(1) - 3) * 100 if dice.count(1) >= 3 else dice.count(1) * 100
    points += (dice.count(5) - 3) * 50 if dice.count(5) >= 3 else dice.count(5) * 50

    return points






print(score([5, 5, 5, 3, 3]))