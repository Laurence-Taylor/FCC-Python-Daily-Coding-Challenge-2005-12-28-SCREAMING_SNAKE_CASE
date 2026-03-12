def to_screaming_snake_case(variable_name):
    set_change_word = set('QWERTYUIOPASDFGHJKLZXCVBNM')
    set_esp_char = set('-_')
    string_to_return = ''
    len_variable_name = len(variable_name)
    pos = 0
    for i in range(1,len_variable_name):
        if variable_name[i] in set_change_word:
            string_to_return += variable_name[pos:i].upper() + '_'
            pos = i
        if variable_name[i] in set_esp_char:
            string_to_return += variable_name[pos:i].upper() + '_'
            pos = i+1
        if i == len_variable_name-1:
            string_to_return += variable_name[pos:len_variable_name].upper()
    print(string_to_return)
    return string_to_return

if __name__ == '__main__':
    print(to_screaming_snake_case("userEmail"))
    print('-----')
    print(to_screaming_snake_case("UserPassword"))
    print('-----')
    print(to_screaming_snake_case("user_id"))
    print('-----')
    print(to_screaming_snake_case("user-address"))
    print('-----')
    print(to_screaming_snake_case("username"))