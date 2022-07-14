from django.core.exceptions import ValidationError

SP_CHARS = ['!','@','#','$']
SP_WORDS = ['kill','bomb', 'terrorist', 'president']
def special_chars(name):
    for i in SP_CHARS:
        if i in name:
            raise ValidationError(f'Title must not contain "{i}". Forbidden symbols{SP_CHARS}')


def special_words(text):
    for i in SP_WORDS:
        if i.lower() in text.lower():
            raise ValidationError(f'Description must not contain "{i}!!!!!!". Forbidden words{SP_WORDS}')
