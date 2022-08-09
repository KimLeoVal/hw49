from django.core.exceptions import ValidationError

from accounts.forms import MyUserCreationForm
from webapp.models import STATUSES

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

def check_count(list):
    if len(list) > 3:
        raise ValidationError(f'Values "type" cannot be more than 3')

def check_status(status):
    list_st = []
    for i in STATUSES:
        list_st.append(i[0])
    list_st = (', ').join(list_st)
    if status in STATUSES:
        raise ValidationError(f'"status" value must be "{list_st}". ')







