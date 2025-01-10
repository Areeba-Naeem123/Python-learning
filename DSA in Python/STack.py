class stack:
    def __init__(self):
        self.stack = []
    def validate(self,s):

        top=''
        for char in s:
            if char=='(':
                self.stack.append(char)
            elif char=='{':
                self.stack.append(char)
            elif char=='[':
                self.stack.append(char)
            elif char==')':
                if not stack :
                    return false 
                else:
                    top=self.stack[-1]
                    if top=='(':
                        self.stack.pop()
                    else :
                        return False
            elif char=='}':
                if not stack :
                    return false 
                else:
                    top=self.stack[-1]
                    if top=='{':
                        self.stack.pop()
                    else :
                        return False
            elif char==']':
                if not stack :
                    return false 
                else:
                    top=self.stack[-1]
                    if top=='[':
                        self.stack.pop()
                    else :
                        return False
        if not self.stack :
            return True
        else :
            return False
    
stack_=stack()
s="[{{{}}}"
print(stack_.validate(s))
         
            

                
                



    






