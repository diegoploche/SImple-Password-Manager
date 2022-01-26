def manager():

	master_pwd = input("What is the master password? ")

	def view():
		with open('passwords.txt', 'r') as f:
			for line in f.readlines():
				user, pwdrec = line.split(",")
				print("User: " + user + " , Password: " + pwdrec)

	def add():
		name = input("Account Name: ")
		pwd = input("Password: ")
		#f the name for the file and use with to close file automatically.
		with open('passwords.txt', 'a') as f:
			f.write(name + " , " + pwd + "\n")

	def pwd_mng():

		while True:
			if master_pwd == "diego":
				print("Correct!")
			else:
				print("Wrong, try again")
				break

			mode = input(str("Add a new password or view? existing ones? Type 1 to add, 2 to view. Press Q tu exit.")).lower()
			if mode == "q":
				break

			if mode == "1":
				add()
				break
			elif mode == "2":
				view()
				break
			else:
				print("Invalid, try again.")
				continue
	pwd_mng()
manager()