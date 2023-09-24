import re
#Matches all numbers, decimal points, and - signs, Excludes the minus sign by itself. Basically checks if its a valid number
num_pattern = r'(?:^|(?<=[^0-9.]))-(?=[0-9.])|(?:[0-9]*\.[0-9]+|[0-9]+)'

def input_to_output(expression):
    shunted = shunting_yard(expression)
    calculated = calculate(shunted)
    return calculated


def calculate(shunted):
    answer = []

    while len(shunted) > 0:

        if "ERROR" in shunted[0]:
            return shunted[0]

        elif is_number(shunted[0]):
            answer.append(shunted[0])
            shunted = shunted[1:]

        elif shunted[0] == "+":
            if is_okay_to_math(answer):
                y = float(answer.pop())
                x = float(answer.pop())
                answer.append(str(x + y))
                shunted = shunted[1:]

        elif shunted[0] == "-":
            if is_okay_to_math(answer):
                y = float(answer.pop())
                x = float(answer.pop())
                answer.append(str(x - y))
                shunted = shunted[1:]
            
        elif shunted[0] == "*":
            if is_okay_to_math(answer):
                y = float(answer.pop())
                x = float(answer.pop())
                answer.append(str(x * y))
                shunted = shunted[1:]

        elif shunted[0] == "/":
            if is_okay_to_math(answer):
                y = float(answer.pop())
                x = float(answer.pop())
                answer.append(str(x / y))
                shunted = shunted[1:]

        elif shunted[0] == "^":
            if is_okay_to_math(answer):
                y = float(answer.pop())
                x = float(answer.pop())
                answer.append(str(x ** y))
                shunted = shunted[1:]

    return answer[0]

#BECASUE YOUR CALCULATOR WAS SO COOL YOU NEED TO MAKE SURE THE INPUTS ARE RIGHT OTHERWISE THIS CALCULATOR IS GOING TO GET FUCKED UP "+ +" KINDA STUFF
def shunting_yard(orginal_equation:str):
    equation = orginal_equation
    shunted = []
    operators = []
    while len(equation) > 0:
        current = equation[0]

        #case where the current item is a zero
        if current.isdigit():
            equation = extract_number(current, equation, shunted)

        #case where the current item is a .  like if the user entered .33, changes it to 0.33
        elif current == '.':
            equation = starting_decimal(equation, shunted)
            
        elif current == '-':
            if len(equation) > 1:
                if equation[1].isdigit():
                    equation = extract_number(current, equation, shunted)
                else:
                    equation = extract_operator(current, equation, shunted, operators)

        elif current == "+" or current == "*" or current == "/" or current == "^" or current == "(" or current == ")":
            equation = extract_operator(current, equation, shunted, operators)

        elif current == " ":
            equation = remove_first_char(equation)

        else:
            shunted.append(f"ERROR: Unknown symbol {current}")
            equation = remove_first_char(equation)
        
    while len(operators) > 0:
        if operators[0] == "(":
            shunted.append("ERROR: Mismatched parentheses")
            equation = remove_first_char(equation)
        shunted.append(operators.pop())


    return shunted


def starting_decimal(equation, shunted):
    equation = '0' + equation
    return extract_number("0", equation, shunted)
    

def extract_operator(current, equation, shunted, operators):
    if current == "-" or current == "+":
        while len(operators) > 0:
            if operators[-1] == '-' or operators[-1] == "+":
                shunted.append(operators.pop())
            elif operators[-1] == '*' or operators[-1] == "/":
                shunted.append(operators.pop())
            elif operators[-1] == '^':
                shunted.append(operators.pop())
            else:
                operators.append(current)
                return remove_first_char(equation)


        if len(operators) == 0:
            operators.append(current)
            return remove_first_char(equation)
    

    if current == "*" or current == "/":
        while len(operators) > 0:
            if operators[-1] == '*' or operators[-1] == "/":
                shunted.append(operators.pop())
            elif operators[-1] == '^':
                shunted.append(operators.pop())
            else:
                operators.append(current)
                return remove_first_char(equation)


        if len(operators) == 0:
            operators.append(current)
            return remove_first_char(equation)
        
    if current == "^":
            operators.append(current)
            return remove_first_char(equation)

    if current == "(":
            operators.append(current)
            return remove_first_char(equation)
    
    if current == ")":
        if len(operators) == 0:
            shunted.append("ERROR: Mismatched parentheses")
            return []
        while len(operators) > 0:
            if operators[-1] != "(":
                shunted.append(operators.pop())
            elif operators[-1] == "(":
                operators.pop()
                return remove_first_char(equation)
            else:
                shunted.append("ERROR: Mismatched parentheses")
                return []
    







def extract_number(current, equation, shunted):
    #Check and see if we have more to look for
    if len(equation) > 1:
        i = 2
        found_decimal = False  #Used to determine if there are multiple decimals in one number
        must_number = False  #Used to determine if a number needs to appear after the decimal 

        #Check to see if the next char is considered a number
        if (equation[i-1].isdigit() or equation[i-1] == '.'): 
            if equation[i-1] == '.':
                found_decimal = True
                must_number = True
            #Find the end of the number
            while True:
                if len(equation) > i and (equation[i].isdigit() or equation[i] == '.'):
                    if equation[i] == '.' and found_decimal:
                        shunted.append("ERROR: Incorrect use of decimal points")
                        return []
                    if equation[i] == '.':
                        found_decimal = True
                        must_number = True
                    must_number = False
                    i += 1
                else:
                    break
            
            #Get the number from the equation
            current = equation[0:i]
            #The number ended with a . so we add a zero to the end of it
            if must_number:
                current = current + "0"
            #save the number
            shunted.append(current)

            #Check if we still have more to parse if yes remove the number we just extracted
            if len(equation) > i:
                return equation[i:]
            #else nothing left to extract
            else:
                return []
            
        #There was not another number following the first one and the equation still has items
        else:
            shunted.append(current)    
            return equation[1:]

    #This is the last item in the equation
    else:
        shunted.append(current)
        if len(equation) == 1:
            return []

def remove_first_char(string):
    if len(string) > 1:
        return string[1:]
    #else nothing left to extract
    else:
        return []
    

def is_okay_to_math(answer):
    if len(answer) > 1:
        if is_number(answer[0]) and is_number(answer[1]):
            return True
    return False

def is_number(possible_number):
    if re.match(num_pattern, possible_number):
        return True
    return False


if __name__ == "__main__":
    print(input_to_output("3.0"))
