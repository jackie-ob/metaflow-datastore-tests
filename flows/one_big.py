import time
from metaflow import FlowSpec, step, profile

class OneBig(FlowSpec):
    """
    Test the overhead of storing one big, low-entropy artifact.
    """

    @step
    def start(self):
        nonce = str(time.time()).encode('ascii')
        self.x = nonce + b'x' * (1024*1024*1024)
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            print(len(self.x))

if __name__ == '__main__':
    OneBig()
