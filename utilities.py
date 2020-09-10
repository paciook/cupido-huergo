from openpyxl import load_workbook
import applicant


def load_appls(sheet):
	appls = []
	for row in sheet:
		appls.append(Appl(row))

	return appls


def load_sheet(name):
	"""
	Lo dice el nombre, titán
	"""
    workbook = load_workbook(filename=name)
    return workbook.active


def match(apl1, apl2):
	"""
	Recibo dos aplicantes y los posiciono (o no) dentro
	del top 5 del otro con el % ponderado de 
	sus coincidencias. Devuelvo Código de error.
	"""
	apl1.top(apl2)
	apl2.top(apl1)


def check(appl1, appl2):
	"""
	Recibo dos aplicantes y devuelvo el % ponderado de
	sus coincidencias
	"""
	LEN_RESP = len(appl1.ans)
	resp1 = appl1.ans
	resp2 = appl2.ans
	coin = 0
	for x in range(LEN_RESP):
		if resp2[x] == resp1[x]:
			coin += 1 / LEN_RESP

	return coin * 100