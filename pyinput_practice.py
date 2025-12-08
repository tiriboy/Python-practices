import pyinputplus

def sum_10(string):
   digits = []
   try:
     for digit in string:
       digits.append(int(digit))
     if sum(digits) == 10:
       return 'Correct'
     return 'Incorrect'
   except:
       raise Exception('Invalid Input')
   
try:
  result = pyinputplus.inputCustom(sum_10,prompt='Enter a number whose digits add up to 10 (5 attempts): ', limit=5)
  print(result)       
except:
   print('Out of attempts')   
      
    
   
