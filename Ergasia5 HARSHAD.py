hashadArray = []

def looping(counter):
  for n in range(1,counter):
    hashadTest(n)
    hashadMult(n)
  return hashadArray

def Tokenizer(integer):
  stringInt = str(integer)
  intArray = list(stringInt)
  return intArray

def sum(charArray):
  sum = 0
  for char in charArray:
    sum += int(char)
  return sum
  
def multiplier(charArray):
  sum = 1
  for characher in charArray:
    sum *= int(characher)
  return sum

def hashadTest(integer):
  stringInt = Tokenizer(integer)
  if integer % sum(stringInt) == 0:
    hashadArray.append(integer)
  return hashadArray
  
def hashadMult(integer):
  stringInt = Tokenizer(integer)
  try:
    if integer % multiplier(stringInt) != 0:
      hashadArray.remove(integer)
  except Exception:
    pass
  return hashadArray
  

print looping(1000)