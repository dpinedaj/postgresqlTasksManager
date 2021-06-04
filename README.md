# postgresqlTasksManager

This repository has a task manager to create files in a folder with a file maker script, publish a task with the file names in a table on a postgresql database, a subscriptor (or many of them) takes the tasks from that table and execute his work... His work is to move that specific file from a folder to another one, and when the destiny folder is full, the file maker remove them to continue his work.


Steps

1. $ docker-compose up
2. $ alembic upgrade head
3. $ python Scripts/fileMaker.py
4. $ python Scripts/publisher.py
5. $ python Scripts/subscriptor.py