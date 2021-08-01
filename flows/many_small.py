import time
from metaflow import FlowSpec, step, profile

class ManySmall(FlowSpec):
    """
    Test the baseline overhead of having many small artifacts
    """

    @step
    def start(self):
        nonce = str(time.time())
        self.x00 = nonce + '00'
        self.x01 = nonce + '01'
        self.x02 = nonce + '02'
        self.x03 = nonce + '03'
        self.x04 = nonce + '04'
        self.x05 = nonce + '05'
        self.x06 = nonce + '06'
        self.x07 = nonce + '07'
        self.x08 = nonce + '08'
        self.x09 = nonce + '09'
        self.x10 = nonce + '10'
        self.x11 = nonce + '11'
        self.x12 = nonce + '12'
        self.x13 = nonce + '13'
        self.x14 = nonce + '14'
        self.x15 = nonce + '15'
        self.x16 = nonce + '16'
        self.x17 = nonce + '17'
        self.x18 = nonce + '18'
        self.x19 = nonce + '19'
        self.x20 = nonce + '20'
        self.x21 = nonce + '21'
        self.x22 = nonce + '22'
        self.x23 = nonce + '23'
        self.x24 = nonce + '24'
        self.x25 = nonce + '25'
        self.x26 = nonce + '26'
        self.x27 = nonce + '27'
        self.x28 = nonce + '28'
        self.x29 = nonce + '29'
        self.next(self.end)

    @step
    def end(self):
        with profile('loading'):
            self.x00 += '00'
            self.x01 += '01'
            self.x02 += '02'
            self.x03 += '03'
            self.x04 += '04'
            self.x05 += '05'
            self.x06 += '06'
            self.x07 += '07'
            self.x08 += '08'
            self.x09 += '09'
            self.x10 += '10'
            self.x11 += '11'
            self.x12 += '12'
            self.x13 += '13'
            self.x14 += '14'
            self.x15 += '15'
            self.x16 += '16'
            self.x17 += '17'
            self.x18 += '18'
            self.x19 += '19'
            self.x20 += '20'
            self.x21 += '21'
            self.x22 += '22'
            self.x23 += '23'
            self.x24 += '24'
            self.x25 += '25'
            self.x26 += '26'
            self.x27 += '27'
            self.x28 += '28'
            self.x29 += '29'

if __name__ == '__main__':
    ManySmall()
