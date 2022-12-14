import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    dict_reader = csv.DictReader(country_file, delimiter = '|')
    for row in dict_reader:
        # countries[country.casefold()] = country_dict - earlier code
        countries[row['Country'].casefold()] = row
        # countries[code.casefold()] = country_dict - earlier code
        countries[row['CC'].casefold()] = row
# #print(countries)

while True:
    chosen_country = input('Please choose the name of the country or the country code: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == "quit":
        break
