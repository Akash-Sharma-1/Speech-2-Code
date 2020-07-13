ACCESS_TOKEN = 'CI6BP3XV7PKYL5WHDXXVEXVEACXRI7SQ'

from wit import Wit

def handle_assign(response: dict) -> str:
    entities = response['entities']  # This field is guaranteed to be in the response
    properties = dict()
    # print(entities)
    
    value = ''
    var = ''
    dataType = ''
    subs = ''

    for name, entity in entities.items():
        if name == 'value:value':
            if 'dataType' in entities:
                for num in entity:
                    value += num['value'] + ' '
                value = value.strip()
            else:
                value = entity[0]['value']

        elif name == 'var:var': 
            var = entity[0]['value']

        elif name == 'dataType:dataType':
            dataType = entity[0]['value']
    
        elif name == 'wit$number:number':
            subs = entity[0]['value']

    # print(var, value, dataType)
    if var == '':
        return -1

    if value == '' and subs == '':
        return str(var) + ';'

    if value == '':
        value = subs

    if dataType == '':
        return var + ' = ' + str(value) + ';'

    else:
        
        if dataType.lower() == 'string':
            return  var + ' = ' + '"' + str(value) + '"' + ';'

        else:
            return  var + ' = ' + "'" + str(value) + "'" + ';'

def get_command(text: str) -> str:
    client = Wit(ACCESS_TOKEN)
    response = client.message(text)
    code = handle_assign(response)
    return code

if __name__ == "__main__":
    print(get_command("set x as 5"))