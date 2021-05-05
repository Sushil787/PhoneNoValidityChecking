
import phonenumbers
from phonenumbers import geocoder, carrier

PhoneNumber = phonenumbers.parse("+9779803394574")
ValidityCheck = phonenumbers.is_valid_number(PhoneNumber)
possible = phonenumbers.is_possible_number(PhoneNumber)
Carrier = carrier.name_for_number(PhoneNumber, 'en')
Region = geocoder.description_for_number(PhoneNumber, 'en')

print(Carrier)
print(Region)
print(ValidityCheck)
