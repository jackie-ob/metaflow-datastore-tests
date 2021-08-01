import time
from metaflow import Parameter, FlowSpec, step, profile

class CasHit(FlowSpec):
    """
    Run this flow twice with the same nonce.
    The second run should be faster as the artifacts
    exist in the CAS already.
    """

    nonce = Parameter('nonce')

    @step
    def start(self):
        self.x00 = self.nonce + 'x00' * (100*1024*1024)
        self.x01 = self.nonce + 'x01' * (100*1024*1024)
        self.x02 = self.nonce + 'x02' * (100*1024*1024)
        self.x03 = self.nonce + 'x03' * (100*1024*1024)
        self.x04 = self.nonce + 'x04' * (100*1024*1024)
        self.x05 = self.nonce + 'x05' * (100*1024*1024)
        self.x06 = self.nonce + 'x06' * (100*1024*1024)
        self.x07 = self.nonce + 'x07' * (100*1024*1024)
        self.x08 = self.nonce + 'x08' * (100*1024*1024)
        self.x09 = self.nonce + 'x09' * (100*1024*1024)
        self.x10 = self.nonce + 'x10' * (100*1024*1024)
        self.x11 = self.nonce + 'x11' * (100*1024*1024)
        self.x12 = self.nonce + 'x12' * (100*1024*1024)
        self.x13 = self.nonce + 'x13' * (100*1024*1024)
        self.x14 = self.nonce + 'x14' * (100*1024*1024)
        self.x15 = self.nonce + 'x15' * (100*1024*1024)
        self.x16 = self.nonce + 'x16' * (100*1024*1024)
        self.x17 = self.nonce + 'x17' * (100*1024*1024)
        self.x18 = self.nonce + 'x18' * (100*1024*1024)
        self.x19 = self.nonce + 'x19' * (100*1024*1024)
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            print(len(self.x00))
            print(len(self.x01))
            print(len(self.x02))
            print(len(self.x03))
            print(len(self.x04))
            print(len(self.x05))
            print(len(self.x06))
            print(len(self.x07))
            print(len(self.x08))
            print(len(self.x09))
            print(len(self.x10))
            print(len(self.x11))
            print(len(self.x12))
            print(len(self.x13))
            print(len(self.x14))
            print(len(self.x15))
            print(len(self.x16))
            print(len(self.x17))
            print(len(self.x18))
            print(len(self.x19))

if __name__ == '__main__':
    CasHit()
