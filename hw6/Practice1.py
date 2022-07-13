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
        temp = []
        for i in range(self.row):
            lst = [None for _ in range(self.column)]
            temp.append(lst)
        self.matrix = temp.copy()

    @property
    def matrix(self):
        """matrix.getter"""
        return self._matrix

    @matrix.setter
    def matrix(self, value: "Matrix.matrix"):
        """matrix.setter: validating the number of rows and columns for setting value"""
        if len(value) == self.row and len(value[0]) == self.column:
            self._matrix = value
        else:
            raise ValueError("The number of rows or columns or both are wrong!")

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

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        ---------------------- add -----------------------
        1: Validating the number of rows and columns.
        2: Creating a Matrix object to store the result
        of summation
        3: adding each member of one matrix to another
        """
        if self.row == other.row and self.column == other.column:
            result = Matrix(self.row, self.column)
            temp = []
            for i in range(self.row):
                ls = [self.matrix[i][j] + other.matrix[i][j] for j in range(self.column)]
                temp.append(ls)
            result.matrix = temp.copy()
            return result
        else:
            raise ValueError("Number of rows or columns or both are wrong!")

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
mat1.matrix = [[-10, 20, -30], [40, -50, 60]]
mat1.show()
print(abs(mat1))
print('_________________')
mat2 = Matrix(2, 3)
mat2.matrix = [[1, 2.5, 3], [4, 5, 6]]
mat1.show()
print('------')
mat2.show()
mat3 = mat1 + mat2
print('------')
mat3.show()
