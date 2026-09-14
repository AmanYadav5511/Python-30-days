#backup_before_write(filename) — if filename exists, 
#copy it to filename + '.bak' before any write happens (use shutil.copy()).
#Test on a file that exists and one that doesn't.
import os
import shutil

def backup_before_write(filename):
    if os.path.exists(filename):
        shutil.copy(filename, filename + '.bak')
        print('Backup created succesfully')
    else:
        print('No file found, no backup needed')

backup_before_write('aman.txt')
backup_before_write('notes.txt')