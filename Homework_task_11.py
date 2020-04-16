import requests
import os.path
import wget
import os


API_KEY = 'trnsl.1.1.20200416T085746Z.896eacde732b4ea4.4be4e3a63a09e1253507d8744142224f3f1687e7'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

check=input('Программа работет при отсутствии файлов для первоначального перевода в папке проекта, загружая их из Github.\n'
            'В случае, если файлы DE.txt, ES.txt или FR.txt присутствуют в директории проекта - они будут удалены, и перевод будет производиться именно тех файлов, которые присутствуют на Github.\n'
            'В конце работы программы будет предложено удалить только что скаченные файлы, чтобы оставить только файл программы и финальный текстовый файл.\n'
            'Нажмите Enter для продолжения работы программы')
if check == ():
    pass


#this try/except cycle below is deliting an existed files in case they are already in the directory of the project, because the program downloads them from the github directly.
try:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'DE.txt')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ES.txt')
    os.remove(path)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'FR.txt')
    os.remove(path)
except FileNotFoundError:
    pass


def translate_it(text, to_lang):

    to_lang='ru'
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-''{}'.format(lang, to_lang),
        'reason': 'auto',
        'format': 'text'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    # print(json_)
    return ''.join(json_['text'])

try:
    if __name__ == '__main__':
        desirednamefile=input('Придумайте имя файлу, который будет содержать текстовые переводы всех текстов ')
        print('Подождите, пока совершается перевод и формирование финального файла...')
        desirednamefile_txt=(desirednamefile+'.txt')
        # print (desirednamefile_txt)
        def german_translate():
            germantext_url = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/3.2.http.requests/DE.txt'
            german_text_downloaded = wget.download(germantext_url)
            with open (german_text_downloaded) as file_to_translate:
                german_lang=(file_to_translate.name.split('.')[0].lower())
                # print(lang)
                global lang
                lang=german_lang #checking language

                with open('DE.txt', 'r') as f:
                    oldtext = f.read()
                newtext = oldtext.replace('\n\n', '\n')
                with open('subs.txt', 'w') as f:
                    f.write(newtext)
                # print(newtext)

                german_translate=(translate_it(newtext, lang))
                german_translation_final = (f'Перевод немецкого текста:\n\n{german_translate}\n')
                # print(german_translation_final)
                with open(desirednamefile_txt,'w') as final_translation:
                    final_translation.write(german_translation_final)
        german_translate()

        def spanish_translate():
            spanishtext_url = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/3.2.http.requests/ES.txt'
            spanish_text_downloaded = wget.download(spanishtext_url)
            with open (spanish_text_downloaded) as file_to_translate:
                espanian_lang=(file_to_translate.name.split('.')[0].lower())
                # print(espanian_lang)
                global lang
                lang=espanian_lang #checking language
                # print(lang)
                espanian_text = file_to_translate.read()
                # print(espanian_text)
                spanish_translate=(translate_it(espanian_text, lang))
                spanish_translation_final=(f'Перевод испанского текста:\n\n{spanish_translate}\n')
                with open (desirednamefile_txt, 'a') as final_translation:
                    final_translation.write(spanish_translation_final)
                # print(spanish_translate)
        spanish_translate()

        def french_translate():
            frenchtext_url = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/3.2.http.requests/FR.txt'
            french_text_downloaded = wget.download(frenchtext_url)
            with open (french_text_downloaded) as file_to_translate:
                french_lang=(file_to_translate.name.split('.')[0].lower())
                # print (french_lang)
                global lang
                lang=french_lang #checking language
                # print(lang)

                with open('FR.txt', 'r') as f:
                    oldtext = f.read()
                newtext = oldtext.replace('\n\n', '\n')
                with open('subs.txt', 'w') as f:
                    f.write(newtext)
                # print(newtext)
                french_translate=(translate_it(newtext, lang))
                french_translation_final = (f'\nПеревод французского текста:\n\n{french_translate}\n')
                with open (desirednamefile_txt,'a') as final_translation:
                    final_translation.write(french_translation_final)
                # print(french_translate)

        french_translate()

        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'subs.txt') #I don't know what is "subs.txt" but it appears every time, I prefer delete it
        os.remove(path)

        def deleting():
            deleting_answer= input('Хотели бы вы оставить скаченные только что текстовые файлы для переводов в папке проекта? Да/Нет ')
            if deleting_answer == 'Нет':
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'DE.txt')
                os.remove(path)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ES.txt')
                os.remove(path)
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'FR.txt')
                os.remove(path)
            else:
                pass
        deleting()
    final_directory=os.path.abspath(desirednamefile_txt)
    print(f'По результатам работы программы был сформирован файл {desirednamefile_txt}, который располагается в директории {final_directory}, т.е. в рабочей папке проекта с данной программой.')
    view_file=input('Хотели бы Вы вывести результаты работы программы? Да/Нет ')
    if view_file=='Да':
        print()
        with open(desirednamefile_txt) as final_file:
            for line in final_file:
                print(line,end='')
    else:
        pass
except KeyError:
    print ('Файлы с текстами для перевода уже существовали в вашей директории до запуска работы программы.\nПросьба удалить все изначальные данные переводов из папки проекта данной программы, затем запустить её заново')