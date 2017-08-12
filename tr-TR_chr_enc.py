kod_çözüm=["UTF-8","cp1254","latin-1","ASCII"]

karakter=input("Bir karakter girin: ")

for x in kod_çözüm:
	try:
		print("'{}' karakteri {} ile {} olarak "
			"ve {} sayısıyla temsil edilir.".format(karakter,x,karakter.encode(x),ord(karakter)))

	except UnicodeEncodeError:
		print("'{}' karakteri {} ile temsil edilemez!".format(karakter,x))