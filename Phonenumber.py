import phonenumbers
number = input("Please enter the phone number with country code: ")

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number , "CH")
print("The origin of the phone number is: ")
print(geocoder.description_for_number(ch_number , "en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(number , "RO")
print("The service provider of your number is: ")
print(carrier.name_for_number(service_provider , "en"))
print("hello world")
