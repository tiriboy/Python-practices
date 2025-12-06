import re
import os

phone_number_pattern = r'[(]?\d{3}[)]?[.\s-]\d{3}[.\s-]\d{4}'
email_pattern = r'[\w._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

def find_phone_numbers_write_to_file(string):
    phone_number_list = re.findall(phone_number_pattern, string)
    if phone_number_list:
        phone_number_file_path = input("Enter the path to save phone numbers: ")
        with open(phone_number_file_path, 'w') as f:
              f.writelines([number + '\n' for number in phone_number_list])
        print(f"Phone numbers saved to {phone_number_file_path}")   
    else:
        print("No phone numbers found.")

def find_emails_write_to_file(string):
    email_list = re.findall(email_pattern, string)
    if email_list:
        email_file_path = input("Enter the path to save email addresses: ")
        with open(email_file_path, 'w') as f:
                f.writelines([email + '\n' for email in email_list])
        print(f"Email addresses saved to {email_file_path}")
    else:
        print("No email addresses found.")

def get_data():
    string = ''
    path = input("Enter the path to the text file where the details are stored: ")
    if os.path.exists(path) and not os.path.isdir(path):
        with open(path, 'r') as f:
            string = f.read()
        if string:
            find_phone_numbers_write_to_file(string)
            find_emails_write_to_file(string)
        else:
            print("The file is empty.")    
 
    else:
        print("Invalid file path.")        

def main():
    print("Code finds emails and phone numbers from a text file and saves them to separate files.")
    get_data()


if __name__ == "__main__":
    main()
