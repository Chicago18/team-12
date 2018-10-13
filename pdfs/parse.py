import os
import sys
import fdfgen
import sqlite3

connection = sqlite3.connect("../sql/data.sql")
cursor = connection.cursor()

#get the username of the user
cursor.execute("SELECT * FROM parent WHERE username=username")
parent_fields = cursor.description()
parentdata = cursor.fetchall()
cursor.execute("SELECT * FROM student WHERE parentid=username")
student_fields = cursor.description()
studentdata = cursor.fetchall()

#parent_fields = ['username','firstname','lastname','familytype','housingstatus','foodstamps','reducedlunch','insurance','referral','clientid','incomesource1','incomesource2','incomesource3','incomesource4','incomesource5','incomesource6','incomesource7','incomesource8']
#parentdata = ['pbatt','pgty','aspdhj','singlemom','own','no','no','yes','County Office','13632','','','','','','','','']
#student_fields = ['username','firstname','lastname','middleinitial','parentid','gender','age','birthdate','phonenumber','ethnicity','race','currentgrade','school','disability','communityarea','ward','registered']
#studentdata = ['jbatt','Jacob','Batipl','R','mommy','male','20','March21, 1998','908-528-2412','white','n/a','14','Rutgers','no','Piscataway','asdflkj','yes']

#def parse_form(parentdata, studentdata, parent_fields, student_fields):
del parentdata[0:2]; del parent_fields[0:2]
del studentdata[0]; del student_fields[0]
del studentdata[-1]; del student_fields[-1]
del studentdata[3]; del student_fields[3]

all_fields = []
#prepare for code gore.
text_fields = ['firstname', 'lastname', 'middleinitial', 'phonenumber', 'age', 'birthdate', 
	'currentgrade', 'school', 'disability', 'communityarea', 'ward', 'race', 'referral', 
	'clientid', 'hisp', 'nothisp', 'genderm', 'genderf', 'native', 'asian', 'black', 
	'hawaiian', 'white', 'other', 'disyes', 'disno', 'singlemom', 'singledad', 'twoparent', 
	'indyouth', 'relative', 'guardian', 'rent', 'own', 'homeless', 'temp', 'fsyes', 'fsno', 
	'rlyes', 'rlno', 'insyes', 'insno', 'incomesource1', 'incomesource2', 'incomesource3', 
	'incomesource4', 'incomesource5', 'incomesource6', 'incomesource7', 'incomesource8']

for i in range(len(text_fields)):
	if (text_fields[i] in student_fields):
		field_value = studentdata[student_fields.index(text_fields[i])]
		all_fields.append((text_fields[i], field_value))

	elif (text_fields[i] in parent_fields):
		field_value = parentdata[parent_fields.index(text_fields[i])]
		all_fields.append((text_fields[i], field_value))

fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf", "wb")
fdf_file.write(fdf_data)
fdf_file.close()

pdftk_cmd = "pdftk simpleform1.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
os.system(pdftk_cmd)