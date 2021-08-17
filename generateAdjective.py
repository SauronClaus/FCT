import random

def generateAdjective(tier):
    tierFile = open("Adjectives\\" + tier + ".txt", "r", encoding='utf8')
    adjectives = tierFile.read().split("\n")
    RNG = random.randint(0, len(adjectives)-1)
    randomAdjective = adjectives[RNG]

    print("Generated " + randomAdjective + "!")
    return randomAdjective