# This program generates a drop down menu of states.

Abbrev=[' ',\
'AL', \
'AK', \
'AZ', \
'AR', \
'CA', \
'CO', \
'CT', \
'DE', \
'FL', \
'GA', \
'HI', \
'ID', \
'IL', \
'IN', \
'IA', \
'KS', \
'KY', \
'LA', \
'ME', \
'MD', \
'MA', \
'MI', \
'MN', \
'MS', \
'MO', \
'MT', \
'NE', \
'NV', \
'NH', \
'NJ', \
'NM', \
'NY', \
'NC', \
'ND', \
'OH', \
'OK', \
'OR', \
'PA', \
'RI', \
'SC', \
'SD', \
'TN', \
'TX', \
'UT', \
'VT', \
'VA', \
'WA', \
'WV', \
'WI', \
'WY']

state=[' ',\
'Alabama', \
'Alaska', \
'Arizona', \
'Arkansas', \
'California', \
'Colorado', \
'Connecticut', \
'Delaware', \
'Florida', \
'Georgia', \
'Hawaii', \
'Idaho', \
'Illinois', \
'Indiana', \
'Iowa', \
'Kansas', \
'Kentucky', \
'Louisiana', \
'Maine', \
'Maryland', \
'Massachussetts', \
'Michigan', \
'Minnesota', \
'Mississippi', \
'Missouri', \
'Montana', \
'Nebraska', \
'Nevada', \
'New Hampshire', \
'New Jersey', \
'New Mexico', \
'New York', \
'North Carolina', \
'North Dakota', \
'Ohio', \
'Oklahoma', \
'Oregon', \
'Pennsylvania', \
'Rhode Island', \
'South Carolina', \
'South Dakota', \
'Tennessee', \
'Texas', \
'Utah', \
'Vermont', \
'Virginia', \
'Washington', \
'West Virginia', \
'Wisconsin', \
'Wyoming']

file = open("C:\Users\Paida\Desktop\PythonLessons\States.html",'w')
file.write('<select name="States">')
for Abbrev, state in zip(Abbrev, state):
   file.write("\t\t\t<option value='{}'>{}</option>".format(Abbrev,state))
file.write("<select>")
file.close()
