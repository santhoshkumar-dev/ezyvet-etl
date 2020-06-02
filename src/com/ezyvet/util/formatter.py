import logging
import re
from datetime import datetime


def format_title(text):
    return str(text).strip('.').capitalize()


def capitalize_acronym(text):
    pattern = r'(?:[a-zA-Z.])+'
    business_name = re.findall(pattern, text)
    if business_name:
        first_word = str(business_name[0])
        business_name[0] = first_word.upper() if '.' in first_word else first_word
        result = ' '.join(business_name[0:])
        return result


def string_to_datetime(text):
    dob = text.split(" ")[0]
    for fmt in ('%m/%d/%Y', '%m/%d/%y'):
        try:
            return datetime.strptime(dob, fmt)
        except ValueError:
            logging.info(f'Cannot format date {text} using {fmt}')
    return None
