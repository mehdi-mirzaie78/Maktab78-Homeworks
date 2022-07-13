# Homework 6
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
            result.show()
            return result
        else:
            raise ValueError("Number of rows or columns or both are wrong!")

    def __sub__(self, other: "Matrix") -> "Matrix":
        """
            ---------------------- sub -----------------------
            1: multiplying -1 to the second matrix
            2: calling add for adding first matrix and second
        """

        temp = []
        for i in range(self.row):
            temp.append([other.matrix[i][j] * -1 for j in range(self.column)])
        other.matrix = temp.copy()
        return self.__add__(other)

    def __mul__(self, other: "Matrix") -> "Matrix":
        """
        ---------------------------- mul -----------------------------
        Multiplying each row of first matrix to the column of another matrix
        if the number of columns of the first matrix equals to the number
        of rows of the second matrix.
        M1(m X n) * M2(n X o) => Res(m X o)
        """
        if self.column == other.row:
            result = Matrix(self.row, other.column)
            for i in range(self.row):
                for k in range(other.column):
                    summation = 0
                    for j in range(self.column):
                        element = self.matrix[i][j] * other.matrix[j][k]
                        summation += element
                    else:
                        result.matrix[i][k] = summation
            result.matrix = [list(map(round, result.matrix[i])) for i in range(self.row)]
            result.show()
            return result

        else:
            raise ValueError("Number of rows of first matrix doesn't equal to"
                             "number of columns of second matrix")

    def inverse(self) -> "Matrix":
        """ inverse of a square matrix 2x2"""
        if self.row == self.column and self.row == 2:
            det = self.matrix[0][0] * self.matrix[1][1] - \
                  self.matrix[0][1] * self.matrix[1][0]
            result = Matrix(2, 2)
            for i in range(self.row):
                for j in range(self.column):
                    result.matrix[i][j] = self.matrix[i][j] / det
            result.matrix[0][0], result.matrix[1][1] = result.matrix[1][1], result.matrix[0][0]
            result.matrix[0][1] = result.matrix[0][1] * -1
            result.matrix[1][0] = result.matrix[1][0] * -1
            return result
        else:
            raise ValueError("the matrix is not square matrix or the number of rows is not 2")

    def __truediv__(self, other: "Matrix") -> "Matrix":
        """Multiplying first matrix to second matrix.inverse()
        A/B = A * B.inv"""
        ans = self.__mul__(other.inverse())
        return ans

    def __eq__(self, other: "Matrix") -> bool:
        if self.row == other.row and self.column == other.column:
            lst = []
            for i in range(self.row):
                for j in range(self.column):
                    t = self.matrix[i][j] == other.matrix[i][j]
                    lst.append(t)
            return all(lst)
        else:
            raise ValueError("Rows and columns aren't match")

    def __ne__(self, other: "Matrix") -> bool:
        return not (self.__eq__(other))

    def __gt__(self, other: "Matrix") -> bool:
        s1, s2 = 0, 0
        for i in range(self.row):
            s1 += sum(self.matrix[i])
        for j in range(other.row):
            s2 += sum(other.matrix[j])
        return s1 > s2

    def __ge__(self, other: "Matrix") -> bool:
        return self.__eq__(other) or self.__gt__(other)

    def __lt__(self, other: "Matrix") -> bool:
        return not (self.__ge__(other))

    def __le__(self, other: "Matrix") -> bool:
        return not (self.__gt__(other))

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


class SquareMatrix(Matrix):
    def __init__(self, row: int) -> None:
        super().__init__(row, row)

    def main_diameter(self) -> dict:
        """Returns a dictionary of indexes and elements for main diameter"""
        dic = {f'M{i}{i}': self.matrix[i][i] for i in range(self.row)}
        return dic

    def sub_diameter(self) -> dict:
        """Returns a dictionary of indexes and elements for sub diameter"""
        dic = {f'M{i}{self.row - 1 - i}': self.matrix[i][self.row - 1 - i] for i in range(self.row)}
        return dic

    def det(self) -> float | int:
        """
        ------------------ det ------------------
        calculates det of the square matrix
        for any matrix with this size 2x2 or 3x3
        """
        if self.row == 2:
            main = 1
            sub = 1
            for i in self.main_diameter().values():
                main *= i
            for j in self.sub_diameter().values():
                sub *= j
            return main - sub

        elif self.row == 3:
            m = self.matrix
            ans = m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))
            ans -= m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))
            ans += m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0]))
            return ans
        else:
            raise ValueError("I don't know more :) ")


mat1 = Matrix(2, 3)
mat1.show()
mat1.matrix = [[-10, 20, -30], [40, -50, 60]]
mat1.show()
print(abs(mat1))
print('_________________')
mat2 = Matrix(2, 3)
mat2.matrix = [[1, 2.5, 3], [4, 5, 6]]
print('mat1: ')
mat1.show()
print('mat2: ')
mat2.show()
print('---add---')
mat_add = mat1 + mat2
print('---sub---')
mat_sub = mat1 - mat2
print('---mul---')
mat1 = Matrix(2, 3)
mat1.matrix = [[1, 2, 3], [4, 5, 6]]
mat2 = Matrix(3, 3)
mat2.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat_mul = mat1 * mat2
print('---div---')
m1 = Matrix(2, 2)
m1.matrix = [[4, 7], [2, 6]]
mat_same = m1 * m1.inverse()
m2 = Matrix(2, 2)
m2.matrix = [[4, 8], [2, 6]]
print(m1 == m2)
print(m1 != m2)
print(m1 > m2)
print(m1 >= m2)
print(m1 < m2)
print(m1 <= m2)

print('-------------------')

square = SquareMatrix(3)
square.show()
square.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square.show()
print("Main diameter:", square.main_diameter())
print("Sub diameter:", square.sub_diameter())
print("Det:", square.det())
# print(help(Matrix))
# I did the best I could. Hope you like it
