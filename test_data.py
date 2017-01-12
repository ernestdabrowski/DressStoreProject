"""
there is a place for all test data which will be used in specific test cases
"""
from random import choice
from string import ascii_uppercase

first_part = (''.join(choice(ascii_uppercase) for i in range(6)))
email_address = (first_part + "@gmail.com")


AccountData = dict(email = email_address,
                   name = "Ernest",
                   last_name = "Dabrowski",
                   password = "123456",
                   company = "XYZ",
                   address = "MainStreet",
                   city = "New York",
                   state_value = "32",
                   country_value = "21",
                   postal = "12345",
                   phone = "678345123",
                   alias_email = "testbls2@yahoo.com")

DressOrderData = dict(email = "testbls@yahoo.com",
                      password = "123456")








