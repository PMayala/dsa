# Sparse Matrix Operations

## Overview

This project implements operations on sparse matrices, which are matrices predominantly filled with zeros. The program supports loading sparse matrices from files, and performing addition, subtraction, and multiplication operations on these matrices.

## Directory Structure

The project directory is organized as follows:

```
/dsa/sparse_matrix/
├── code/
│   └── src/
│       └── sparse_matrix.py
└── sample_inputs/
    ├── matrix1.txt
    └── matrix2.txt
```

- **code/src/**: Contains the implementation of the sparse matrix operations.
- **sample_inputs/**: Contains sample input files for testing the program.

## Input File Format

Each input file for a sparse matrix follows this format:

```
rows=NUMBER_OF_ROWS
cols=NUMBER_OF_COLUMNS
(ROW_INDEX, COL_INDEX, VALUE)
...
```

Example:

```
rows=4
cols=4
(0, 1, 5)
(1, 3, 8)
(3, 0, -3)
```

This example represents a 4x4 matrix with non-zero values at specific positions.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Open a terminal or command prompt.
2. Navigate to the `code/src` directory:

   ```sh
   cd /dsa/sparse_matrix/code/src/
   ```

3. Run the script with the desired operation (add, subtract, multiply) and paths to the input matrix files:

   ```sh
   python sparse_matrix.py <operation> <matrix1_path> <matrix2_path>
   ```

   - `<operation>`: The operation to perform (`add`, `subtract`, or `multiply`).
   - `<matrix1_path>`: Path to the first matrix file.
   - `<matrix2_path>`: Path to the second matrix file.

### Example Commands

**Addition:**

```sh
python sparse_matrix.py add ../sample_inputs/matrix1.txt ../sample_inputs/matrix2.txt
```

**Subtraction:**

```sh
python sparse_matrix.py subtract ../sample_inputs/matrix1.txt ../sample_inputs/matrix2.txt
```

**Multiplication:**

```sh
python sparse_matrix.py multiply ../sample_inputs/matrix1.txt ../sample_inputs/matrix2.txt
```

### Error Handling

- The program will raise an error if the input file format is incorrect (e.g., incorrect parentheses, floating point values).
- The program will raise an error if the matrix dimensions do not match the requirements for the specified operation (e.g., trying to add matrices of different sizes, or trying to multiply matrices with incompatible dimensions).

## Code Structure

### SparseMatrix Class

The `SparseMatrix` class provides the following methods:

- `__init__(self, file_path=None, num_rows=None, num_cols=None)`: Initializes the matrix, either from a file or with specified dimensions.
- `load_from_file(self, file_path)`: Loads a sparse matrix from a file.
- `get_element(self, row, col)`: Gets the value of the element at the specified position.
- `set_element(self, row, col, value)`: Sets the value of the element at the specified position.
- `add(self, other)`: Adds two sparse matrices.
- `subtract(self, other)`: Subtracts one sparse matrix from another.
- `multiply(self, other)`: Multiplies two sparse matrices.
- `__str__(self)`: Returns a string representation of the sparse matrix.

### Helper Functions

- `read_matrix_from_file(file_path)`: Reads a matrix from a file and returns a `SparseMatrix` object.
- `main()`: Main function to execute the script based on command-line arguments.

## Sample Input Files

Place your input files in the `sample_inputs` directory. Example files (`matrix1.txt`, `matrix2.txt`) are provided to get you started.

## License

This project is open-source and available under the MIT License.
