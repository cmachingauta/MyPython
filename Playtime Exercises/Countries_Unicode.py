# -*- coding: -utf-8 -*-
#

ISO_CODE=[' ',\
'DZA', \
'AGO', \
'BEN', \
'BWA', \
'BFA', \
'BDI', \
'CMR', \
'CPV', \
'CAF', \
'TCD', \
'COM', \
'COG', \
'COD', \
'DJI', \
'EGY', \
'GNQ', \
'ERI', \
'ETH', \
'GAB', \
'GMB', \
'GHA', \
'GNB', \
'GIN', \
'CIV', \
'KEN', \
'LSO', \
'LBR', \
'LBY', \
'MDG', \
'MWI', \
'MLI', \
'MRT', \
'MUS', \
'MAR', \
'MOZ', \
'NAM', \
'NER', \
'NGA', \
'RWA', \
'STP', \
'SEN', \
'SYC', \
'SLE', \
'SOM', \
'ZAF', \
'SSD', \
'SDN', \
'SWZ', \
'TZA', \
'TGO', \
'TUN', \
'UGA', \
'ZMB', \
'TZA', \
'ZWE']

country=[' ',\
'Algeria', \
'Angola', \
'Benin', \
'Botswana', \
'Burkina Faso', \
'Burundi', \
'Cameroon', \
'Cape Verde', \
'Central African Rep', \
'Chad', \
'Comoros', \
'Congo', \
'Dem. Rep. Congo', \
'Djibouti', \
'Egypt', \
'Equatorial Guinea', \
'Eritrea', \
'Ethiopia', \
'Gabon', \
'Gambia', \
'Ghana', \
'Guinea Bissau', \
'Guinea', \
u'Côte d’Ivoire', \
'Kenya', \
'Lesotho', \
'Liberia', \
'Libya', \
'Madagascar', \
'Malawi', \
'Mali', \
'Mauritania', \
'Mauritius', \
'Morocco', \
'Mozambique', \
'Namibia', \
'Niger', \
'Nigeria', \
'Rwanda', \
u'São Tomé and Principe', \
'Senegal', \
'Seychelles', \
'Sierra Leone', \
'Somalia', \
'South Africa', \
'South Sudan', \
'Sudan', \
'Swaziland', \
'Tanzania', \
'Togo', \
'Tunisia', \
'Uganda', \
'Zambia', \
'Zanzibar', \
'Zimbabwe']

# opening a text file in python:
# import codecs
# f = codecs.open(filename, encoding="utf-8") > when you open a file that has certain encoding, you should always use the codecs module, rather than doing f = open(filename)
#arguments 'w' -> for only writing. An existing file with the same name will be erased. 'a' would append to the file
# 'utf-8-sig' ->: In some areas, it is also convention to use a Byte Order marker (BOM) at the start of UTF-8 encoded files;
#the name is misleading since UTF-8 is not byte-order dependent.The mark simply announces that the file
#is encoded in UTF-8. Use the ‘utf-8-sig’ codec to automatically skip the mark if present for reading such files

import codecs
file = codecs.open("C:\Users\Paida\Desktop\PythonLessons\UnicodeCountries.html",'w','utf-8-sig')

#Option 1: Print to file
##print >>file, '<select name="Countries">'
##for ISO_CODE, country in zip(ISO_CODE, country):
##   print >>file, u"\t\t\t<option value='{}'>{}</option>".format(ISO_CODE,country)
##print >>file, "<select>"

#Option 2: Write to file 
file.write('<select name="Countries">')
for ISO_CODE, country in zip(ISO_CODE, country):
   file.write(u"\t\t\t<option value='{}'>{}</option>".format(ISO_CODE,country))
file.write("<select>")
file.close()
