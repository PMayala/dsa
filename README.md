# Unique Integers Assignment

This repository contains a Python solution for the Unique Integers assignment, a task commonly encountered in Enterprise Web Development courses. The assignment requires reading a list of integers from an input file and generating an output file containing sorted unique integers, adhering to specific formatting rules.

## Features

- **Input Handling:** Reads integers from input files with support for various formats, including optional leading/trailing whitespace, empty lines, multiple integers per line, and non-integer inputs.
- **Unique Integer Generation:** Generates output files with sorted unique integers.
- **File Organization:** Organizes code and sample data according to assignment guidelines.
- **Documentation:** Provides internal documentation within the code for clarity and understanding.

## Algorithm

1. **Initialize a boolean array named "seen" to keep track of seen integers from -1023 to 1023.**

2. **Open the input file.**

3. **For each line in the input file:**
     a. Remove any leading and trailing whitespaces from the line.
     b. Check if the line is not empty:
          i. Attempt to convert the line to an integer.
          ii. If the conversion is successful and the integer falls within the range -1023 to 1023:
               - Add the integer to a set of unique integers.
               - This range is chosen because it encompasses the expected range of integers according to the problem description.
               - Using a set ensures that only unique integers are stored, avoiding duplicates.

4. **Open the output file.**
     - This file will store the unique integers extracted from the input file.

5. **Write the unique integers from the set to the output file in sorted order.**
     - Sorting ensures that the integers are written in ascending order, as required by the problem statement.
     - Writing the integers to the output file one by one ensures that each integer is written on a separate line.

6. Close both the input and output files.
     - Closing the files is important to release system resources and ensure proper file handling.

## Usage

1. **Clone the Repository:** Clone or download the repository to your local machine.
2. **Navigate to Project Directory:** Open a terminal or command prompt and navigate to the project directory.
3. **Run the Script:** Execute the Python script `UniqueInt.py`, providing appropriate input and output file paths as arguments.

   Example:
   ```bash
   python UniqueInt.py input_file.txt output_file.txt
   ```

## File Structure

- **code/src/UniqueInt.py:** Main Python script containing the solution code.
- **sample_inputs/:** Directory containing sample input files.
- **sample_results/:** Directory containing corresponding sample output files.
- **README.md:** This README file providing an overview of the project.

## Sample Input

- Sample input files are provided in the `sample_inputs/` directory. These files contain lists of integers in various formats, including positive and negative integers with optional leading/trailing whitespace.

## Sample Output

- Corresponding sample output files demonstrating the expected format of the generated output are provided in the `sample_results/` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This assignment is part of the curriculum for Enterprise Web Development courses, aimed at practicing file handling, data manipulation, and algorithmic problem-solving skills.

## Improvements

- **Error Handling:** Improve error handling for invalid input files, such as missing input files or unsupported file formats.
- **Testing:** Implement automated testing for the solution code, ensuring consistent results for various input files.
- **Code Optimization:** Optimize the solution code for performance, reducing memory usage and execution time.
- **Documentation:** Add additional documentation for the solution code, including comments and docstrings.
- **Code Style:** Improve code style and formatting, adhering to PEP 8 guidelines.
- **Additional Features:** Implement additional features, such as support for different integer ranges or input file formats.
