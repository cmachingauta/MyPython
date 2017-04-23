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

import codecs
#
file = codecs.open("C:\Users\Paida\Desktop\PythonLessons\UnicodeCountries.html",'w','utf-8-sig')
#arguments 'w' -> for only writing. An existing file with the same name will be erased.
# 'a' would append to the file
# 'utf-8-sig' ->: On encoding a utf-8 encoded BOM will be prepended to the UTF-8 encoded bytes

#Print to file
##print >>file, '<select name="Countries">'
##for ISO_CODE, country in zip(ISO_CODE, country):
##   print >>file, u"\t\t\t<option value='{}'>{}</option>".format(ISO_CODE,country)
##print >>file, "<select>"

# Write to file 
file.write('<select name="Countries">')
for ISO_CODE, country in zip(ISO_CODE, country):
   file.write(u"\t\t\t<option value='{}'>{}</option>".format(ISO_CODE,country))
file.write("<select>")
file.close()
