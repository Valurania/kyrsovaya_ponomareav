def operatoin_data_filer(operation_list):
    operation_list_new = []
    operation_description = "Описание отсутствует"
    operation_date = "XX.XX.XXXX"
    operation_card = "**** **** **** ****"
    operation_check = "**** **** **** ****"
    operation_amount = "нет данных"
    operation_currency = "нет данных"
    operation_id = "нет данных"
    operation_state = "нет данных"
    operation_code = "нет данных"

    for operation_dict in operation_list:
        if "date" in operation_dict.keys():
            operation_date = operation_dict['date']
        if "description" in operation_dict.keys():
            operation_description = operation_dict['description']
        if "from" in operation_dict.keys():
            operation_card = mask_card(operation_dict['from'])
        if 'to' in operation_dict.keys():
            operation_check = mask_check(operation_dict['to'])
        if 'operationAmount' in operation_dict.keys():
            if 'amount' in operation_dict['operationAmount']:
                operation_amount = operation_dict['operationAmount']['amount']
            if 'currency' in operation_dict['operationAmount']:
                operation_currency = operation_dict['operationAmount']['currency']['name']
            if 'code' in operation_dict['operationAmount']['currency']:
                operation_code = operation_dict['operationAmount']['currency']['code']
        if 'id' in operation_dict.keys():
            operation_id = operation_dict['id']
        if 'state' in operation_dict.keys():
            operation_state = operation_dict['state']
        operation_list_new.append({'id':operation_id, 'state':operation_state, 'date': operation_date, 'operationAmount': {'amount':operation_amount, 'currency': {'name': operation_currency, 'code': operation_code}}, 'description': operation_description, 'from': operation_card, 'to': operation_check})
    return operation_list_new


def operations_output(operation_dict):
    return f"{transformation_date(operation_dict['date'])} {operation_dict['description']}\n" \
           f"{operation_dict['from']} -> {operation_dict['to']}\n" \
           f"{operation_dict['operationAmount']['amount']} {operation_dict['operationAmount']['currency']['name']}"

def transformation_date(data_str):
    return f"{data_str[8:10]}.{data_str[5:7]}.{data_str[0:4]}"

def mask_card(from_str):
    from_str = from_str.split()
    name = ' '.join(from_str[:-1])

    chunk = 4
    number = ''
    for i in range(len(from_str[-1]) - 1, -1, -1):
        if chunk == 0:
            number += ' '
            chunk = 4
        if len(from_str[-1]) - 10 <= i <= len(from_str[-1]) - 5:
            number += '*'
        else:
            number += from_str[-1][i]
        chunk -= 1

    return f"{name} {number[::-1]}"

def mask_check(to):
    name = ' '.join(to.split()[:-1])
    return f"{name} **{to[-4:]}"



