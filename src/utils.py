

def rule_parser(s):
    """
    Input: Rule String
    Output: rules string parsed to list of instructions
    """
    out = [*map(lambda x: x.strip(), s.split(','))]
    for i in range(len(out)):
        try:
            out[i] = float(out[i])
        except ValueError:
            pass
    return out


def rule_validator(s):
    """
    Input: Rule String
    Output: Bool determining if rule is valid
    """
    operators = ['>', '<']
    conj = ['and', 'or']
    rules_array = rule_parser(s)
    if len(rules_array) < 3:
        return False
    elif len(rules_array) == 3:
        return all([
            rules_array[0] == 'temp',
            rules_array[1] in operators,
            type(rules_array[2]) is float
        ])
    elif len(rules_array) == 7:
        return all([
            rules_array[0] == 'temp',
            rules_array[1] in operators,
            type(rules_array[2]) is float,
            rules_array[3] in conj,
            rules_array[4] == 'temp',
            rules_array[5] in operators,
            type(rules_array[6]) is float,
        ])
    else:
        return False


def sub_rule(rule, t):
    if rule[1] == '>':
        if t > rule[2]:
            return False
    if rule[1] == '<':
        if t < rule[2]:
            return False

    return True


def following_rules(s, temp, unit):
    """
    input: (rule_string, temp_reading, unit)
    output: true if rule is followed false if not
    """
    if unit == 'fahrenheit':
        temp = (temp - 32) * (5/9)

    rule = rule_parser(s)
    if len(rule) == 3:
        if sub_rule(rule, temp):
            return True
    if len(rule) == 7:
        if sub_rule(rule[:3], temp) and sub_rule(rule[4:], temp):
            return True

    return False


def send_message(msg):
    """
    input: message string
    Output: None
    Description: Sends SMS message using number information defined in environment variables
    """

    # TODO: send message with twilio
    # message = client.messages \
    #     .create(
    #     body=msg,
    #     from_=FROM_NUMBER,
    #     to=TO_NUMBER
    # )
    print(msg)

