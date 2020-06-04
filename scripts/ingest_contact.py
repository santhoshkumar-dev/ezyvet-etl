#!/usr/bin/env python
import argparse

from pandas import read_csv
from sqlalchemy import create_engine

from com.ezyvet.contacts import CustomerContactsBuilder

contact_table_columns = ['id', 'title', 'first_name', 'last_name', 'company_name', 'date_of_birth', 'notes']
address_table_columns = ['id', 'contact_id', 'street1', 'street2', 'suburb', 'city', 'post_code']


def main(input_file):
    input_contacts = read_csv(input_file, na_filter=False)
    input_contacts['id'] = input_contacts.index + 1
    customer_contact = CustomerContactsBuilder(input_contacts)

    contacts = customer_contact.contacts()
    contact_address = customer_contact.address()
    contact_phone = customer_contact.phone()

    db_engine = create_engine('mysql+pymysql://root:example@localhost/test')
    db_connection = db_engine.connect()
    print("Starting to ingest contact, address, phone")
    contacts. \
        rename(columns=dict(zip(contacts.columns, contact_table_columns))). \
        to_sql('contact', db_connection, index=False, if_exists='append')

    contact_address. \
        rename(columns=dict(zip(contact_address.columns, address_table_columns))). \
        to_sql('address', db_connection, index=False, if_exists='append')

    contact_phone.to_sql('phone', db_connection, index=False, if_exists='append')
    print("Finished ingesting contact, address, phone")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingests input contacts file into local mysql database')
    parser.add_argument('input_file', help='path to the input contacts csv file')
    args = parser.parse_args()
    main(args.input_file)
