**ezyVet Data Engineer Test**


**Objective:**
Write a simple script to pipe data from the attached CSV into the MySQL tables provided

**Supplied:**

CSV should be attached inside ZIP

Database tables provided

**Requirements:**
- All data from the CSV must be processed into the provided tables
- Data must be sanitized to be safely inserted
- Data must be consistent when exported as is when imported
- First and Last names must have the first letter capitalized
- Business Names must have acronyms be capitalized
- Mobile numbers must have a 64 prefixed
- Landline numbers must have 09 prefixed
- The `contact_id` field in the address and phone tables must match to an existing record
with the same value in the `id` field of the contact table
- You can use any language for any code that is written. Preferably use PHP 7.0 where
possible
- MySQL 5.7 is to be used