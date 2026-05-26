import json


def load_exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        return json.load(file)

def instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available currencies.')
    print('3. Type QUIT to exit.')

def convert_currencies(user_input: str, rates: dict[str, float]) -> dict[str, float | str | dict[str, float]] | None:
    currency_codes: list[str] = list(rates.keys())
    input_currency_code: str = user_input[-3:]

    if input_currency_code not in currency_codes:
        print(f'Currency code: {input_currency_code} is invalid')
        return

    try:
        input_amount: float = float(user_input[:-3])
    except ValueError:
        print(f'"{user_input}" is invalid. Try something like: "10 AUD"')
        return

    base_conversion: float = input_amount / rates[input_currency_code]

    converted_currencies: dict[str, float] = {}
    for currency_code in currency_codes:
        converted_currencies[currency_code] = base_conversion * rates[currency_code]

    return {'input_amount': input_amount,
            'input_currency': input_currency_code,
            'conversions': {code: base_conversion * rates[code] for code in currency_codes}}

def disp_converted_currencies(result: dict[str, float | str | dict[str, float]] | None) -> None:
    print(f'{round(result['input_amount'], 2):>16} {result['input_currency']}')
    print('-' * 20)
    for code, amount in result['conversions'].items():
        print(f'= {round(amount, 2):>14} {code}')


def main() -> None:
    instructions()

    exchange_rates: dict[str, float] = load_exchange_rates()

    while True:
        user_input: str = input('Convert: ').upper().strip()

        if user_input == 'LIST':
            print(f'Available currencies: {', '.join(exchange_rates.keys())}')
            continue
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        result = convert_currencies(user_input, exchange_rates)
        if result:
            disp_converted_currencies(result)

if __name__ == '__main__':
    main()
