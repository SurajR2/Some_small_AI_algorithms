def calculate_heuristic(blocks, correct_support_structure, wrong_support_structure):
    heuristic = 0

    for block in blocks:
        if block in correct_support_structure:
            # For each block that has the correct support structure: +1 to every block in the support structure
            heuristic += 1
        elif block in wrong_support_structure:
            # For each block that has a wrong support structure: -1 to every block in the support structure
            heuristic -= 1

    return heuristic

def main():
    # Example Blocks World state
    blocks = ['A', 'B', 'C', 'D']

    # Example correct support structure and wrong support structure
    correct_support_structure = {'A': 'table', 'B': 'A', 'C': 'table', 'D': 'C'}
    wrong_support_structure = {'A': 'table', 'B': 'C', 'C': 'table', 'D': 'A'}

    # Calculate heuristic value
    heuristic_value = calculate_heuristic(blocks, correct_support_structure, wrong_support_structure)

    print("Heuristic value:", heuristic_value)

if __name__ == "__main__":
    main()