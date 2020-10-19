# Hello this is a Test

while True:
	print("Willkommen zum Rechner")
	print("======================")
	print(" 1 - Plus")
	print(" 2 - Minus")
	print(" 3 - Mal")
	print(" 4 - Durch \n")
	print(" 0 - Beenden")
	
	# Eingabe
	try:
		eing = int(input("Wählen Sie: "))
	except:
		input("input error try again.")
		eing = 5
	if(not eing == 5):
		first_number = int(input("Bitte die erste Zahl eingeben: "))
		second_number = int(input("Bitte die zweite Zahl eingeben: "))		

		out = 0

		# Verarbeitung
		if(eing == 1):
			out = first_number + second_number
		if(eing == 2):
			out = first_number - second_number
		if(eing == 3):
			out =  first_number * second_number
		if(eing == 4):
			out = first_number / second_number
		if(eing == 0):
			break
		
		input("Das ist das Resultat: " + str(out))