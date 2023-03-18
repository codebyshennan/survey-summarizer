from googletrans import Translator


def translate_sentence(sentence):
    translator = Translator()
    return translator.translate(sentence, dest='en').text
    