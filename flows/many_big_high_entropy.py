import secrets
from metaflow import FlowSpec, step, profile

class ManyBigHighEntropy(FlowSpec):
    """
    Test compression overhead by with high-entropy artifacts
    """

    @step
    def start(self):
        self.x00 = secrets.token_bytes(100_000_000)
        self.x01 = secrets.token_bytes(100_000_000)
        self.x02 = secrets.token_bytes(100_000_000)
        self.x03 = secrets.token_bytes(100_000_000)
        self.x04 = secrets.token_bytes(100_000_000)
        self.x05 = secrets.token_bytes(100_000_000)
        self.x06 = secrets.token_bytes(100_000_000)
        self.x07 = secrets.token_bytes(100_000_000)
        self.x08 = secrets.token_bytes(100_000_000)
        self.x09 = secrets.token_bytes(100_000_000)
        self.x10 = secrets.token_bytes(100_000_000)
        self.x11 = secrets.token_bytes(100_000_000)
        self.x12 = secrets.token_bytes(100_000_000)
        self.x13 = secrets.token_bytes(100_000_000)
        self.x14 = secrets.token_bytes(100_000_000)
        self.x15 = secrets.token_bytes(100_000_000)
        self.x16 = secrets.token_bytes(100_000_000)
        self.x17 = secrets.token_bytes(100_000_000)
        self.x18 = secrets.token_bytes(100_000_000)
        self.x19 = secrets.token_bytes(100_000_000)
        self.x20 = secrets.token_bytes(100_000_000)
        self.x21 = secrets.token_bytes(100_000_000)
        self.x22 = secrets.token_bytes(100_000_000)
        self.x23 = secrets.token_bytes(100_000_000)
        self.x24 = secrets.token_bytes(100_000_000)
        self.x25 = secrets.token_bytes(100_000_000)
        self.x26 = secrets.token_bytes(100_000_000)
        self.x27 = secrets.token_bytes(100_000_000)
        self.x28 = secrets.token_bytes(100_000_000)
        self.x29 = secrets.token_bytes(100_000_000)
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            self.x00 += b'00'
            self.x01 += b'01'
            self.x02 += b'02'
            self.x03 += b'03'
            self.x04 += b'04'
            self.x05 += b'05'
            self.x06 += b'06'
            self.x07 += b'07'
            self.x08 += b'08'
            self.x09 += b'09'
            self.x10 += b'10'
            self.x11 += b'11'
            self.x12 += b'12'
            self.x13 += b'13'
            self.x14 += b'14'
            self.x15 += b'15'
            self.x16 += b'16'
            self.x17 += b'17'
            self.x18 += b'18'
            self.x19 += b'19'
            self.x20 += b'20'
            self.x21 += b'21'
            self.x22 += b'22'
            self.x23 += b'23'
            self.x24 += b'24'
            self.x25 += b'25'
            self.x26 += b'26'
            self.x27 += b'27'
            self.x28 += b'28'
            self.x29 += b'29'

if __name__ == '__main__':
    ManyBigHighEntropy()
