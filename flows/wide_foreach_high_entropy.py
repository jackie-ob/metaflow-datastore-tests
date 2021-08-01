import secrets
from metaflow import FlowSpec, step, profile

class WideForeachHighEntropy(FlowSpec):
    """
    Test a wide foreach with high-entropy artifacts.
    """

    @step
    def start(self):
        self.splits = range(250)
        self.next(self.foreach, foreach='splits')

    @step
    def foreach(self):
        self.x = secrets.token_bytes(10_000_000)
        self.next(self.join)

    @step
    def join(self, inputs):
        self.agg = b','.join(inp.x for inp in inputs)
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            print(len(self.agg))

if __name__ == '__main__':
    WideForeachHighEntropy()
