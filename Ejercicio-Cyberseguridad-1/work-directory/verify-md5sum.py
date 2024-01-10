import hashlib
from read_file_test import read_file

folder_path = "../PyJ Systems"

files_to_check = [
    [
         f'{folder_path}/copia.sh',
        '90965b0eb20e68b7d0b59accd2a3b4fd'
    ],
    [
         f'{folder_path}/log.txt',
        '0b29406e348cd5f17c2fd7b47b1012f9'
    ],
    [
         f'{folder_path}/pass.txt',
        '6d5e43a730490d75968279b6adbd79ec'
    ],
    [
         f'{folder_path}/plan-A.txt',
        '129ea0c67567301df1e1088c9069b946'
    ],
    [
         f'{folder_path}/plan-B.txt',
        '4e9878b1c28daf4305f17af5537f062a'
    ],
    [
         f'{folder_path}/script.py',
        '66bb9ec43660194bc066bd8b4d35b151'
    ]
]

def verify_files_md5sum(files):
    responses = []
    i = 0
    for file in files:
        print(i)
        current_hash = hashlib.md5(read_file(file[0])).hexdigest()
        if not (current_hash == file[1]):
            responses.append(f'The file {file[0]} has been compromised.\n\n original hash: {file[1]}\ncurrent hash: {current_hash}')
        i = i + 1

    for res in responses:
        print(res)

verify_files_md5sum(files_to_check)