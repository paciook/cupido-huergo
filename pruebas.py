from openpyxl import load_workbook

def main():

	wb = load_workbook(filename="Prueba del match (respuestas).xlsx")
	wb = wb.active

	appls = []

	for row in wb:
		resp = []
		for cell in row:
			resp.append(cell.value)
		appls.append(resp)

	for appl in appls:
		for resp in appl:
			print(resp)
		print("\n")
