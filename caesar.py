
import time

def caesar():
	key = input("Enter Key: ")
	oldarray = list(input("Enter message: "))
	t0 = time.time()
	finish = []
	space = 32
	array = [x.lower() for x in oldarray]
	for i in array:
		if ord('z') < ord(i) + int(key):
			left = (ord(i) + int(key))- ord('z')
			rest = ord('a') + int(left - 1)
			finish.append(chr(rest))
		elif ord(i) == space:
			finish.append(chr(space))
		else:
			b = ord(i) + int(key)
			c = chr(b)
			finish.append(c)
	import os
	file = open("Cipher.txt", "w+")
	for i in finish:
		file.write(i)
	file.close()
	file = open("Cipher.txt", "r")
	########################################################################
	fileloc = "Text-sFile location: " + os.path.dirname(os.path.abspath(__file__))
	ncryptd = "Encrpyted Message: " + file.read()
	#############################################
	print("\n" + "-" * len(ncryptd) + "|")
	print(ncryptd + "|")
	file.close()
	################
	t1 = time.time()
	runtime = "Runtime: " + str(t1-t0)
	##################################
	print("-" * len(runtime) + "|")
	print(runtime + "|")
	print("-" * len(fileloc)+ "|")
	print(fileloc + "|")
	print("-" * len(fileloc) + "|")

caesar()
