import os
import re

phone_number_pattern = r'(\d{3})[.\s-]?(\d{3})[.\s-]?(\d{4})'

def find_phone_numbers(text):
    import re
    phone_numbers = re.findall(phone_number_pattern, text)
    if phone_numbers:
        for i in range(len(phone_numbers)):
            first, second, third = phone_numbers[i]
            print(f"{i+1}: {first}-{second}-{third}")
    else:
        print("No phone numbers found.")

def get_data():
    string = ''
    input_file_path = input("Enter the path to the input file: ")
    if os.path.exists(input_file_path) and not os.path.isdir(input_file_path):
        with open(input_file_path, 'r') as f:
            string = f.read()
    else:
        print("Invalid file path.")        
    return string

def main():
    string = get_data()
    find_phone_numbers(string)


if __name__ == "__main__":
    main()