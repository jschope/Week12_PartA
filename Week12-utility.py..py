# Jacob Schope
# CSCI 102 - Section C
# Week 12 - Part B

def PrintOutput(string):
    print(f"OUTPUT {string}")


def LoadFile(file_name):
    lines = []
    with open(file_name, "r") as x:
        r = x.readlines()
        for line in range(len(r)):
            lines.append(r[line])
            lines = [line.replace("\n", "") for line in lines]
        return lines

def UpdateString(string, letter, index):
    string1 = list(string)
    string1[index] = letter
    string = "".join(string1)
    print(f"OUTPUT", string)

    # Fix
def FindWordCount(list_a, word):
    x = list_a.count(word)
    return x

def ScoreFinder(players, scores, name):
    score = 0
    for i in range(len(players)):
        if(players[i].lower()==name.lower()):
            score = scores[1]
            break
    if(scores == 0):
        print("OUTPUT player not found")
    else:
        print(f"OUTPUT {name} got a score of {score}")

def Union(list_A, list_B):
    final=[]
    for i in list_A:
        if i not in final:
            final.append(i)
    for i in list_B:
        if i not in final:
            final.append(i)
    return final
        
        
def Intersection(players, players2):
    res = []
    for i in players:
        if(not i in res) and(i in players2):
            for x in range(min(players.count(i), players2.count(i))):
                res.append(i)
    return res
    



