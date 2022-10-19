import matlab.engine

class MLEngine():
    def __init__(self):
        self.eng = matlab.engine.start_matlab()

    def createNeuron(self, cell, type):
        neuron = self.eng.Neuron(cell,type)
        return neuron

    def nodes(self,neuron):
        nodes = self.eng.getfield(neuron, 'nodes')
   
        id = self.eng.getfield(nodes,'ID')
        posx = self.eng.getfield(nodes,'X')
        posy = self.eng.getfield(nodes,'Y')
        posz = self.eng.getfield(nodes,'Z')

        neuronData = []
        for i in range(len(posx)):
            neuronData.append((id,posx[i][0],posy[i][0],posz[i][0]))

        return neuronData
