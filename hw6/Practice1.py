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
            lst = [None for _ in range(self.column)]
            self.matrix.append(lst)

    def __str__(self) -> str:
        return f"{self.matrix}"

    def __repr__(self) -> str:
        return f'This is a matrix class: {self.matrix} ' \
               f'It has {self.row} rows and {self.column} columns'

    def __len__(self) -> int:
        """ Returns the product of number of rows and number of column"""
        return self.row * self.column

    def __abs__(self) -> list:
        """Returns a matrix with absolute value of every member"""
        result = [list(map(abs, self.matrix[r])) for r in range(self.row)]
        return result

    def __setitem__(self, index1: int, index2: int, value: float | int) -> None:
        """Sets the given value for one member of matrix"""
        self.matrix[index1][index2] = value

    def __getitem__(self, index1: int, index2: int) -> float | int:
        """Returns one member of matrix with given indexes"""
        return self.matrix[index1][index2]

    def show(self) -> None:
        """Shows matrix in the right format"""
        for i in range(self.row):
            print(self.matrix[i])

    def set_values(self) -> None:
        """
        ------------------- set_values --------------------
        sets a float value for each member of Matrix object
        """

        temp = []
        for i in range(1, self.row + 1):
            ls = [float(input(f"Enter member{i}{j}: ")) for j in range(1, self.column + 1)]
            temp.append(ls)
        else:
            self.matrix = temp.copy()

    def transpose(self) -> None:
        """
        ---------------- transpose ----------------
        Converts a matrix with m rows and n column
        to a matrix with n rows and m columns
        """
        temp = []
        for j in range(self.column):
            temp.append([self.matrix[i][j] for i in range(self.row)])
        else:
            self.matrix = temp.copy()
            self.row, self.column = self.column, self.row


mat1 = Matrix(2, 3)
mat1.show()
mat1.matrix = [[-10.5, 20.1, -30], [40, -50, 60]]
mat1.matrix[0][0] = 100
print(mat1.matrix[1][1])
mat1.show()
print(abs(mat1))
print(mat1.__repr__())
mat1.transpose()
print('_________________')
mat1.show()
while True:
    exec(input('Enter: '))
