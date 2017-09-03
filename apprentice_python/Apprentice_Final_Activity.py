import operator

saved_string = ''

def  remove_letter(): #Remove a selected letter from a string
	print "Remove Letter"
	base_string = str(raw_input("Enter a string: "))
	letter_remove = str(raw_input("Introduce letter to remove: ")) # here we get all letters we want
	letter_remove = letter_remove[0] # we force to have only one letter
	string_length = len(base_string)
	location = 0
	
	while (location < string_length): #by reference (rather than by value)
		if base_string[location] == letter_remove:
			base_string = base_string[:location] + base_string[location+1::] # cada vez que se elmina 
			string_length -= 1 # u caracter, se acorta en uno la longitud del string
			location+=1

	print "Result: %s" % base_string
	return

def num_compare(): #Compare 2 numbers to determine the larger
	print "Num compare"
	num1 = int(raw_input("Input first number: "))
	num2 = int(raw_input("Input second number: "))
	
	if num1 > num2:
		print num1
	elif num1 < num2:
		print num2
	else:
		print "Equal"
		
	return

def print_string(): #Print the previously stored string
	print "Print String"
	print saved_string
	return

def calculator(): #Basic Calculator (addition, subtraction, multiplication, division)
	print "Calculator"
	# esto no funciona: sign_dict = {'+':sum, '*':*, '-':-, '%'=%}
	sign_dict = {'+': operator.add , '-' : operator.sub , '*' : operator.mul , '%' : operator.div}
	num1 = int(raw_input("Input first number: "))
	sign = str(raw_input("Action: "))
	num2 = int(raw_input("Input second number: "))
	
	res = sign_dict[sign](num1,num2)
	print res
	# following way is less practical
	#if sign =="+":
	#	print num1 + num2
	#if sign =="-":
	#	print num1-num2
	#if sign =="*":
	#	print num1*num2
	#if sign =="%":
	#	print num1%num2
		
	return

def accept_and_store(): #Accept and store a string	
	global saved_string # use of global only to writing a variable, not to read
	saved_string = str(raw_input('Input String: '))
	return

def main(): #menu goes here	
	opt_list = [accept_and_store,
	calculator, print_string,num_compare,remove_letter]
	
	while(True):
		print "SELECT OPTION"
		print "1\tAccept and  Store"
		print "2\tCalculator"
		print "3\tPrint String"
		print "4\tNum compare"
		print "5\tRemove Letter"
		opt_choice = int(raw_input("SELECTION:  "))
		opt_choice -= 1
		opt_list[opt_choice]()
		
	return

main()
