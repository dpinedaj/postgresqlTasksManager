import sys
import os
import shutil
from .constants import Constants as cts

class Files:
    
    def __init__(self):
        self.constants = cts()

    def fn_file_maker(self, ar_path, ar_file):
        filePath = os.path.join(ar_path, ar_file)
        exitValue = None
        try:
            with open(filePath, 'w') as f:
                f.write(' ')
            exitValue = self.constants.OK

        except Exception as ex:
            print(str(ex))
            exitValue = self.constants.ERROR

        return exitValue

    def fn_get_list_path(self, ar_path):
        exitValue = None
        listPath = None
        try:
            listPath = os.listdir(ar_path)
            exitValue = self.constants.OK
        except Exception as ex:
            print(str(ex))
            exitValue = self.constants.ERROR
        
        return listPath, exitValue

    def fn_get_len_path(self, ar_path):
        listPath = None
        lenPath = None
        try:
            listPath = os.listdir(ar_path)
            lenPath = len(listPath)
            
        except Exception as ex:
            print(str(ex))

            lenPath = 0
        
        return lenPath


    def fn_move_file(self, ar_origin_path, ar_destiny_path, ar_file):
        exitValue = None

        originPath = os.path.join(ar_origin_path, ar_file)
        destinyPath = os.path.join(ar_destiny_path, ar_file)

        try:
            shutil.move(originPath, destinyPath)
            exitValue = self.constants.OK
        except Exception as ex:
            print(str(ex))
            exitValue = self.constants.ERROR

        return exitValue

    def fn_remove_file(self, ar_path, ar_file):
        exitValue = None

        filePath = os.path.join(ar_path, ar_file)
        try:
            os.remove(filePath)
            exitValue = self.constants.OK
        except Exception as ex:
            print(str(ex))
            exitValue = self.constants.ERROR

        return exitValue

    def fn_remove_all(self, ar_path):
        exitValue = None

        try:
            listPath = os.listdir(ar_path)
            for file in listPath:
                filePath = os.path.join(ar_path, file)
                os.remove(filePath)
            exitValue = self.constants.OK

        except Exception as ex:
            print(str(ex))
            exitValue = self.constants.ERROR
        
        return exitValue