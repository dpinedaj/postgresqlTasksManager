import sys
import os
import shutil
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.constants import Constants as cts
from modules.files import Files

class FileMaker:

    def __init__(self):
        self.constants = cts()
        self.files = Files()

    def fn_cleaner(self, ar_path):
        print('--Removing files from Destiny--')
        exitValue = fm.files.fn_remove_all(ar_path)
        if exitValue == fm.constants.OK:
            print('DONE')
            time.sleep(5)
        else:
            print('SOMETHING FAIL')
    
    def fn_file_maker(self, ar_path, n):
        name = '{}.txt'.format(n)
        exitValue = fm.files.fn_file_maker(originPath, name)
        if exitValue == fm.constants.OK:
            print('Created file: ', name)
        else:
            print('SOMETHING FAIL')

if __name__ == "__main__":
    
    fm = FileMaker()
    originPath = fm.constants.ORIGIN_PATH
    destinyPath = fm.constants.DESTINY_PATH
    os.makedirs(originPath, exist_ok=True)
    os.makedirs(destinyPath, exist_ok=True)

    n = 1
    try:
        while True:
            if fm.files.fn_get_len_path(destinyPath) >= fm.constants.ITER:
                fm.fn_cleaner(destinyPath)
            else:
                while fm.files.fn_get_len_path(originPath) < fm.constants.ITER :
                    fm.fn_file_maker(originPath, n)
                    n += 1
                else:
                    print('There\'s no space')
                    time.sleep(10)
    finally:
        shutil.rmtree(originPath)
        shutil.rmtree(destinyPath)


            