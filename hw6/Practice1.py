# Homework 6
# Defining a Matrix class
class Matrix:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column
        self.matrix = []
        for i in range(self.row):
            lst = [None for j in range(self.column)]
            self.matrix.append(lst)

    def __str__(self):
        return f"{self.matrix}"

    def __repr__(self):
        return f'This is a matrix class: {self.matrix}'

    def set_values(self, row, col):
        if self.row != row or self.column != col:
            raise ValueError("The number of row or column is WRONG!")
        else:
            temp = []
            for i in range(1, row + 1):
                ls = [int(input(f"Enter member{i}{j}: ")) for j in range(1, col + 1)]
                temp.append(ls)
            else:
                self.matrix = temp.copy()


mat1 = Matrix(2, 3)
print(mat1)
print(mat1.__repr__())
mat1.set_values(2, 3)
print(mat1)
