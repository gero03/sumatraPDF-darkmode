import replace_sumatra_darkmode
import replace_sumatra_lightmode

mode=str(input('type "d" for darkmode and "l" for lightmode: '))

if mode=='d':
	replace_sumatra_darkmode.darkmode()
elif mode=='l':
	replace_sumatra_lightmode.lightmode()
else:
	print("error")