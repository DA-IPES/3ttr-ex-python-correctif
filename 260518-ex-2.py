my_list = [3, 2, 6, 5]
# observe that the 1st is at position (1-1=) 0 in the list, and that the third is at position (3-1=) 2
sum_of_first_and_third = my_list[0] + my_list[2]
rest_of_div_is_modulo = my_list[2] % my_list[3]
second_to_square = my_list[1] ** 2

print(sum_of_first_and_third)  # returns 9
print(rest_of_div_is_modulo)  # returns 1
print(second_to_square)  # returns 4
