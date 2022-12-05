input_filename = 'country_info.txt'

countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialling_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        #print(country_dict)
        # modify the code to allow user to use country code as well as the name to select the country:
        countries[country.casefold()] = country_dict
        # code_lookup[code.casefold()] = country or try:
        countries[code.casefold()] = country_dict
#print(countries)
#print('*' * 80)

# Challenge: print capital city for the country input by the user:

while True:
    chosen_country = input('Please choose the name of the country or the country code: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == "quit":
            break




