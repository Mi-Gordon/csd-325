# Michael Gordon
# CSD-325
# Assignment 7.2

# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such as Santiago, Chile.

def city_country(city, country, population='', language=''):
    if population and language:
        location_data = (
            f'\n{city}, {country} - population {population}, {language}\n')
    elif population:
        location_data = (
            f'\n{city}, {country} - population {population}\n')
    else:
        location_data = (f'\n{city}, {country}\n')
    return location_data


def main(): {
    print(city_country('Peoria', 'USA')),
    print(city_country('Santiago', 'Chile', 5000)),
    print(city_country('Farmington', 'USA', 47000, 'English'))
}


if __name__ == '__main__':
    main()
