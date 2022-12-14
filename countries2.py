import csv

input_filename = 'country_info.txt'

dialect = csv.excel # cmd+click on excel, shows the properties of the excel csv code:
dialect.delimiter = '|'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    # Get the column heading from the first like of the file
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # countries[country.casefold()] = country_dict - earlier code
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict - earlier code
        countries[row['cc'].casefold()] = row
# #print(countries)

while True:
    chosen_country = input('Please choose the name of the country or the country code: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == "quit":
        break
