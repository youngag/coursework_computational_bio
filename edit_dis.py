def diff(x, y, cost):
    if x == y:
        return 0
    keyStr = x + y
    return int(costBook[keyStr])

def align(one_Line, costBook):
    Split_Line = one_Line.split(",")

    # Defining an array with an extra row and col to represent a leading gap
    array = [[0] * (len(Split_Line[1])+1) for i in range(len(Split_Line[0])+1)]  # Zero fill array,

    xLine = Split_Line[0]
    yLine = Split_Line[1]

    # Changed so we include our extra line in the loop
    for i in range(1, len(xLine)+1):
        array[i][0] = array[i - 1][0] + int(costBook['-' + xLine[i - 1]])
    for i in range(1, len(yLine)+1):
        array[0][i] = array[0][i - 1] + int(costBook[yLine[i - 1] + '-'])

    # Changed so we include our extra row/col in the loop
    for i in range(1, len(xLine)+1):
        for j in range(1, len(yLine)+1):
            # The references to the original string now need -1 (i.e. i-1)
            array[i][j] = min(array[i - 1][j] + diff('-', xLine[i-1], costBook), 
                              array[i][j - 1] + diff(yLine[j-1], '-', costBook), 
                              array[i - 1][j - 1] + diff(yLine[j-1], xLine[i-1], costBook))
    return array
    
    def main():
      # todo: add callin
