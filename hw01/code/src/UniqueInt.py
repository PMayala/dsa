class UniqueInt:
    def __init__(self):
        # Initialize a boolean array to track seen integers (-1023 to 1023)
        # We use a boolean array to efficiently track whether each integer within the range has been seen or not.
        # The array has a length of 2047 to cover the range from -1023 to 1023 inclusive.
        self.seen = [False] * 2047

    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        # Set to store unique integers
        # We use a set to efficiently store unique integers encountered in the input file.
        unique_integers = set()

        # Open the input file and iterate through each line
        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                # Remove leading and trailing whitespaces from the line
                # Stripping whitespace ensures consistent processing of integers from each line.
                line = line.strip()
                
                # Skip empty lines
                # Empty lines do not contain valid integers, so we skip processing them.
                if line:
                    try:
                        # Convert line to integer
                        # We attempt to convert each line to an integer to extract numerical values.
                        num = int(line)
                        # Check if the integer is within the valid range
                        # We ensure that the integer falls within the specified range (-1023 to 1023).
                        if -1023 <= num <= 1023:
                            # Add the integer to the set of unique integers
                            # If the integer is within the valid range, we add it to the set of unique integers encountered.
                            unique_integers.add(num)
                    except ValueError:
                        # Skip non-integer inputs
                        # We skip processing lines that cannot be converted to integers.
                        # This includes lines containing non-numeric characters or empty lines.
                        pass

        # Write unique integers to the output file in sorted order
        # We write the unique integers stored in the set to the output file in sorted order.
        # Sorting ensures that the integers are written in ascending order as required.
        with open(outputFilePath, 'w') as outputFile:
            for num in sorted(unique_integers):
                # Write each unique integer followed by a newline character
                outputFile.write(str(num) + '\n')

    @staticmethod
    def readNextItemFromFile(inputFileStream):
        # This method is not used in this implementation
        # The readNextItemFromFile method is not utilized in the current implementation and is provided for potential future use or expansion.
        pass

if __name__ == "__main__":
    # If this script is executed directly, run the following code
    # This section of code is executed only if the script is run directly, not when imported as a module

    # Create an instance of the UniqueInt class
    unique_int_processor = UniqueInt()

    # Define input and output file paths
    input_file_path = "C:\\Users\\USER\\Desktop\\dsa\\hw01\\sample_inputs\\small_sample_input_02.txt"
    output_file_path = "C:\\Users\\USER\\Desktop\\dsa\\hw01\\sample_results\\small_sample_input.txt_result.txt"

    # Process the input file to generate the output file with unique integers
    unique_int_processor.processFile(input_file_path, output_file_path)

    print("Unique integers extracted from input file and saved to output file.")
