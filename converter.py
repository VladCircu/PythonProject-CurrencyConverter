import data

def convert(first_currency,value,last_currency):
    print()
    print(first_currency)
    print(last_currency)
    dict = data.data()
    # print(dict[first_currency])
    # print(dict[last_currency])
    print(value)
    if first_currency == last_currency:
        return
    if first_currency == 'RON':
        converted_sum = float(value) / dict[last_currency]
    elif last_currency == 'RON':
        converted_sum = float(value) * dict[first_currency]
    else:
        converted_sum = float(value) * dict[first_currency] / dict[last_currency]


    return converted_sum




# convert('USD',100,'EUR')