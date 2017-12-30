
a = int(input("Enter the first input: "))
b = int(input("Enter the second input: "))

class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(self, *args):
        """ initialise the class """
        self.input = args
        self.output = None

    def logic(self):
        """ the intelligence to be performed """
        raise NotImplementedError



class AndGate(Gate):
    """ class representing AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]
        return self.output

class OrGate(Gate):
    """ class representing OR gate """

    def logic(self):
        self.output = self.input[0] or self.input[1]
        return self.output


class NotGate(Gate):
    """ class representing NOT gate """

    def logic(self):
        self.output = not self.input[0]
        return self.output


class NandGate(AndGate,NotGate):
    """ class representing Nand Gate """
    
    def logic(self):
    
        self.temp = AndGate.logic(self)
        Gate.__init__(self,self.temp)
        self.output = NotGate.logic(self)
        return self.output

x = NandGate(a,b).logic()

class NorGate(AndGate,NotGate):
    """ class representing Nor Gate """
    
    def logic(self):
        self.temp = OrGate.logic(self)
        Gate.__init__(self,self.temp)
        self.output = NotGate.logic(self)
        return self.output

y = NorGate(a,b).logic()

op = str(input('Choose the gate needed to be operated (na/no/nn): '))

if op == 'na':
    print(int(x))

elif op == 'no':
    print(int(y))
    
elif op == 'nn':
    print(int(x))
    print(int(y))

else:
    print('Invalid operation.')
