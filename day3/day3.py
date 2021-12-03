def split_code(code):
    code = list(code[0])
    for i in range(len(code)):
        code[i] = int(code[i])
    return code

def count_higher_bit(bit_list):
    counter = 0
    for bit in bit_list:
        if bit == 1:
            counter += 1
    if counter >= (len(bit_list) / 2):
        return 1
    else:
        return 0
    
    
def count_lower_bit(bit_list):
    if count_higher_bit(bit_list) == 1:
        return 0
    else:
        return 1
    
def recursive_removal1(matrix, depth):
    m2 = Matrix()
        
    a = count_higher_bit(matrix.print()[depth])
    #print("number: ", a, " depth: ", depth)
    matrix.transposition()
    for row in matrix.print():
        if row[depth] == a:
            m2.append_row(row)
    #print(m2.print())
    m2.transposition()
    if len(m2.print()[0]) == 1:
        m2.transposition()
        return m2
    return recursive_removal1(m2, depth + 1)

def recursive_removal2(matrix, depth):
    m2 = Matrix()
    matrix.transposition()

    a = count_lower_bit(matrix.print()[depth])
    matrix.transposition()
    for row in matrix.print():
        if row[depth] == a:
            m2.append_row(row)
    if len(m2)==1:
        #m2.transposition()
        return m2
    return recursive_removal2(m2, depth + 1)
   
class Matrix():

    def __init__(self):
        self.matrix = []

    def add_value(self, row, column, value):
        self.values[row][column] = value

    def __len__(self):
        return len(self.matrix)

    def transpose(self, matrix):
        return[list(i) for i in zip(*matrix)]

    def transposition(self):
        self.matrix = self.transpose(self.matrix)

    def null_matrix(self, row, columns):
        self.rows = row
        self.columns = columns
        self.matrix = [[0 for j in range(self.columns)] for i in range(self.rows)]

    def print(self):
        return self.matrix

    def get_value(self, row, column):
        return self.matrix[row-1][column - 1]

    def set_value(self, row, column, value):
        self.matrix[row - 1][column - 1] = value

    def get_row(self, row):
        return self.matrix[row - 1]

    def get_column(self, column):
        matrix2 = self.matrix
        matrix2.transposition()
        return matrix2[column]

    def append_row(self, row):
        self.matrix.append(row)
        
    def set_row(self, row, values):
        self.matrix[row] = values

    def set_column(self, column, values):
        self.matrix.transpition()
        self.matrix[column - 1] = values
        self.matrix.transposition()

    def remove_row(self, row):
        self.matrix[row - 1].pop()
    

def main():
    m1 = Matrix()
    with open("day3_data", "r") as f:
                i = 0
                for line in f.readlines():
                        lines = line.split()
                        splitted = split_code(lines)
                        m1.append_row(splitted)
                        i += 1
                        #print(splitted)
    #print(m1.print())
    m1.transposition()

    final_bit = ["", ""]
    i = 0
    for row in m1.print():
        #print(row)
        final_bit[0] = final_bit[0] + str(count_higher_bit(row))
        #print("most common bit: ", count_higher_bit(row))
        final_bit[1] = final_bit[1] + str(count_lower_bit(row))
        i += 1
        
    first = int(final_bit[0], 2)
    second = int(final_bit[1], 2)
    print(first, "    ", second, "   result: ", first * second)


    ########## second part ######
    
    #print(m4.print())
    m2 = recursive_removal1(m1, 0)
    m3 = recursive_removal2(m1, 0)
    print(m2.print()[0])
    print(m3.print()[0])
    a = ""
    for bit in m2.print()[0]:
        a =  a + str(bit)
    print("valore oxigen: ", int(a, 2))
    b = ""
    for bit in m3.print()[0]:
        b = b + str(bit)
    print("valore co2: ", int(b, 2))
    print( int(a, 2) * int(b, 2))
    
if __name__ == "__main__":
    main()
