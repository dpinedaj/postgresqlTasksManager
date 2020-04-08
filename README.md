# postgresqlTasksManager

This repository has a task manager to create files in a folder with a file maker script, publish a task with the file names in a table on a postgresql database, a subscriptor (or many of them) takes the tasks from that table and execute his work... His work is to move that specific file from a folder to another one, and when the destiny folder is full, the file maker remove them to continue his work.
