import time
lamp_status = ['00','10','10','01','01','10','10','00']
def convert_string_to_decimal(msg):
    return int(msg,2)
# msg = '01|5|03|08|%s|%s'%(convert_string_to_decimal("".join(lamp_status[0:4])),convert_string_to_decimal("".join(lamp_status[4:8])))
msg = '01|5|03|08|%s|%s'%(convert_string_to_decimal("".join(lamp_status[0:4])),convert_string_to_decimal("".join(lamp_status[4:8])))

def convert_str_to_hex(msg):
    bytes = msg.split('|')
    hex_values = []
    for d in bytes :
        hex_data = hex(int(d))  # Convert the byte to its hex representation
        hex_values.append(hex_data) 
    return hex_values
def calculate_string_check_sum(message_without_check_sum):
    '''
    Calculate check_sum
    Args:
        message_without_check_sum(str): message after removing check sum value.
    Returns:
        int: calculated check_sum(mod 10).
    '''
    check_sum = 0
    buffer = message_without_check_sum.split("|")
    for char in buffer:
        if char != "|":
            try:
                check_sum = check_sum + int(char)
            except ValueError:
                continue
    check_sum = check_sum % 10
    return check_sum

def final_string(msg):
    check_sum = calculate_string_check_sum(msg)
    return "250|"+msg+"|"+str(check_sum)+"|251"

# print(bytearray(final_string(msg),'utf-8'))
print(final_string(msg))
# print(convert_str_to_hex(final_string(msg)))