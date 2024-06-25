print("hello")
a = 22

res = 'hello'*2
print(res)

stuff_us = 23
print(stuff_us)


print('what is your name')
# my_name = input()
# print('it is good to meet you, ' + my_name )
#
# if my_name == 'anand':
#     print('yes')

def life_lesson():
    print("Be kind")
life_lesson()

def addTwo (a,b):
    return a*b
print( addTwo(2,5))

# multiple lines of arguments in one function (user *args)
# Arrays are called lists in python it has some reference to it
def handle_multiple_args(*args):
    return args

print(handle_multiple_args(2,34,6,7,2,24,'sf','ffg'))

# slice method in python
# used for trimming an array or string

message = 'Hi there everyone'

print(message[3:7]) # message[3:7] - the first value [3] will get included but last value won't
# it's like [last value - 1] index
