from os.path import expanduser
home = expanduser("~")

def darkmode():
	#read input file
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "rt")
	#read file contents to string
	data = fin.read()
	#replace all occurrences of the required string
	data = data.replace('TextColor = #000000', 'TextColor = #ffffff')
	data = data.replace('BackgroundColor = #ffffff', 'BackgroundColor = #000000')
	#close the input file
	fin.close()
	#open the input file in write mode
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "wt")
	#overrite the input file with the resulting data
	fin.write(data)
	#close the file
	fin.close()