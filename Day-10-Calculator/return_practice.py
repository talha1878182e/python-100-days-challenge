
def format_name(f_name, l_name):
    formate_f_name = f_name.title()
    formate_l_name = l_name.title()
    return f"Hello {formate_f_name} {formate_l_name}"
formated_str = format_name(input("What is your name: "), input("What is your last name: "))
print(formated_str)
