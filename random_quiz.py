import pyinputplus
import random
from pathlib import Path

states_capitals = {
   'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'

}

def make_quiz_files():
    quiz_path_list = []
    try:
        num_quizes = pyinputplus.inputInt(prompt='Enter the number of quizes you want to make: ', max=50,min=1,limit=5)
        quiz_folder_path = pyinputplus.inputFilepath(prompt='Enter the folder path where the quizes will be stored: ',limit = 5)
        quiz_folder_path = Path(quiz_folder_path)
    except pyinputplus.RetryLimitException:
        return None
    if not quiz_folder_path.is_dir():
       quiz_folder_path.mkdir(parents=True,exist_ok=True)
    for quiz in range(num_quizes):
        quiz_file_name = f'Quiz - {quiz+1}.txt'
        quiz_path = quiz_folder_path / quiz_file_name
        quiz_path.touch()
        quiz_path_list.append(quiz_path)
    return quiz_path_list    
def write_questions_on_files(path_list):
    for path in path_list:
        with open(path,'w') as file:
            file.write('\t\t\tQuiz\n\n')
            states = list(states_capitals.keys())
            capitals = list(states_capitals.values())
            random.shuffle(states)
            question_number = 1
            for state in states:
                correct_capital = states_capitals[state]
                wrong_capitals = random.sample([w_capital for w_capital in capitals if w_capital != correct_capital],3)
                choices = wrong_capitals + [correct_capital]
                random.shuffle(choices)
                file.write(f"{question_number}. What is the capital of {state}?\n\n")
                file.write(f"A. {choices[0]}\nB. {choices[1]}\nC. {choices[2]}\nD. {choices[3]}\n\n")
                question_number += 1
    print("Done.")       
def main():
    file_path_list = make_quiz_files()
    if file_path_list is not None:
       write_questions_on_files(file_path_list)



if __name__ == '__main__':
    main()
