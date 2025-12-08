import pyinputplus
import random

number_1 = 0
number_2 = 0
def check_answer(answer):
    try:
        answer = int(answer)
        if answer == number_1*number_2:
            return 'Correct'
        else:
            raise Exception('Incorrect Answer')
    
    except Exception as e:
        raise Exception(e if str(e)=='Incorrect Answer' else 'Invalid input Enter an integer')

try:    
  num_questions = pyinputplus.inputInt(prompt='Enter number of questions you want to get asked, min = 1, max = 10: ',limit=5,min=1,max=10)
except pyinputplus.RetryLimitException:
    print('Out of attempts')
for i in range(num_questions):
    number_1 = random.randint(0,50)
    number_2 = random.randint(0,50)
    print('You have 1 minute and 5 attempts')
    try:
        answer = pyinputplus.inputCustom(check_answer, prompt=f'{number_1} x {number_2} = ', limit= 5, timeout=60)
        print(answer)
    except pyinputplus.TimeoutException:
        print('Out of time')
    except  pyinputplus.RetryLimitException:
        print('Out of attempts')               
          