import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.constants import Constants as cts
from modules.files import Files

class FileMaker:

    def __init__(self):
        self.constants = cts()
        self.files = Files()

    def gen_initialize(self, ar_path):
        n = 0

        while True:
            n += 1
            name = '{}.txt'.format(n)
            self.files.fn_file_maker(ar_path, name)
            yield name
    

if __name__ == "__main__":
    
    fm = FileMaker()
    originPath = fm.constants.ORIGIN_PATH
    destinyPath = fm.constants.DESTINY_PATH
    n = 1
    while True:
        if fm.files.fn_get_len_path(destinyPath) >= fm.constants.ITER:
            print('--Removing files from Destiny--')
            exitValue = fm.files.fn_remove_all(destinyPath)
            if exitValue == fm.constants.OK:
                print('DONE')
                time.sleep(2)
            else:
                print('SOMETHING FAILS')

        else:
            while fm.files.fn_get_len_path(originPath) < fm.constants.ITER :
                name = '{}.txt'.format(n)
                n += 1
                fm.files.fn_file_maker(originPath, name)
                print('Created file: ', name)
            else:
                print('There\'s no space')
                time.sleep(10)

            