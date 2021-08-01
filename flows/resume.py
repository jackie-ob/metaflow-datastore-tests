import time
from metaflow import FlowSpec, step, profile

D = {'one': 1, 'two': 2, 'three': 3}

class ResumeFlow(FlowSpec):
    """
    Use this flow to test resuming across versions:
    Run with a version X, resume with Y and vice versa.
    """

    @step
    def start(self):
        self.d = D
        self.next(self.split)

    @step
    def split(self):
        self.splits = range(250)
        self.next(self.foreach, foreach='splits')

    @step
    def foreach(self):
        self.x = self.input
        self.next(self.join)

    @step
    def join(self, inputs):
        self.d = inputs[0].d
        self.agg = list(sorted(inp.x for inp in inputs))
        self.next(self.end)

    @step
    def end(self):
        if self.agg != list(range(250)):
            raise Exception("incorrect results: %s" % self.agg)
        if self.d != D:
            raise Exception("incorrect results: %s" % self.d)

if __name__ == '__main__':
    ResumeFlow()
