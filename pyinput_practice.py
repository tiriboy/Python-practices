import pyinputplus

def sum_10(string):
   digits = []
   try:
     for digit in string:
       digits.append(int(digit))
     if sum(digits) == 10:
       return 'Correct'
     raise Exception('Sum is not 10')
   except Exception as e:
       raise Exception(str(e))
   
try:
  result = pyinputplus.inputCustom(sum_10,prompt='Enter a number whose digits add up to 10 (5 attempts): ', limit=5)
  print(result)       
except:
   print('Out of attempts')   
      
    
   
