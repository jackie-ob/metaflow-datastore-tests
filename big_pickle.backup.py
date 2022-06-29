import time
from datetime import datetime
from metaflow import FlowSpec, step, profile

class BigPickle(FlowSpec):
    """
    Create a complex Python object to test (un)pickling overhead
    """

    @step
    def start(self):
        self.splits = range(30)
        nonce = str(time.time())
        # self.d should become a large pickled object
        self.d = {}
        lst = [(i, datetime.utcnow()) for i in range(10)]
        for i in range(100000):
            self.d[i] = {'%d %s' % (j, nonce): lst for j in range(100)}
        self.next(self.foreach, foreach='splits')

    @step
    def foreach(self):
        with profile('loading'):
            print(len(self.d))
        self.next(self.join)

    @step
    def join(self, inputs):
        self.d = inputs[0].d
        self.agg = [len(inp.d) for inp in inputs]
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            print(len(self.agg))

if __name__ == '__main__':
    BigPickle()
