# def winner (args):
  # if len(set(args)) == 1:
    # return True

# def checkio(mass):
  # i = 0
  # while i < 3:
    # if winner(mass[i]):
      # return(mass[i][i])
    # elif winner(mass[row][i] for row in [0,1,2]):
      # return(mass[i][i])
    # i += 1
# #  return(filter(winner,(mass[row][row] for row in [0,1,2])))
  # print (list(zip(*mass)))
# #  elif len(set(mass[row][-(row+1)] for row in [0,1,2])) == 1:
# #    print('vv'); break
# #  print(list(mass[i][-i] for i in [0,1,2]))
# #  print(mass[0][2])
# #  print(set(mass[row][-(row+1)] for row in [0,1,2]))
# #  print(mass[2][-3])
# print(checkio([
    # "X.O",
    # "XX.",
    # "XOO"]))# == "X"
# print(checkio([
    # "XXX",
    # "XO0",
    # "0OX"]))# == "O"

# print(checkio([
    # "XX0",
    # "X0X",
    # "00X"]))# == "O"
# print(checkio([
    # "00X",
    # "X00",
    # "0X0"]))# == "D"
# print(checkio([
    # "OOX",
    # "XXO",
    # "OXX"]))# == "D"
def checkio(game_result):
    strnum = {'X': -1, '.': 0, 'O': 1}
    resnum = [[strnum[c] for c in row] for row in game_result]
    res_array = (list(map(sum, resnum))
                 + list(map(sum, map(list, zip(*resnum))))
                 + [sum([resnum[i][j] for i, j in ((0, 0), (1, 1), (2, 2))])]
                 + [sum([resnum[i][j] for i, j in ((0, 2), (1, 1), (2, 0))])])
    if any([n == -3 for n in res_array]):
        return "X"
    elif any([n == 3 for n in res_array]):
        return "O"
    else:
        return "D"


def checkio(game_result):
    result = 'D'
    rotated = zip(*game_result[::-1])
    for line in game_result:
        print line
        if "X" not in line and "." not in line:
            result = 'O'
            print "O wins in normal list"
        elif "O" not in line and "." not in line:
            result = 'X'
            print "X wins in normal list"
    for line in rotated:        
        print line
        if "X" not in line and "." not in line:
            result = 'O'
            print "O wins in normal list"
        elif "O" not in line and "." not in line:
            result = 'X'
            print "X wins in normal list"
    if game_result[0][0] == 'O' and  game_result[1][1] == 'O' and  game_result[2][2] == 'O':
        result = 'O'
    if game_result[0][0] == 'X' and  game_result[1][1] == 'X' and  game_result[2][2] == 'X':
        result = 'X'
    print result
    return result
