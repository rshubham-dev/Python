# Map applies a function to all the items in an input_list.
# map(function, input_list) 
              # the function can be lambda function


l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqlist = map(square, l)
print(list(sqlist))