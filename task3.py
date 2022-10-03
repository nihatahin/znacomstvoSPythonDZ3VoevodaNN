def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        listNum = input("Enter list of numbers split with spacebar (example: 0 1 2 3 4 5) or '/break' to change task: ")
        if listNum == '/break':
            return
        elif input_valid_condition(listNum):
            task_basic_func(listNum.split())
        else:
            print("Invalid list. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    for i in range(len(input_data)):
        if not(input_data[i].isdigit() or input_data[i] == '.' or input_data[i] == '-' or input_data[i] == ' '):
            return False
    else:
        return True
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data): 
    frac_data = frac_list_creation(in_data)
    if len(frac_data) > 1:
        result = max_min_in_list(frac_data)
        print(f"Maximal ({result[1]}) and minimal ({result[0]}) elements substraction is equal to {round(result[1] - result[0], 3)}.")
    else:
        print("Input array consists of integer numbers or have only one float nuber.")
        print("Subtraction is impossible!")

#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def integer_cut(num):
    return num - int(num)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def str_is_float(str_num):
    for i in range(len(str_num)):
        if str_num[i] == '.':
            return True
    else:
        return False
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def frac_list_creation(str_list):
    frac_list = []
    for i in range(len(str_list)):
        if str_is_float(str_list[i]):
            frac_list.append(round(integer_cut(float(str_list[i])), 3))
    return frac_list
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def max_min_in_list(num_list):
    max = num_list[0]
    min = max
    for i in range(1, len(num_list)):
        if min > num_list[i]:
            min = num_list[i]
        elif max < num_list[i]:
            max = num_list[i]
    return [min, max]
