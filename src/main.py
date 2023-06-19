import functions


data_list = functions.get_input_data('operations.json')

operations = functions.get_executed_operations(data_list)

for operation in operations:
    print(functions.get_message(operation))