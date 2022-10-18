import matlab.engine

class MLEngine():
    def __init__(self):
        self.eng = matlab.engine.start_matlab()
    