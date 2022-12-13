import file_recording as f_r
import reading_a_file_1 as r_a_f_1


def dialog():

    print('===== Существующие форматы ВВОДА => ( .txt ), ( .json ), ( .csv ) <- -------\n')
    a = input('Выберете и введите формат файла ВВОДА c его именем\nпредварительно добавив его в '
              'директорию с программой (пример: file.jpg):\n')

    print('===== Существующие форматы ВЫВОДА => ( .json ), ( .txt ), ( .csv ) <- -------\n')
    b = input('Выберете и введите формат файла ВЫВОДА c его именем (пример: file.jpg):\n')

    return a, b


def logic(a, b):

    if a.split('.')[1] == 'txt':

        if b.split('.')[1] == 'json':
            f_r.write_json(b, r_a_f_1.read_txt(a))

        elif b.split('.')[1] == 'csv':
            f_r.write_csv(b, r_a_f_1.read_txt(a))

    elif a.split('.')[1] == 'json':      # 'phone_book_input.json

        if b.split('.')[1] == 'txt':
            f_r.write_txt(b, r_a_f_1.read_json(a))

        elif b.split('.')[1] == 'csv':
            f_r.write_csv(b, r_a_f_1.read_json(a))

    elif a.split('.')[1] == 'csv':      # 'phone_book_input.json

        if b.split('.')[1] == 'txt':
            f_r.write_txt(b, r_a_f_1.read_csv(a))

        elif b.split('.')[1] == 'json':
            f_r.write_json(b, r_a_f_1.read_csv(a))





