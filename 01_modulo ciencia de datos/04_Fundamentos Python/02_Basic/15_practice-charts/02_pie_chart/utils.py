def get_population(countryDic):
    # Inicializa el diccionario de población
    populationDic = {
        "2022": int(countryDic["2022 Population"]),
        "2020": int(countryDic["2020 Population"]),
        "2015": int(countryDic["2015 Population"]),
        "2010": int(countryDic["2010 Population"]),
        "2000": int(countryDic["2000 Population"]),
        "1990": int(countryDic["1990 Population"]),
        "1980": int(countryDic["1980 Population"]),
        "1970": int(countryDic["1970 Population"]),
    }
    # Llenar el diccionario con los datos de población
    for year in populationDic:
        key = f"{year} Population"
        if key in countryDic:
            populationDic[year] = int(countryDic[key])  # Convertimos a entero
    
    labels = list(populationDic.keys())
    values = list(populationDic.values())
    return labels, values


def population_by_country(data, country):
    # Filtrar el país en la lista de diccionarios
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result
