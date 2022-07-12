# Homework 6
# Defining a Matrix class
class Matrix:
    """
    ----------- Matrix class -----------
    row: int
        number of rows of matrix
    column: int
        number of columns of matrix
    """

    def __init__(self, row, column) -> None:
        """
        --------- __init__ -----------
        initialize the instance attributes of Matrix class
        creating a matrix with row X column with
        None for each member.
        """

        self.row = row
        self.column = column
        self.matrix = []
        for i in range(self.row):
            lst = [None for j in range(self.column)]
            self.matrix.append(lst)

    def __str__(self) -> str:
        return f"{self.matrix}"

    def __repr__(self) -> str:
        return f'This is a matrix class: {self.matrix}'

    def set_values(self, row: int, col: int) -> None:
        """
        ----------------- set_values -----------------
        sets a float value for each member of Matrix object
        """
        if self.row != row or self.column != col:
            raise ValueError("The number of row or column is WRONG!")
        else:
            temp = []
            for i in range(1, row + 1):
                ls = [float(input(f"Enter member{i}{j}: ")) for j in range(1, col + 1)]
                temp.append(ls)
            else:
                self.matrix = temp.copy()

    def transpose(self):
        temp = []
        for j in range(self.column):
            temp.append([self.matrix[i][j] for i in range(self.row)])
        else:
            self.matrix = temp.copy()
            self.row, self.column = self.column, self.row


mat1 = Matrix(2, 3)
print(mat1)
print(mat1.__repr__())
mat1.set_values(2, 3)
for i in range(mat1.row):
    print(mat1.matrix[i])
mat1.transpose()
print('_________________')
for i in range(mat1.row):
    print(mat1.matrix[i])