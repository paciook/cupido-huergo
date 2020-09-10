import utilities as ut

FILE_NAME = "sample.xlsx"

def main():

	sheet = ut.load_sheet(FILE_NAME)
	
	appls = ut.load_appls(sheet)

	for x in range(len(appls)):
		aux = appls[x:]
		for appl in aux:
			ERROR = ut.match(appls[x], appl)

			if ERROR != 0:
				print(ERROR)
				break
