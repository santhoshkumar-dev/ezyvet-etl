from pandas import read_csv, option_context, DataFrame
from sqlalchemy import create_engine

from com.ezyvet.util.formatter import format_title, capitalize_acronym, string_to_datetime, \
    prefix_phone_number_for_contact

db_engine = create_engine('mysql+pymysql://root:example@localhost/test')
contact_table_columns = ['id', 'title', 'first_name', 'last_name', 'company_name', 'date_of_birth', 'notes']
address_table_columns = ['id', 'contact_id', 'street1', 'street2', 'suburb', 'city', 'post_code']
phone_table_columns = ['id', 'contact_id', 'name', 'content', 'type']


class CustomerContacts:

    def __init__(self, all_contacts):
        self.all_contacts = all_contacts

    def contacts(self):
        contact = self.all_contacts.filter(
            ['id', 'Title', 'First Name', 'Last Name', 'Business', 'Date Of Birth', 'Notes'])
        contact['Title'] = contact['Title'].apply(format_title)
        contact['First Name'] = contact['First Name'].str.capitalize()
        contact['Last Name'] = contact['Last Name'].str.capitalize()
        contact['Business'] = contact['Business'].apply(capitalize_acronym)
        contact['Date Of Birth'] = contact['Date Of Birth'].apply(string_to_datetime)
        return contact

    def address(self):
        address = self.all_contacts.filter(['id', 'Address Line 1', 'Address Line 2', 'Suburb', 'City', 'Post Code'])
        address = address.rename(columns={"id": "contact_id"})
        # Not required but added only to differentiate from contact_id
        address['id'] = address.index + 100
        address = address[['id', 'contact_id', 'Address Line 1', 'Address Line 2', 'Suburb', 'City', 'Post Code']]
        return address

    def phone(self):
        new_columns = {"id": "contact_id", 'Home Number': 'home', 'Work Number': 'work', 'Mobile Number': 'mobile',
                       'Other Number': 'other'}
        phone_df = self.all_contacts.filter(['id', 'Home Number', 'Work Number', 'Mobile Number', 'Other Number'])
        phone_dict = phone_df.rename(columns=new_columns).to_dict('records')
        phones = DataFrame(self.__merge_phones(phone_dict))
        # Not required but added only to differentiate from contact_id
        phones['id'] = phones.index + 200
        phones = phones[['id', 'contact_id', 'name', 'content', 'type']]
        return phones

    @staticmethod
    def __merge_phones(phone_dict):
        all_phones = []

        for item in phone_dict:
            contact_id = item['contact_id']
            all_phones.append(prefix_phone_number_for_contact(contact_id, item['home'], 'Home', '09'))
            all_phones.append(prefix_phone_number_for_contact(contact_id, item['mobile'], 'Mobile', '64'))
            all_phones.append(prefix_phone_number_for_contact(contact_id, item['work'], 'Work', ''))
            all_phones.append(prefix_phone_number_for_contact(contact_id, item['other'], 'Other', ''))

        all_phones = [item for item in all_phones if item]
        return all_phones
