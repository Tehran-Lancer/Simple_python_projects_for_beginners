# pip install deep-translator 
from deep_translator import GoogleTranslator
codes = {
    'english': 'en',
    'persian': 'fa',
    'french': 'fr',
    'germany': 'de',
    'spanish': 'es',
    'italian': 'it',
    'russian': 'ru',
    'arabic': 'ar',
}
print ('wellcome to translator\n')
while True:
    text = input("enter text to translate: ")
    target_language = input("enter the language that you want to translate to : ").strip()
    if target_language in codes:
        TargetLanguageCode = codes[target_language]
        break
    else:
        print("something thing went wrong please try again")
try:
    TranslatedText = GoogleTranslator(source='auto', target=TargetLanguageCode).translate(text)
    print(f"translating : {TranslatedText}")
except Exception as e:
    print(f"you got this error: {e}")