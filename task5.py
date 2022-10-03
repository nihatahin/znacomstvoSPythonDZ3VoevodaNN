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
    if in_data == 0:
        fibo = [0]
    elif in_data == 1:
        fibo = [1, 0, 1]
    else:
        fibo = [0] * (2 * in_data + 1)
        fibo[in_data + 1] = 1
        fibo[in_data - 1] = fibo[in_data + 1]
        for i in range(2, in_data + 1):
            fibo[in_data + i] = fibo[in_data + i - 1] + fibo[in_data + i - 2]
            if (i % 2) > 0:
                fibo[in_data - i] = fibo[in_data + i]
            else:
                fibo[in_data - i] = -fibo[in_data + i]
    print(fibo)      
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------