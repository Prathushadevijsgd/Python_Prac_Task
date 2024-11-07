def uniq_min_max(numbers):
    uniq_num = list(set(numbers))
    tuple1 = tuple(uniq_num)

    min_num = min(tuple1)
    max_num = max(tuple1)

    return tuple1, min_num, max_num

numbers = [11,2,7,3,2,11,7,8]

uniq_tuple,min_val,max_val = uniq_min_max(numbers)

print("List of numbers is : ",numbers)
print("Unique tuple is : ",uniq_tuple)
print("Min number is : ",min_val)
print("Max number is : ",max_val)
