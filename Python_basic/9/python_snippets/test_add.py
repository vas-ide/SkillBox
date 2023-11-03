import os
import time


class InOutBlock:

    def __enter__(self):
        print('Входим в блок кода')
        # TODO обратите внимание что тут надо вернуть обьект - в видео это пропущено
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Выходим из блока кода')

    def some_method(self):
        print('Выполяем метод обьекта InOutBlock')


with InOutBlock() as in_out:
    # in_out = InOutBlock()
    print('Некоторый код')
    in_out.some_method()


path = '//sessions/VAS-IDE/Documents'
path_normalized = os.path.normpath(path)
counter = 0
# Пройтись по всем файлам в директории.
for dirpath, dirnames, filenames in os.walk(path_normalized):
    # print(dirpath, dirnames, filenames)
    counter += len(filenames)
    for file in filenames:
        full_file_path = dirpath + '/' + file
        secs = os.path.getctime(full_file_path)
        file_time = time.gmtime(secs)
        if file_time[0] == 2022:
            print(full_file_path,
                  # secs,
                  file_time)
print(f"{counter}\n{__file__}\n{os.path.dirname(__file__)}")