#NORGATE


class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(self, *args):
        """ initialise the class """
        self.input = args
        self.output = None

    def logic(self):
        """ the intelligence to be performed """
        raise NotImplementedError

    def output(self):
        """ the output of the gate """
        self.logic()
        return self.output

a= int(input('Enter the first input bit: '))
b = (int(input('Enter the second input bit: ')))
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


class NorGate(OrGate,NotGate):
    """class representing Nor Gate"""
    
    def logic(self):
       self.temp = OrGate.logic(self)
       Gate.__init__(self,self.temp)
       self.output = NotGate.logic(self)
       return self.output

n = NorGate(a,b).logic()
print(int(n))

