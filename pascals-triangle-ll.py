# next_element = previous element×(rowIndex−position+1) / position

def getRow(self, rowIndex):
    row = [1]

    for i in range(1, rowIndex+1):
        next_element = row[i-1] * (rowIndex - i + 1) // i
        row.append(next_element)

    return row