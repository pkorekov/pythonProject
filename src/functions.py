import json


def read_json(file_path):
    '''
    читает файл json
    :return: данные в виде списка словарей
    '''
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
    return data

def sort_data(data: list[dict]) -> list[dict]:
    '''
    сортирует даннные по статусу операции
    :param data: исходные даннные
    :return: отсортированные данные
    '''
    sorted_data = [operation for operation in data if operation['state'] == 'EXECUTED']

    return sorted_data


def format_from_account(input_from_account):
    '''
    Функция скрывает номер карты отправителя
    :param input_from_account: Номер счёта отправителя
    :return: Скрытый счёт отправителя
    '''
    from_account_split = input_from_account.split(" ")
    if len(from_account_split) == 2:
        if len(from_account_split[1]) == 16:
           new_str = ' ' + from_account_split[-1][0:4] + ' ' + from_account_split[-1][4:6] + '** ' + '**** ' + from_account_split[-1][12:16]
        elif len(from_account_split[1]) == 20:
           new_str = ' ' + from_account_split[-1][0:4] + ' ' + from_account_split[-1][4:6] + '** ' + '**** ' + from_account_split[-1][16:20]
        else:
           return "Invalid bank account from"
        return from_account_split[0] + new_str
    if len(from_account_split) == 3:
        if len(from_account_split[2]) == 16:
           new_str = ' ' + from_account_split[-1][0:4] + ' ' + from_account_split[-1][4:6] + '** ' + '**** ' + from_account_split[-1][12:16]
        elif len(from_account_split[2]) == 20:
           new_str = ' ' + from_account_split[-1][0:4] + ' ' + from_account_split[-1][4:6] + '** ' + '**** ' + from_account_split[-1][16:20]
        else:
           return "Invalid bank account to"
        return from_account_split[0] + " " +  from_account_split[1] + new_str

def format_to_account(input_to_account):
    """
    Функция скрывает номер карты получателя
    :param input_to_account: Номер счёта получателя
    :return: Скрытый счёт получателя
    """

    to_account_split = input_to_account.split(" ")
    if len(to_account_split) == 2:
        if len(to_account_split[-1]) == 16:
            new_str = ' **' + to_account_split[-1][12:16]
        elif len(to_account_split[-1]) == 20:
            new_str = ' **' + to_account_split[-1][16:20]
        else:
            return "Invalid bank account to"
        return to_account_split[0] + new_str
    if len(to_account_split) == 3:
        if len(to_account_split[-1]) == 16:
            new_str = ' **' + to_account_split[-1][12:16]
        elif len(to_account_split[-1]) == 20:
            new_str = ' **' + to_account_split[-1][16:20]
        else:
            return "Invalid bank account to"
        return to_account_split[0] + " "+ to_account_split[1] + new_str

def format_date(input_date):
    """
    Форматирует дату и время операции оставляя только дату в нужном формате
    :param input_date: Строка с данными о дате и времени операции
    :return: Строка с данными о дате в заданном формате
    """
    date_list = input_date[0:10].split('-')
    return '.'.join(date_list[::-1])