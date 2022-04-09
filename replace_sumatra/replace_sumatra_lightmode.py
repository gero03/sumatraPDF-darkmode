from os.path import expanduser
home = expanduser("~")

def lightmode():
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "rt")
	data = fin.read()
	data = data.replace('TextColor = #ffffff', 'TextColor = #000000')
	data = data.replace('BackgroundColor = #000000', 'BackgroundColor = #ffffff')
	fin.close()
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "wt")
	fin.write(data)
	fin.close()
