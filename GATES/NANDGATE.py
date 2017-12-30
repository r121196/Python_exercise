# NAND GATE


class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(bit, *args):
        """ initialise the class """
        bit.input = args
        bit.output = None

    def logic(bit):
        """ the intelligence to be performed """
        raise NotImplementedError

    def output(bit):
        """ the output of the gate """
        bit.logic()
        return bit.output

a = int(input("Enter the first input: "))
b = int(input("Enter the second input: "))
class AndGate(Gate):
    """ class representing AND gate """

    def logic(bit):
        bit.output = bit.input[0] and bit.input[1]
        return bit.output

class NotGate(Gate):
    """ class representing NOT gate """

    def logic(bit):
        bit.output = not bit.input[0]
        return bit.output


class NandGate(AndGate,NotGate):
    """ class representing Nand Gate """
    
    def logic(bit):
       bit.store = AndGate.logic(bit)
       Gate.__init__(bit,bit.store)
       bit.output = NotGate.logic(bit)
       return bit.output

n = NandGate(a,b).logic()
print(int(n))

