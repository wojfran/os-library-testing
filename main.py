import os
import shutil

try:
    source_directory = 'input_directory'
    destination_directory = 'output_directory'

    for filename in os.listdir(source_directory):
        source = os.path.join(source_directory, filename)
        destination = os.path.join(destination_directory, filename)
        if filename.endswith('.txt'):
            shutil.copy(source, destination)
            print('copied', filename)

except FileNotFoundError:
    print('Oops, it seems that the directories were not found, do not worry though.\n'
          'I have created them in the working directory of the script.\n'
          'Simply paste all of the files and directories you want sort '
          'through in search of ".txt" files into the directory called "input_directory".\n'
          'The copied text files will appear in the other created directory called "output_directory.\n')
    cwd_path = os.getcwd()
    path_source = os.path.join(cwd_path, source_directory)
    path_destination = os.path.join(cwd_path, destination_directory)
    os.makedirs(path_source)
    os.makedirs(path_destination)