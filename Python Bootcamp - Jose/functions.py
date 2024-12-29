
'''
def even_check(num_list):
    """to check if numbers in a list is even or not"""
    even_check = []
    
    for nums in num_list:
        if nums % 2 == 0:
            even_check.append(nums)
        else:
            print(f"{nums} is odd")
    
    return even_check
    
print(even_check([1,2,3, 4, 6]))
'''

work_hours = [('Abby', 1000), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''
    
    for emp in work_hours:
        if emp[1] > current_max:
            current_max = emp[1]
            employee_of_month = emp[0]
        else:
            pass
    
    return (current_max, employee_of_month)

best_emp = employee_check(work_hours)
print(best_emp)