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
            logging.info(f'No valid date format found for {text}')
    return None


def get_number_from_string(text):
    pattern = r'\d+'
    business_name = re.findall(pattern, str(text))
    return ''.join(business_name)


def prefix_phone_number_for_contact(contact_id, phone_number, phone_type, prefix):
    phone_number = get_number_from_string(phone_number)
    possible_prefix = ('09', '64')

    if phone_number.startswith(possible_prefix):
        return {'contact_id': contact_id, 'name': phone_type, 'content': phone_number, 'type': phone_type}
    elif phone_number and phone_type in ('Mobile', 'Home'):
        return {'contact_id': contact_id, 'name': phone_type, 'content': prefix + phone_number, 'type': phone_type}
    elif len(phone_number) == 7:
        return {'contact_id': contact_id, 'name': phone_type, 'content': '09' + phone_number, 'type': phone_type}
    elif phone_number:
        return {'contact_id': contact_id, 'name': phone_type, 'content': '64' + phone_number, 'type': phone_type}
