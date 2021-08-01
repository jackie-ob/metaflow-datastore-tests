from metaflow import FlowSpec, step

class ManyNoop(FlowSpec):
    """
    Test the baseline latency of executing many no-op steps.
    """

    @step
    def start(self):
        self.next(self.x0)

    @step
    def x0(self):
        self.next(self.x1)

    @step
    def x1(self):
        self.next(self.x2)

    @step
    def x2(self):
        self.next(self.x3)

    @step
    def x3(self):
        self.next(self.x4)

    @step
    def x4(self):
        self.next(self.x5)

    @step
    def x5(self):
        self.next(self.x6)

    @step
    def x6(self):
        self.next(self.x7)

    @step
    def x7(self):
        self.next(self.x8)

    @step
    def x8(self):
        self.next(self.x9)

    @step
    def x9(self):
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    ManyNoop()
