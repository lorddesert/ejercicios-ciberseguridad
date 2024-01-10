import os

def read_file(file_path):
  dirname = os.path.dirname(__file__)
  filename = os.path.join(dirname, f'{file_path}')

  return open(f'{filename}', 'rb').read()