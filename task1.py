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
    sum = 0
    for i in range(1, len(in_data), 2):
        sum += float(in_data[i])
    print(f"Odd indexed element sum is equal to {round(sum, 2)}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------