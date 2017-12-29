# NAND GATE


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

a = int(input("Enter the first input: "))
b = int(input("Enter the second input: "))
class AndGate(Gate):
    """ class representing AND gate """

    def logic(self):
        self.output = self.input[0] and self.input[1]
        return self.output

class NotGate(Gate):
    """ class representing NOT gate """

    def logic(self):
        self.output = not self.input[0]
        return self.output


class NandGate(AndGate,NotGate):
    #class representing Nand Gate
    
   def logic(self):
       self.temp = AndGate.logic(self)
       Gate.__init__(self,self.temp)
       self.output = NotGate.logic(self)
       return self.output

n = NandGate(a,b).logic()
print(int(n))
