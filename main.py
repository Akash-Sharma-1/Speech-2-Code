'''
    NOTES
    Represent best_varname to represent a property with maximum confidence value
    which usually occurs as the first occurence in the array.
'''

import wit
import enum
import control_flow, assignment, math_operations, load_clear, doc_display

# Access Tokens of Apps with specific functionalities
ACCESS_TOKEN_Assign = 'CI6BP3XV7PKYL5WHDXXVEXVEACXRI7SQ'
ACCESS_TOKEN_Doc_Help = 'KK53HUY7LVRSQHMRABZMZVWOJROABNZ5'
ACCESS_TOKEN_Clear_Load = 'OWGTVORYEEKL5RYTVPWMJNI6WA5UIFDB'
ACCESS_TOKEN_Math_Operation = 'QJEZVEXD7TWA4BIRITQZ4NDEPEPJ3LZ7'
ACCESS_TOKEN_control_flow = 'KZ4WJKAEN3YQ7KRY2S4F77GYIOV3NZ4D'

# Returns the MATLAB syntax if the response is valid.
# Otherwise returns -1.

if __name__ == "__main__":
    
    speechText = [
        # "set n as 5",
        # "Assign fact as 1",
        # "loop i from 1 through 5",
        # "multiply fact with i",
        # "end",
        # "display fact",
        # "remainder of x with 34"
        "set Pi as 3.14",
        "loop I from 1 to 20",
        "add I with x",
        "end the loop",
        "display x"
    ]

    for speech in speechText:
        ACCESS_TOKEN=""
        code = -1

        speechLowerCase = speech.lower()

        ## Conditional Handling of Apps
        # trivial
        if("doc" in speechLowerCase or "documentation" in speechLowerCase  or "help" in speechLowerCase or "display" in speechLowerCase or "print" in speechLowerCase):
            code = doc_display.get_command(speech)

        # modularised
        elif("set" in speechLowerCase or "assign" in speechLowerCase):
            # ACCESS_TOKEN = ACCESS_TOKEN_Assign
            code = assignment.get_command(speech)

        #modularised
        elif("while" in speechLowerCase or "if" in speechLowerCase or "loop" in speechLowerCase  or "for" in speechLowerCase or "end" in speechLowerCase or "else" in speechLowerCase):
            code = control_flow.get_command(speech)

        ## FOR abhivandan's
        elif("clear" in speechLowerCase or "remove" in speechLowerCase or "load" in speechLowerCase):
            code = load_clear.get_command(speech)

        else:
            # ACCESS_TOKEN = ACCESS_TOKEN_Math_Operation
            code = math_operations.get_command(speech)
        
        print(code)

        # client = wit.Wit(ACCESS_TOKEN)
        # response = client.message(speech)
        # print(get_syntax(response))