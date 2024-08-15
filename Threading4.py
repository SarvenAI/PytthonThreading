import time
import random
import threading

class Device:
    def __init__(self):
        self.isRunning = True
        self.resistance = 0 
        self.start()

    def getResistance(self):
        return self.resistance
    
    def _generateResistance(self):
        while self.isRunning:
            self.resistance = 5 + random.random()
            time.sleep(0.1)

    def start(self):
        self._thread = threading.Thread(target=self._generateResistance)
        self._thread.start()

    def stop(self):
        self.isRunning = False

if __name__ == "__main__":
    DMM = Device()
    DMM.start()
    for x in range(10):
        print("Resistance measured : {}".format(DMM.getResistance()))
    DMM.stop()
