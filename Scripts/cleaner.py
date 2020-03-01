import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.constants import Constants as cts
from modules.files import Files

class Cleaner:

    def __init__(self):
        self.files = Files()
        self.cts = cts()

    def cleaner(self, ar_path):
        exitValue = self.files.fn_remove_all(cts.DESTINY_PATH)
        return exitValue


if __name__ == "__main__":
    cln = Cleaner()
    while True:
        if cln.files.fn_get_len_path(cts.DESTINY_PATH) >= cln.cts.ITER:
            exitValue = cln.cleaner(cln.cts.DESTINY_PATH)
            if exitValue == cln.cts.OK:
                print('---CLEANED---')
        else:
            print('----NOT YET-----')
            time.sleep(15)
        