import sys

def get_input(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    input = get_input(sys.argv[1])
    zero_count = 0
    current_position = 0
    rotate_list = input.split()
    for instruction in rotate_list:
        direction = instruction[0]
        num = instruction[1:]
        #change num from string to number type?!
        if direction == "L":
            current_position = current_position - num
        else:
            current_position = current_position + num
    
main()
