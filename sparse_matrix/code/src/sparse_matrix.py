import os

class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        """
        Initialize the SparseMatrix object.
        If file_path is provided, load the matrix from the file.
        Otherwise, initialize an empty matrix with specified dimensions.

        :param file_path: Path to the file containing the matrix data (optional).
        :param num_rows: Number of rows in the matrix (optional).
        :param num_cols: Number of columns in the matrix (optional).
        """
        if file_path:
            # Load the matrix from the given file path
            self.num_rows, self.num_cols, self.elements = self.load_from_file(file_path)
        else:
            # Initialize an empty matrix with specified dimensions
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.elements = {}  # Dictionary to store non-zero elements

    def load_from_file(self, file_path):
        """
        Load a sparse matrix from a file.

        :param file_path: Path to the file containing the matrix data.
        :return: A tuple containing the number of rows, number of columns, and the elements dictionary.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Read the number of rows and columns from the first two lines
        num_rows = int(lines[0].strip().split('=')[1])
        num_cols = int(lines[1].strip().split('=')[1])
        elements = {}
        
        # Read the elements from the subsequent lines
        for line in lines[2:]:
            if line.strip():  # Ignore empty lines
                try:
                    # Remove parentheses and split by commas
                    line = line.strip().replace('(', '').replace(')', '')
                    row, col, value = map(int, line.split(','))
                    elements[(row, col)] = value
                except ValueError:
                    # Raise an error if the file format is incorrect
                    raise ValueError("Input file has wrong format")

        return num_rows, num_cols, elements

    def get_element(self, row, col):
        """
        Get the value of the element at the specified row and column.

        :param row: The row index.
        :param col: The column index.
        :return: The value of the element.
        """
        return self.elements.get((row, col), 0)  # Return 0 if the element is not in the dictionary

    def set_element(self, row, col, value):
        """
        Set the value of the element at the specified row and column.

        :param row: The row index.
        :param col: The column index.
        :param value: The value to set.
        """
        if value != 0:
            self.elements[(row, col)] = value  # Add or update the element in the dictionary
        elif (row, col) in self.elements:
            del self.elements[(row, col)]  # Remove the element if the value is zero

    def add(self, other):
        """
        Add two sparse matrices.

        :param other: The matrix to add.
        :return: The resulting matrix after addition.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions must match for addition")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        result.elements = self.elements.copy()  # Start with a copy of the current elements

        for (row, col), value in other.elements.items():
            # Add the corresponding elements from the other matrix
            result.set_element(row, col, result.get_element(row, col) + value)
        
        return result

    def subtract(self, other):
        """
        Subtract one sparse matrix from another.

        :param other: The matrix to subtract.
        :return: The resulting matrix after subtraction.
        """
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        result.elements = self.elements.copy()  # Start with a copy of the current elements

        for (row, col), value in other.elements.items():
            # Subtract the corresponding elements from the other matrix
            result.set_element(row, col, result.get_element(row, col) - value)
        
        return result

    def multiply(self, other):
        """
        Multiply two sparse matrices.

        :param other: The matrix to multiply with.
        :return: The resulting matrix after multiplication.
        """
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        
        for (row, col), value in self.elements.items():
            for k in range(other.num_cols):
                # Only multiply and add if the element in the other matrix is non-zero
                if (col, k) in other.elements:
                    result.set_element(row, k, result.get_element(row, k) + value * other.elements[(col, k)])
        
        return result

    def __str__(self):
        """
        Return a string representation of the sparse matrix.
        """
        return f"SparseMatrix({self.num_rows}, {self.num_cols}, {self.elements})"

def read_matrix_from_file(file_path):
    """
    Helper function to read a matrix from a file.

    :param file_path: Path to the file containing the matrix data.
    :return: A SparseMatrix object.
    """
    return SparseMatrix(file_path=file_path)

def main():
    import sys  # Importing sys to access command-line arguments
    if len(sys.argv) != 4:
        print("Usage: sparse_matrix.py <operation> <matrix1> <matrix2>")
        return

    operation = sys.argv[1]  # Operation to perform (add, subtract, multiply)
    matrix1_path = sys.argv[2]  # Path to the first matrix file
    matrix2_path = sys.argv[3]  # Path to the second matrix file

    # Read the matrices from the provided file paths
    matrix1 = read_matrix_from_file(matrix1_path)
    matrix2 = read_matrix_from_file(matrix2_path)

    if operation == 'add':
        result = matrix1.add(matrix2)
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
    else:
        print("Unknown operation")
        return
    
    print(result)  # Print the result of the operation

if __name__ == "__main__":
    main()  # Execute the main function when the script is run
