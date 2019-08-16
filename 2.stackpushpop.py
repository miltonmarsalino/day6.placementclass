class stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True 
        else:
            return False
    def pop(self):
        if len(self.stack)<=0:
            return ("no element")
        else:
            return self.stack.pop()
s = stack()
ph ="m"
while ph=="m":
    inp = input("enter the value")
    s.push(inp)
    ph = input("enter the val")
print(s.pop())
    
