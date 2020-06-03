import unittest
from datetime import datetime

from com.ezyvet.util.formatter import format_title, capitalize_acronym, string_to_datetime, get_number_from_string, \
    prefix_phone_number_for_contact


class FormatterTest(unittest.TestCase):
    """
        Formatter tests  - only sample tests, this can be expanded.
    """

    def test_format_title(self):
        self.assertEqual('Mrs', format_title('Mrs.'))

    def test_format_title_with_lower(self):
        self.assertEqual('Mr', format_title('mr.'))

    def test_with_a_string_containing_acronym_prefix(self):
        self.assertEqual('P.P.P pet product providers', capitalize_acronym('p.p.p pet product providers'))

    def test_with_a_string_containing_already_capitalized_acronym_prefix(self):
        self.assertEqual('A.N.Z.A.C Associates', capitalize_acronym('A.N.Z.A.C Associates'))

    def test_with_a_string_containing_no_acronym_prefix(self):
        self.assertEqual('Guide Dog Services', capitalize_acronym('Guide Dog Services'))

    def test_with_an_empty_string(self):
        self.assertEqual(None, capitalize_acronym(''))

    def test_string_to_datetime_with_a_datetime_string(self):
        self.assertEqual(datetime(1988, 9, 7, 0, 0), string_to_datetime('9/07/1988 0:00'))

    def test_string_to_datetime_with_a_partial_year_string(self):
        self.assertEqual(datetime(1969, 1, 13, 0, 0), string_to_datetime('1/13/69'))

    def test_string_to_datetime_with_empty_string(self):
        self.assertEqual(None, string_to_datetime(''))

    def test_get_number_from_string(self):
        self.assertEqual('095594886', get_number_from_string('09 559-4886'))

    def test_get_number_from_string_with_brackets(self):
        self.assertEqual('093828858', get_number_from_string('(09) 382-8858'))

    def test_prefix_phone_number_for_contact(self):
        self.assertEqual({'contact_id': '1', 'content': '095559462', 'name': 'Home', 'type': 'Home'},
                         prefix_phone_number_for_contact('1', '555 9462', 'Home', '09'))

    def test_prefix_phone_number_for_contact_with_already_prefixed_one(self):
        self.assertEqual({'contact_id': '1', 'content': '093828858', 'name': 'Work', 'type': 'Work'},
                         prefix_phone_number_for_contact('1', '(09) 382-8858', 'Work', '09'))


if __name__ == '__main__':
    unittest.main()
