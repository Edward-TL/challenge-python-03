# Resolve the problem!!
import re
import os

def run():
    #Opening file
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    f = os.path.join(THIS_FOLDER, 'encoded.txt')
    with open(f, 'rt', encoding='utf-8') as encoded_file:
        content = encoded_file.read()

    #RegEx Pattern
    pattern = re.compile(r'[a-z]')
    
    #Extracting the marchs and storing as object
    x = re.findall(pattern, content)
    print(f'Object version: {x}')
    
    #Passinf to string
    str_x = ""
    for element in x:
        str_x = str_x + element
    print(f'String version: {str_x}')
    encoded_file.close()

if __name__ == '__main__':
    run()