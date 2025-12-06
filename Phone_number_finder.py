import os
def check_if_phone_number(string):
    if len(string) != 12:
        return False
    if not string[:3].isdigit():
        return False
    if string[3] != '-':
        return False
    if not string[4:7].isdigit():
        return False
    if string[7] !='-':
        return False
    if not string[8:].isdigit():
        return False
    return True

def get_data():
    string = ''
    input_file_path = input("Enter the path to the input file: ")
    if os.path.exists(input_file_path) and not os.path.isdir(input_file_path):
        with open(input_file_path, 'r') as f:
            string = f.read()
    return string

def main():
    string = get_data()
    for i in range(len(string)):
        if check_if_phone_number(string[i:i+12]):
            print(f"{i}: {string[i:i+12]}")
    print("Done")        

if __name__ == "__main__":
    main()
