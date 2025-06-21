from translate import Translator

translate = Translator(to_lang='en')
try:    
   with open('./sameer.txt', 'r+') as my_file:
    my_text = my_file.read()
    translation = translate.translate(my_text)

    with open('translated.txt', 'w') as new_file:
       new_file.write(translation)
    # print(my_file.read())

except FileNotFoundError as err:
    print('file not found')