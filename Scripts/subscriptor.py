
import os
import sys
import time
from datetime import datetime
from datetime import timedelta

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.tasksManager import TaskManager
from modules.files import Files
from modules.constants import Constants as cts
from modules.db_session import session

if __name__ == '__main__':
    fls = Files()
    cts = cts()
    n=0
    while True:
        task = TaskManager.next()
        if not task:
            print('---No tasks to execute---')
            time.sleep(5)
        else:
            try:
                exitValue = fls.fn_move_file(cts.ORIGIN_PATH, cts.DESTINY_PATH, task.file_name)
                
            except Exception as ex:
                task.failed(ex)

            if (task.error is None or task.error == ' ') and (exitValue == cts.OK):
                n+=1
                task.destroy()
                print('completed work {}'.format(n))