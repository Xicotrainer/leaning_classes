from io import open

def file_w(file_name):
	
	file = open(file_name, "w")

	print(file_name, "was created")
	gretting = "Hello there!!! \nToday is Wednesday"
	
	file.write(gretting)
	file.write("\nJust a dummy line")
	file.write("\nJust another dummy line")
	file.close()


#def file_w():
#	pass:


def main():
	#Into the same folder
	file_name = "file_text.txt"

	print("We area going to create a new file ussing python")
	file_name = input("Please, type its name: ")

	file_w(file_name+".txt")


main()