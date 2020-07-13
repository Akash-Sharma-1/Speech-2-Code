ACCESS_TOKEN = 'QJEZVEXD7TWA4BIRITQZ4NDEPEPJ3LZ7'

from wit import Wit

def handle_math(response: dict) -> str:
    entities = response['entities']
    operation=entities["operation:operation"][0]["value"]  # This field is guaranteed to be in the response
    operator_map={"multiply":"*","add":"+","divide":"/","subtract":"-","remainder":"rem","modulo":"mod","increment":"+","decrement":"-"}
    varList=entities["var:var"]
    command=""
    operator_sign=operator_map[operation]

    if("wit$number:number" in entities):
        number = entities["wit$number:number"][0]["value"] 
        var = varList[0]["value"]
        if operator_sign == "rem" or operator_sign == "mod":
            command = var + " = " + operator_sign + "(" + var + "," + str(number) + ");"
        else:
            command = var + " = " + var + operator_sign + number
    else:
        primaryVar = varList[0]["value"] 
        if operator_sign == "rem" or operator_sign == "mod":
            secondaryVar = varList[1]["value"] 
            command = primaryVar + " = " + operator_sign + "(" + primaryVar + "," + secondaryVar + ");"
        else:
            command = primaryVar + " = " + primaryVar + " "
            for varNames in varList[1:]:
                command += operator_sign + " " + varNames["value"]
            command += ";"
    
    return command

def get_command(text: str) -> str:
    client = Wit(ACCESS_TOKEN)
    response = client.message(text)
    code = handle_math(response)
    return code

if __name__ == "__main__":
    print(get_command("multiply fact with i"))