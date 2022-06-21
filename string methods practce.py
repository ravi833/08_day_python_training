''' string methods practice'''

# a='round circle'
# print(a.count('r'))  #2

# a='raju taking books'
# print(a.index('j')) #2
# print(a.rindex('o')) #14

# a='we are workers'
# # print(a.find('a')) #3
# print(a.rfind('w')) #7

# a,b=[x for x in input().split()]
 
# a='python program'
# print(a.split()) # ['python', 'program']
# print(a.splitlines()) # ['python program']

# a='  python  . '
# print(a.strip())  #python.
# print(a.lstrip()) #python  .
# print(a.rstrip())  #  python  .

# a='python'
# print(a.isupper())  #false
# print(a.upper())  #PYTHON
# a='PYTHON' 
# print(a.isupper()) #true 


# a='python'
# print(a.islower())  #true
# a='PYTHON'
# print(a.lower())  #python
# print(a.islower())  #false





''' practice string methods day 2'''

# print(isinstance('hello',str))  #true
# print(isinstance('raju330',str))  #true
# print(isinstance('coding 45',str))  #true
# print(isinstance('hello',int))   #false
# print(isinstance('hello',float))  #false
# print(isinstance('ironman',str))  #true

# print('hello'.isidentifier())  #True
# print('vikram'.isidentifier())  #true
# print('69he'.isidentifier())  #false
# print('_ravi'.isidentifier())  #true
# print('_virat'.isidentifier())  #true

# print(''.isspace())  #false
# print(' '.isspace())  #true
# print('  '.isspace())  #true
# print('65'.isspace())  #false


# print('cricket'.isalpha())  #true
# print('cricket67'.isalpha())  #false
# print('cricket virat'.isalpha())  #false
# print('cricket_raju'.isalpha())  #false


# print('virat68'.isalnum())  #true
# print('virat 68'.isalnum())  #false
# print('virat_68'.isalnum())  #false
# print('dhoni7'.isalnum())   #true
# print('kohli123'.isalnum())   #false


print('coding solution in python'.find('i'))   #3
print('coding solution in python'.find('i',4))   
print('coding solution in python'.rfind('i'))   #3


