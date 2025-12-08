import pyinputplus

def keep_idiot_busy(string):
   if string == 'No' or string == 'no':
      return 'Ur smart'
   else:
      raise Exception

result = pyinputplus.inputCustom(keep_idiot_busy, prompt='Want to know how to keep and idiot busy? Type yes: ')
print(result)   