import os
import sys
import random
from os import path
import time
from tqdm import tqdm

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.tasksManager import TaskManager
from modules.files import Files
from modules.constants import Constants as cts
from modules.db_session import session


if __name__ == '__main__':
    
    cts = cts()
    files = Files()
    iters = cts.ITER
    doneList = list()
    while True:
        
        try:
            filesList = sorted(files.fn_get_list_path(cts.ORIGIN_PATH)[0])
            fileName = random.choice(filesList)
            id = fileName.split('.')[0]
            if id not in doneList:
                taskManager = TaskManager(
                    id=id,
                    file_name=fileName,
                    fails=False,
                    processing=False,   
                    error = ' '
                )
                session.add(taskManager)
                print('added file name:', fileName)
                doneList.append(id)
                session.commit()

        except Exception as exc:
            print(str(exc))
            time.sleep(5)
            continue