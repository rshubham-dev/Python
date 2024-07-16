st = "Get into the world of programming"
f = open("write.txt", "w")
f.write(st)
f.close()

fr = open("write.txt", "r")
data = fr.read()
dataline = fr.readline()
datalines = fr.readlines()
print(data)
print(dataline)
print(datalines)
fr.close()