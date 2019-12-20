import os
import sys

from app import script

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.abspath(__file__))
    try:
        src_path, tgt_path, changes_path = sys.argv[1:]
    except ValueError:
        src_path = current_path + input('Enter source backup folder path: ')
        tgt_path = current_path + input('Enter target backup folder path: ')
        changes_path = current_path + input('Enter folder path where changes will be stored: ')
    else:
        src_path = current_path + src_path
        tgt_path = current_path + tgt_path
        changes_path = current_path + changes_path
    script.compare_backups(src_path, tgt_path, changes_path)

