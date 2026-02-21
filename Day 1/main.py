import sys

def get_input(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    input = get_input(sys.argv[1])
    zero_count = 0
    current_position = 50
    rotate_list = input.split()
    for instruction in rotate_list:
        direction = instruction[0]
        num = int(instruction[1:])
        print(f"current position is {current_position}")
        if direction == "L":
            result = current_position - num
            if result < 0:
                diff = num - current_position - 1
                current_position = 99 - diff
                print(f"rotation is {instruction}")
                print(f"new position is {current_position}")
            else:
                current_position = result
                print(f"new position is {current_position}")
        if direction == "R":
            result = current_position + num
            if result > 99:
                diff = num - current_position - 1
                current_position = 0 + diff
                print(f"rotation is {instruction}")
                print(f"difference is {diff}")
                print(f"new position is {current_position}")
        else:
            current_position = result


main()
