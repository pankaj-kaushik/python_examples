country = ['India', 'USA', 'France']
cities = ['delhi', 'new york', 'paris']

y = {city:country for city, country in zip(country, cities)}

print y