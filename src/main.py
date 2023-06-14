import functions


data_list = functions.read_json('../operations.json')

operations = functions.sort_data(data_list)

for operation in operations:
    print(functions.get_message(operation))