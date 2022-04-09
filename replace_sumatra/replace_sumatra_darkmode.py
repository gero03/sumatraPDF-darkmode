from os.path import expanduser
home = expanduser("~")

def darkmode():
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "rt")
	data = fin.read()
	data = data.replace('TextColor = #000000', 'TextColor = #ffffff')
	data = data.replace('BackgroundColor = #ffffff', 'BackgroundColor = #000000')
	fin.close()
	fin = open(str(home)+"/AppData/Local/SumatraPDF/SumatraPDF-settings.txt", "wt")
	fin.write(data)
	fin.close()
