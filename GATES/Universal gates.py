
print('na = NAND GATE, no = NOR GATE, nn = BOTH GATES ')
op = str(input('Choose the gate needed to be operated (na/no/nn): '))

a = int(input("Enter the first input: "))
b = int(input("Enter the second input: "))

class Gate(object):
    """ class representing a gate. It can be any gate. """

    def __init__(bit, *args):
        """ initialise the class """
        bit.input = args
        bit.output = None

    def logic(bit):
        """ the intelligence to be performed """
        raise NotImplementedError



class AndGate(Gate):
    """ class representing AND gate """

    def logic(bit):
        bit.output = bit.input[0] and bit.input[1]
        return bit.output

class OrGate(Gate):
    """ class representing OR gate """

    def logic(bit):
        bit.output = bit.input[0] or bit.input[1]
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

x = NandGate(a,b).logic()

class NorGate(AndGate,NotGate):
    """ class representing Nor Gate """
    
    def logic(bit):
        bit.store = OrGate.logic(bit)
        Gate.__init__(bit,bit.store)
        bit.output = NotGate.logic(bit)
        return bit.output

y = NorGate(a,b).logic()

if op == 'na':
    print(int(x))

elif op == 'no':
    print(int(y))
    
elif op == 'nn':
    print(int(x))
    print(int(y))

else:
    print('Invalid operation.')
