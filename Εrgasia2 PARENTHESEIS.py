def Par(par):

  stack = []
  push = "({["
  pop = ")}]"

  for ch in par :

    if ch in push:
      stack.append(ch)

    elif ch in pop:

    	if len(stack) != 0 :
    		top = stack.pop()
        	br = push[pop.index(ch)]
        if top != br:
          return False
    else:
    	return False
  return len(stack) == 0

if __name__ == '__main__':
 par = raw_input('Enter the parenthesis:\n')
 print Par(par)