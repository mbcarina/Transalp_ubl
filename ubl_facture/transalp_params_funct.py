from datetime import datetime
current_datetime = datetime.now()


invoice_cbc_id = str(current_datetime.year) + str(current_datetime.month) + str(current_datetime.day) + str(current_datetime.hour) + str(current_datetime.minute) + str(current_datetime.second) #+ str(current_datetime.microsecond)
invoice_cbc_issueDate = current_datetime.strftime('%Y-%m-%d')
cbc_invoice_typeCode = 380
cbc_document_currencyCode = 'EUR'
ID_supplier_fiscal = 'FR39672004660'
Supplier_name= "TRANSALPES COMPOSITE"
TaxTypeCode = 'VAT'
StreetName = 'Plate-forme logistique les Echerolles'
CityName = 'Saint-Loup'
PostalZone = '03150'
CountryName = 'FR'
Unitemesure='MTR'