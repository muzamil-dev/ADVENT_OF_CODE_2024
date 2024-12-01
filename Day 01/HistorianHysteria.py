import fileinput

filename = "input.txt"

def main():
    left = []
    right = []

    # Read the file
    with fileinput.input(files=(filename)) as f:
        # Iterate through the file
        for line in f:
            nums = line.split('   ')

            # Append numbers to the lists
            left.append(int(nums[0]))
            right.append(int(nums[1]))

    # Sort the lists
    left.sort()
    right.sort()

    total_distance = 0

    # Calculate the total distance
    for i in range(len(left)):
        total_distance += abs(left[i] - right[i])

    # Print the total distance
    print(total_distance)

main()
