import win32api

def caesar():
	key = input("Enter Key: ")
	array = input("Enter message: ")
	finish = []
	space = 32

	for i in list(array):
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
	file = open("Cipher.txt", "w")
	for i in finish:
		file.write(i)
	file.close()

caesar()
