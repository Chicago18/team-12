import os
import sys
import fdfgen

field_names = ['studentlname', 'studentfname']
all_fields = []

for i in range(len(field_names)):
	field_value = input(field_names[i] + ": ")
	all_fields.append((field_names[i], field_value))

fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf", "wb")
fdf_file.write(fdf_data)
fdf_file.close()

pdftk_cmd = "pdftk simpleform1.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
os.system(pdftk_cmd)

