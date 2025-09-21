import sys
import io
import os
import glob


# =====================================================================================
#  SOLUTION FUNCTION: PASTE YOUR CODE HERE
# =====================================================================================
# This is the function that will be tested. It should contain your solution logic.
# It's designed to read from standard input and write to standard output.

def solve():
    """
    Reads multiple test cases from standard input and prints the results.
    """
    try:

        import sys

        inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
        for i in range(0, len(inp), 2):
            case = list(map(int, inp[i + 1].split()))
            length = len(case)
            beautiful = False
            for j in range(length - 1):
                if abs(case[j] - case[j + 1]) <= 1:
                    beautiful = True
                    break
            if beautiful:
                print(0)
            elif length == 2:
                print(-1)
            else:
                print(1)



    except (IOError, ValueError) as e:
        print(f"Error processing input: {e}", file=sys.stderr)
    # --- END OF EXAMPLE SOLUTION ---

    # For a multi-line input problem, you might do something like this:
    # try:
    #     num_lines = int(sys.stdin.readline())
    #     for _ in range(num_lines):
    #         line = sys.stdin.readline().strip()
    #         # ... process the line ...
    #     print("Your result here")
    # except (IOError, ValueError):
    #     pass # Handle errors gracefully


# =====================================================================================
#  TEST CASE SETUP: CREATE FILES FOR YOUR TEST CASES
# =====================================================================================
# To use this tester, create files in the same directory as this script.
#
# 1. Create input files named:
#    input1.txt
#    input2.txt
#    ...
#
# 2. For each input file, create a corresponding output file named:
#    output1.txt
#    output2.txt
#    ...
#
# The script will automatically find these files and run your `solve()` function,
# comparing its output to the content of the corresponding output file.
#
# Example Directory Structure:
# .
# |-- template.py       (This script)
# |-- input1.txt
# |-- output1.txt
# |-- input2.txt
# |-- output2.txt
#
#
# Example `input1.txt`:
# 5
#
# Example `output1.txt`:
# 25
#

# =====================================================================================
#  TEST RUNNER: NO NEED TO EDIT BELOW THIS LINE
# =====================================================================================
# This part of the script discovers and runs the file-based tests.

def run_tests():
    """
    Discovers and executes the solution against all file-based test cases.
    """
    passed_count = 0
    failed_count = 0
    skipped_count = 0

    # Find all input files matching the pattern 'input*.txt'
    input_files = sorted(glob.glob('input*.txt'))

    if not input_files:
        print("\033[93mWARNING: No test case files found.\033[0m")
        print("Please create files like 'input1.txt' and 'output1.txt' in the same directory.")
        return

    print("=" * 50)
    print(f"Found {len(input_files)} test case(s). Running tests...")
    print("=" * 50)

    for i, input_filename in enumerate(input_files):
        case_name = os.path.splitext(input_filename)[0]
        output_filename = input_filename.replace('input', 'output', 1)

        print(f"--- Test Case {i + 1}: {case_name} ---")

        if not os.path.exists(output_filename):
            print(f"\033[93mSKIPPED: Output file '{output_filename}' not found.\033[0m\n")
            skipped_count += 1
            continue

        with open(input_filename, 'r') as f:
            input_data = f.read()

        with open(output_filename, 'r') as f:
            expected_output = f.read()

        # Redirect stdin to read from our input_data string
        original_stdin = sys.stdin
        sys.stdin = io.StringIO(input_data)

        # Redirect stdout to capture the output of the solve function
        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        actual_output = ""
        try:
            # Run the user's solution
            solve()
            # Get the output from the solution
            actual_output = captured_output.getvalue()
        except Exception as e:
            actual_output = f"An exception occurred during execution:\n{e}"
        finally:
            # Restore original stdin and stdout
            sys.stdin = original_stdin
            sys.stdout = original_stdout

        # Compare the actual output with the expected output, ignoring leading/trailing whitespace
        if actual_output.strip() == expected_output.strip():
            print("\033[92mPASSED\033[0m\n")  # Green color for PASSED
            passed_count += 1
        else:
            print("\033[91mFAILED\033[0m\n")  # Red color for FAILED
            failed_count += 1
            print("Expected Output:")
            print("-" * 20)
            print(expected_output.strip())
            print("-" * 20)
            print("\nActual Output:")
            print("-" * 20)
            print(actual_output.strip())
            print("-" * 20)
            print("")

    print("=" * 50)
    print("Test Summary:")
    print(f"\033[92mPassed: {passed_count}\033[0m")
    print(f"\033[91mFailed: {failed_count}\033[0m")
    if skipped_count > 0:
        print(f"\033[93mSkipped: {skipped_count}\033[0m")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
