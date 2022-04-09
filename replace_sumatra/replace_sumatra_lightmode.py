from os.path import expanduser
home = expanduser("~")

def lightmode():
	#read input file
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "rt")
	#read file contents to string
	data = fin.read()
	#replace all occurrences of the required string
	data = data.replace('TextColor = #ffffff', 'TextColor = #000000')
	data = data.replace('BackgroundColor = #000000', 'BackgroundColor = #ffffff')
	#close the input file
	fin.close()
	#open the input file in write mode
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "wt")
	#overrite the input file with the resulting data
	fin.write(data)
	#close the file
	fin.close()