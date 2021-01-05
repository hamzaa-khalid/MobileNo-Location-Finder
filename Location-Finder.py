import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
number = input('Enter Number (With Country Code): ')

ch_num = phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_num, 'en'))
service_pro = phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(service_pro, 'en'))


