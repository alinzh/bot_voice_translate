from googletrans import Translator
translator = Translator()
message = input()
result = translator.translate(message)
if result.src == 'en':
    result = translator.translate(message, dest='ru')
else:
    result = translator.translate(message, dest='en')
print(result.text)

