import time
from metaflow import Parameter, FlowSpec, step, profile

class ClientAPIFlow(FlowSpec):
    """
    Run this flow prior to ClientAPICheck. Use different
    versions for this flow and ClientAPICheck.
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
        pass

if __name__ == '__main__':
    ClientAPIFlow()
