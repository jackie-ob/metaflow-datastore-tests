import time
from metaflow import Run, Parameter, FlowSpec, step, profile

class ClientAPICheck(FlowSpec):
    """
    Run ClientAPIFlow before this flow. Supply its run id and the nonce used parameters.
    This flow uses the Client API to fetch and validate its results.
    """

    nonce = Parameter('nonce')
    run_id = Parameter('run-id', default=0)

    @step
    def start(self):
        run = Run('ClientAPIFlow/%d' % self.run_id)
        # fetch artifacts a few times to exercise the client cache
        for n in range(3):
            with profile('assert artifacts (iter %d)' % n):
                for i in range(20):
                    key = 'x%.2d' % i
                    x = run['start'].task[key].data
                    expect = self.nonce + key * (100*1024*1024)
                    if x != expect:
                        raise Exception("unexpected %dth artifact" % i)
        self.next(self.end)

    @step
    def end(self):
        # the client cache should persist across steps when running locally
        run = Run('ClientAPIFlow/%d' % self.run_id)
        with profile('load artifacts'):
            for i in range(20):
                key = 'x%.2d' % i
                x = run['start'].task[key].data

if __name__ == '__main__':
    ClientAPICheck()
