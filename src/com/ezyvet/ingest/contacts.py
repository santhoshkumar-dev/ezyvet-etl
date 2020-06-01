from pandas import read_csv, option_context

contacts = read_csv("/home/santhosh/PycharmProjects/ezyvet-etl/input/contact_list.csv")

with option_context('display.max_rows', None, 'display.max_columns', None):
    print(contacts)
