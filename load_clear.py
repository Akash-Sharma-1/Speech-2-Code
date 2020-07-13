ACCESS_TOKEN = 'OWGTVORYEEKL5RYTVPWMJNI6WA5UIFDB'

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

def handle_load_clear(response: dict) -> str:
    intent = get_intent(response)
    if intent == Intent.load:
        # print("here")
        # Put this code here for now
        entities = response['entities']  # This field is guaranteed to be in the response
        properties = dict()
        
        for name, entity in entities.items():
            print(name,entity)
            # print(type(entity))
            if name == 'filename:filename':
                for x in entity:
                    # print(x.keys())
                    if x['value']!='file':
                        command='load '+x['value']
                        return command
    
    elif intent==Intent.clear:
        command='clear'
        return command
    
    elif intent==Intent.clear_cw:
        command='clc'
        return command

def get_command(text: str) -> str:
    client = Wit(ACCESS_TOKEN)
    response = client.message(text)
    print(response)
    code = handle_load_clear(response)
    return code

if __name__ == "__main__":
    print(get_command("load abc"))