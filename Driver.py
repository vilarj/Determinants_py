class Functions:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        matrix = ([row], [column])

        if row != column:
            print('The matrix needs to be squared')
        elif row == 1 and column == 1:
            return 1
        elif row == 2 and column == 2:
            self.setMatrix(matrix)
            self.matrix2D(matrix)

        else:
            pass


    def setMatrix(self, matrix):
        for x in matrix:
            self.matrix = matrix[x]

    def matrix2D(self, matrix):
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]

        return (a*d) - (b*c)
