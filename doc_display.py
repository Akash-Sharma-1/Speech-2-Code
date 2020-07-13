ACCESS_TOKEN = 'KK53HUY7LVRSQHMRABZMZVWOJROABNZ5'

from wit import Wit
import enum

class Intent(enum.Enum):
    load = 1
    clear = 2
    clear_cw = 3
    doc = 4
    help = 5
    assign = 6
    math = 7
    display = 8

def get_intent(response):
    try:
        intents = response['intents'] # This field is guaranteed to be in the response
        best_intent = intents[0]['name']
        return Intent[best_intent]
    except:
        return -1

def handle_doc_display(response: dict) -> str:
    intent = get_intent(response)
    if intent==Intent.doc:
        entities = response['entities']  # This field is guaranteed to be in the response
        command="doc "
        command+=entities["function:function"][0]["value"]
        return command

    elif intent==Intent.help:
        # print(response)
        entities = response['entities']  # This field is guaranteed to be in the response
        command="help "
        command+=entities["function:function"][0]["value"]
        return command
    
    elif intent==Intent.display:
        entities = response['entities']

        if("function:function" in entities):
            var = entities["function:function"][0]["value"]
            command = "disp(" + var + ");"
        elif("wit$number:number" in entities):
            number = entities["wit$number:number"][0]["value"]
            command = "disp(" + number + ");"
        
        return command

def get_command(text: str) -> str:
    client = Wit(ACCESS_TOKEN)
    response = client.message(text)
    code = handle_doc_display(response)
    return code

if __name__ == "__main__":
    print(get_command("load abc"))