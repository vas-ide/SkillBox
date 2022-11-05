




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
