import time
from metaflow import FlowSpec, step, profile

class WideForeachLowEntropy(FlowSpec):
    """
    Test a wide foreach with low entropy artifacts
    """

    @step
    def start(self):
        self.splits = range(250)
        self.next(self.foreach, foreach='splits')

    @step
    def foreach(self):
        self.x = 'x' * 1000
        self.next(self.join)

    @step
    def join(self, inputs):
        self.agg = ','.join(inp.x for inp in inputs)
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            print(len(self.agg))

if __name__ == '__main__':
    WideForeachLowEntropy()
