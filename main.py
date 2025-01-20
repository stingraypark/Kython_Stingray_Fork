# Import
import os
import subprocess
import traceback
import tempfile
import inquirer

from core import interpret_kpy_2_py, interpret_py_2_kpy, read_file, write_file, get_file_name

# Mode
question = [inquirer.List('mode',
                           message='모드를 선택해주세요',
                           choices=['.kpy 실행', '.kpy -> .py 변환', '.py -> .kpy 변환'])]

answer = inquirer.prompt(question)

# App
while True:
    # Mode selection
    if answer['mode'] == '.kpy 실행':
        file_path = input('\033[38;2;90;210;232m실행할 파일의 경로를 입력해주세요: \033[0m')
    else:
        file_path = input('\033[38;2;90;210;232m변환할 파일의 경로를 입력해주세요: \033[0m')

    # File validation
    if not os.path.exists(file_path):
        print('존재하지 않는 파일입니다.\n')
        break

    contents = read_file(file_path)

    # Run
    if answer['mode'] == '.kpy 실행':
        with tempfile.TemporaryDirectory() as temp_dir:
            # Convert .kpy to .py
            temp_py_path = os.path.join(temp_dir, 'temp.py')
            write_file(temp_py_path,
                       interpret_kpy_2_py(contents))

            try:
                print()
                subprocess.run(['python', temp_py_path], check=True)
            except subprocess.CalledProcessError as e:
                traceback.print_exc()

            break

    # Conversion
    if answer['mode'] == '.kpy -> .py 변환':
        # Convert .kpy to .py
        write_file(os.path.join('projects/', get_file_name(file_path) + '.py'),
                   interpret_kpy_2_py(contents))
        break
    else:
        # Convert .py to .kpy
        write_file(os.path.join('projects/', get_file_name(file_path) + '.kpy'),
                   interpret_py_2_kpy(contents))
        break

print()
input('<ENTER>를 눌러 종료')