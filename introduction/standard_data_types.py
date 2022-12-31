from pickle import TRUE

print("Standard Data Types: ")
print('Immutable Data Types:')
print('Numbers:')
integer = 19
float_number = 23.4
complex_number = 10-9j
print("Numbers: ", "Integer: ", integer, "Float: ", float_number, "Complex(j): ", complex_number)

print('Strings:')
string_identifier = 'Single quotes' 
string_doubled_identifier = "Double quotes"
print("String: ", "Single quoted: ", string_identifier, "Double quoted: ", string_doubled_identifier)

print('Tuples:')
tuple_A = (1,10,-8,2,'String single quoted', "Double quoted string", 0)
print("Tuple: ", tuple_A)

print("===============================================")
print('Mutable Data Types:')
print('Lists:')
list_A =[1,10,-8,2,'String single quoted', "Double quoted string", 0]
print("List A: ", list_A)
list_A.append(13)
print("List A: ", list_A)

print('Dictionaries:')
dictionary_A = {'Age': 23, 'Gender': 'F'}
print("Dictionary A: ", dictionary_A)
dictionary_A.__delitem__('Age')
print("Dictionary A: ", dictionary_A)

print('Sets:')
set_A = {1,2,3,2}
print("Set A: every elements should be unique: ", set_A)
set_A.add(4)
print("Set A: every elements should be unique: ", set_A)