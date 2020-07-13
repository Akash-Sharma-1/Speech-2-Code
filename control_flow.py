# Author: Apoorv Singh
# Author: Reeshabh Kumar Ranjan

ACCESS_TOKEN = "KZ4WJKAEN3YQ7KRY2S4F77GYIOV3NZ4D"

from wit import Wit
import json

def __process_for(root: dict) -> str:
    entities: dict = root['entities']
    range_start = None
    range_end = None
    variable = None

    # handle errors if required keys are not present
    range_start = None
    range_end = None

    if 'range_start:range_start' in entities:
        range_start = int(entities['range_start:range_start'][0]['value'])
    else:
        range_start = int(entities['wit$number:number'][0]['value'])

    # print(entities)
    if 'range_end:range_end' in entities:
        range_end = int(entities['range_end:range_end'][0]['value'])
    else:
        range_end = int(entities['wit$number:number'][len(entities['wit$number:number']) - 1]['value'])
    

    variable = entities['variable:variable'][0]['value']

    command = f'for {variable} = {range_start} : {range_end}'
    return command

def __process_conditional(root: dict) -> str:
    text = root['text']
    entities = root['entities']
    
    variable1 = None
    variable2 = None

    if 'variable:variable' in entities:
        variable1 = entities['variable:variable'][0]['value']
        if len(entities['variable:variable']) > 1:
            variable2 = entities['variable:variable'][1]['value']

    if 'wit$number:number' in entities:
        if len(entities['wit$number:number']) > 1:
            variable1 = entities['wit$number:number'][0]['value']
        variable2 = entities['wit$number:number'][-1]['value']

    variable1 = str(variable1)
    variable2 = str(variable2)

    if text.find(variable1) > text.find(variable2):
        variable1, variable2 = variable2, variable1
    
    operation = root['entities']['operation:operation'][0]['value']
    
    if operation == 'else if':
        operation = 'elseif'

    comparision = root['entities']['comparision:comparision'][0]['value']
    # print (comparision)

    operator = ''

    if comparision.find('greater') >= 0:
        operator += '>'
        if comparision.find('equal') >= 0:
            operator += '='
    elif comparision.find('less') >= 0:
        operator += '<'
        if comparision.find('equal') >= 0:
            operator += '='
    else:
        operator += '=='

    command = f'{operation} {variable1} {operator} {variable2}'

    return command

def __handle_conditional_and_loops(root: dict) -> str:
    intent = root['intents'][0]['name']

    # print(intent)

    if intent == 'for_loop':
        return __process_for(root)
    elif intent == 'conditional_operation':
        return __process_conditional(root)
    elif intent == 'end':
        return 'end'
    elif intent == 'else':
        return 'else'

def get_command(text: str) -> str:
    client = Wit(ACCESS_TOKEN)
    response: dict = client.message(text)
    code = __handle_conditional_and_loops(response)
    return code

if __name__ == "__main__":

    client = Wit(ACCESS_TOKEN)

    inputs = [
        "if xjsdh is greater than 528374",
        "if 872348923 less than 392742398",
        "if cjksdkkb is less than dkjgkskkks",
        "if xjsdh is lesser than 528374",
        "if 872348923 is greater than 392742398",
        "if cjksdkkb greater than dkjgkskkks",
        "if xjsdh is greater than or equals 528374",
        "if cjksdkkb greater than or equal to dkjgkskkks",
        "if 872348923 lesser than or equal to 392742398",
        "if cjksdkkb less than or equals dkjgkskkks",
        "if fsdkllfl equals 213992",
        "if 123123 equals 1323",
        "while 5 is greater than asd",
        "while xasdd is greater than or equals 123123",
        "while xasdd equals 123123",
        "while xasdd is less than 123123",
        "while xasdd less than or equals 123123"
        "else",
        "end",
        "loop i from 5 through 78"
    ]

    for inp in inputs:
        print(inp)
        print(__handle_conditional_and_loops(client.message(inp)))