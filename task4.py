def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        int_num = input("Enter not negative integer number or '/break' to change task: ")
        if int_num == '/break':
            return
        elif input_valid_condition(int_num):
            task_basic_func(int_num)
        else:
            print("Invalid integer. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    return int(input_data) >= 0
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    in_data = int(in_data)
    str_num = ''
    print(f"Decimal {in_data} is binary ", end='')
    while(in_data > 1):
        if in_data % 2 > 0:
            str_num = '1' + str_num
        else:
            str_num = '0' + str_num
        in_data //= 2
    else:
        str_num = '1' + str_num
    print(f"{str_num}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------