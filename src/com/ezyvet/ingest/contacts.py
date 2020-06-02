from pandas import read_csv, option_context
from sqlalchemy import create_engine

from com.ezyvet.util.formatter import format_title, capitalize_acronym, string_to_datetime

db_engine = create_engine('mysql+pymysql://root:example@localhost/test')
contact_table_columns = ['id', 'title', 'first_name', 'last_name', 'company_name', 'date_of_birth', 'notes']
address_table_columns = ['id', 'contact_id', 'street1', 'street2', 'suburb', 'city', 'post_code']


class CustomerContacts:

    def __init__(self, all_contacts):
        self.all_contacts = all_contacts

    def contacts(self):
        contact = self.all_contacts.filter(['id', 'Title', 'First Name', 'Last Name', 'Business', 'Date Of Birth', 'Notes'])
        contact['Title'] = contact['Title'].apply(format_title)
        contact['First Name'] = contact['First Name'].str.capitalize()
        contact['Last Name'] = contact['Last Name'].str.capitalize()
        contact['Business'] = contact['Business'].apply(capitalize_acronym)
        contact['Date Of Birth'] = contact['Date Of Birth'].apply(string_to_datetime)
        return contact

    def address(self):
        address = self.all_contacts.filter(['id', 'Address Line 1', 'Address Line 2', 'Suburb', 'City', 'Post Code'])
        address = address.rename(columns={"id": "contact_id"})
        address['id'] = address.index + 1
        address = address[['id', 'contact_id', 'Address Line 1', 'Address Line 2', 'Suburb', 'City', 'Post Code']]
        return address


if __name__ == '__main__':
    input_contacts = read_csv('/home/santhosh/PycharmProjects/ezyvet-etl/input/contact_list.csv', na_filter=False)
    input_contacts['id'] = input_contacts.index + 1
    customer_contact = CustomerContacts(input_contacts)

    contacts = customer_contact.contacts()
    contact_address = customer_contact.address()

    db_connection = db_engine.connect()

    contacts. \
        rename(columns=dict(zip(contacts.columns, contact_table_columns))). \
        to_sql('contact', db_connection, index=False, if_exists='append')

    contact_address.\
        rename(columns=dict(zip(contact_address.columns, address_table_columns))).\
        to_sql('address', db_connection, index=False, if_exists='append')

    with option_context('display.max_rows', None, 'display.max_columns', None):
        print(input_contacts)