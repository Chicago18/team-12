import os
import sys
import fdfgen
import sqlite3
import cma as model

#connection = sqlite3.connect("sql/data.sql")
#cursor = connection.cursor()

#get the username of the user
#cursor.execute("SELECT * FROM parent WHERE username=username")
#parent_fields = cursor.description()
#parentdata = cursor.fetchall()
#cursor.execute("SELECT * FROM student WHERE parentid=username")
#student_fields = cursor.description()
#studentdata = cursor.fetchall()

parent_fields = ['username','firstname','lastname','familytype','housingstatus','foodstamps','reducedlunch','insurance','referral','clientid','incomesource1','incomesource2','incomesource3','incomesource4','incomesource5','incomesource6','incomesource7','incomesource8']
parentdata = ['pbatt','pgty','aspdhj','relative','own','n','n','y','County Office','13632','y','n','n','n','y','n','n','n']
student_fields = ['username','firstname','lastname','middleinitial','parentid','gender','age','birthdate','phonenumber','ethnicity','race','currentgrade','school','disability','communityarea','ward','registered']
studentdata = ['jbatt','Billy','Smith','R','mommy','male','20','March 21, 1998','908-555-2115','white','n/a','14','Rutgers','no','Piscataway','asdflkj','yes']

#def parse_form(parentdata, studentdata, parent_fields, student_fields):
del parentdata[0:3]; del parent_fields[0:3]
del studentdata[0]; del student_fields[0]
del studentdata[-1]; del student_fields[-1]
del studentdata[3]; del student_fields[3]

all_fields = []
#prepare for code gore.
text_fields = ['firstname', 'lastname', 'middleinitial', 'phonenumber', 'age', 'birthdate', 
	'currentgrade', 'school', 'disability', 'communityarea', 'ward', 
	'race', 'referral', 'clientid', 'hisp', 'nothisp', 
	'genderm', 'genderf', 'native', 'asian', 'black', 
	'hawaiian', 'white', 'other', 'disyes', 'disno', 
	'singlemom', 'singledad', 'twoparent', 'indyouth', 'relative', 
	'guardian', 'rent', 'own', 'homeless', 'temp', 
	'fsyes', 'fsno', 'rlyes', 'rlno', 'insyes', 
	'insno', 'incomesource1', 'incomesource2', 'incomesource3', 'incomesource4', 
	'incomesource5', 'incomesource6', 'incomesource7', 'incomesource8']

for i in range(len(text_fields)):
	if (text_fields[i] in student_fields):
		field_value = studentdata[student_fields.index(text_fields[i])]
		all_fields.append((text_fields[i], field_value))

	elif (text_fields[i] in parent_fields):
		field_value = parentdata[parent_fields.index(text_fields[i])]
		all_fields.append((text_fields[i], field_value))

famtype = parentdata[0]
print(famtype)
if (famtype[0] == 's'):
	if (famtype[-1] == 'd'): all_fields.append((text_fields[27], 'x'))
	else: all_fields.append((text_fields[26], 'x'))
if (famtype[0] == 't'): all_fields.append((text_fields[28], 'x'))
if (famtype[0] == 'i'): all_fields.append((text_fields[29], 'x'))
if (famtype[0] == 'r'): all_fields.append((text_fields[30], 'x'))
if (famtype[0] == 'g'): all_fields.append((text_fields[31], 'x'))

house = parentdata[1]
if (house[0] == 'r'): all_fields.append((text_fields[32], 'x'))
if (house[0] == 'o'): all_fields.append((text_fields[33], 'x'))
if (house[0] == 'h'): all_fields.append((text_fields[34], 'x'))
if (house[0] == 't'): all_fields.append((text_fields[35], 'x'))

stamps = parentdata[2]
if (stamps[0] == 'y'): all_fields.append((text_fields[36], 'x'))
else: all_fields.append((text_fields[37], 'x'))

lunch = parentdata[3]
if (lunch[0] == 'y'): all_fields.append((text_fields[38], 'x'))
else: all_fields.append((text_fields[39], 'x'))

insurance = parentdata[4]
if (insurance[0] == 'y'): all_fields.append((text_fields[40], 'x'))
else: all_fields.append((text_fields[41], 'x'))

if (parentdata[-1] == 'y'): all_fields.append((text_fields[49], 'x'))
else: all_fields.append((text_fields[49], ''))
if (parentdata[-2] == 'y'): all_fields.append((text_fields[48], 'x'))
else: all_fields.append((text_fields[48], ''))
if (parentdata[-3] == 'y'): all_fields.append((text_fields[47], 'x'))
else: all_fields.append((text_fields[47], ''))
if (parentdata[-4] == 'y'): all_fields.append((text_fields[46], 'x'))
else: all_fields.append((text_fields[46], ''))
if (parentdata[-5] == 'y'): all_fields.append((text_fields[45], 'x'))
else: all_fields.append((text_fields[45], ''))
if (parentdata[-6] == 'y'): all_fields.append((text_fields[44], 'x'))
else: all_fields.append((text_fields[44], ''))
if (parentdata[-7] == 'y'): all_fields.append((text_fields[43], 'x'))
else: all_fields.append((text_fields[43], ''))
if (parentdata[-8] == 'y'): all_fields.append((text_fields[42], 'x'))
else: all_fields.append((text_fields[42], ''))

ethn = studentdata[7]
if (ethn[0:2] == 'hi'): all_fields.append((text_fields[14], 'x'))
else: all_fields.append((text_fields[15], 'x'))
if (ethn[0:2] == 'am'): all_fields.append((text_fields[18], 'x'))
if (ethn[0:2] == 'as'): all_fields.append((text_fields[19], 'x'))
if (ethn[0:2] == 'bl'): all_fields.append((text_fields[20], 'x'))
if (ethn[0:2] == 'ha'): all_fields.append((text_fields[21], 'x'))
if (ethn[0:2] == 'wh'): all_fields.append((text_fields[22], 'x'))

gender = studentdata[3]
if (gender[0] == 'm'): all_fields.append((text_fields[16], 'x'))
if (gender[0] == 'f'): all_fields.append((text_fields[17], 'x'))


fdf_data = fdfgen.forge_fdf("", all_fields, [], [], [])
fdf_file = open("file_fdf.fdf", "wb")
fdf_file.write(fdf_data)
fdf_file.close()

pdftk_cmd = "pdftk simpleform1.pdf fill_form file_fdf.fdf output output_pdf.pdf flatten"
os.system(pdftk_cmd)