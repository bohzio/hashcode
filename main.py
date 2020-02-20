f = open("a_example.txt", "r")

books = None
libraries = None
days = None

first_recod = f.readline()
books = first_recod.split(" ")[0]
libraries = first_recod.split(" ")[1]
days = first_recod.split(" ")[2]

