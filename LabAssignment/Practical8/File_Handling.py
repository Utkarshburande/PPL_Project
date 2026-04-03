f = open("input.txt", "r")
data = f.read()
f.close()

f = open("output.txt", "w")
f.write(data.upper())
f.close()