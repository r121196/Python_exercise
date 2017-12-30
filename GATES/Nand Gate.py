# Nand Gate

n = True
next_output = True
def start() :

        class Gate:
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
            return self.logic()

        a = int(input('enter the first no: '))
        b = int(input('enter the sevon no: '))

        
        class AndGate(Gate):
            """ class representing AND gate """

            def logic(self):
                
                self.output = self.input[a] and self.input[b]
                return self.output

        class NotGate(Gate):
            """ class representing NOT gate """

            def logic(self):
                self.output = not self.input[0]
                return self.output

        class NandGate(Gate):
            def logic(self):
                anded = AndGate(self.input).logic() # calculate the and'd values
                notted = NotGate(anded).logic() # not them
                return notted
                
        print (int(n))


while next_output :
    start()
