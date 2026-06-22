def check_valid_brackets(s):
   stack = []
   pairs = {
       ')' : '(',
       '}' : '{',
       ']' : '['
   }
   
   for ch in s:
       if ch in '({[':
           stack.append(ch)
       else:
           '''
           "If there is no opening bracket available, O
           R the opening bracket on top of the stack does not match the current closing bracket, 
           then the bracket sequence is invalid."
           '''
           
           if not stack or stack[-1] != pairs[ch]:
               return False
           stack.pop()
           
   return len(stack) == 0

print(check_valid_brackets("({[]})"))
            
            