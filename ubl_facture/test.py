import os
from lxml import etree
from faker import Faker
import pandas as pd

fake = Faker()

# Define namespaces
nsmap = {
    None: "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
    'cac': "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
    'cbc': "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
    'xsi': "http://www.w3.org/2001/XMLSchema-instance",
    'ccts': "urn:un:unece:uncefact:documentation:2",
    'qdt': "urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2",
    'udt': "urn:oasis:names:specification:ubl:schema:xsd:UnqualifiedDataTypes-2"
}

# Function 1: Generates an invoice XML element
def create_ubl_invoice(invoice_data):

    #INFORMATIONS GENERALES DE LA FACTURE UBL
    root = etree.Element('{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}Invoice',  nsmap=nsmap)

    root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation'] = 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd'

    etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UBLVersionID").text = "2.1"
    etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = invoice_data["id"]
    etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate").text = "2023-01-25"
    etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoiceTypeCode").text = "FAC"
    etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}DocumentCurrencyCode").text = "EUR"


    cac_order_reference=etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}OrderReference")
    etree.SubElement(cac_order_reference, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "AA52525252"

    #IDENTITE DU FOURNISSEUR / VENDEUR : TRANSALP

    cac_AccountingSupplierParty=etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingSupplierParty")
    cac_Party=etree.SubElement(cac_AccountingSupplierParty, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party")
    cac_PartyIdentification = etree.SubElement(cac_Party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification")

    cbc_ID_supplier_party=  etree.SubElement(cac_PartyIdentification, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID"); cbc_ID_supplier_party.attrib['schemeName'] = "1" ; cbc_ID_supplier_party.text = "FR123456789"


    cac_PartyName = etree.SubElement(cac_Party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName")
    etree.SubElement(cac_PartyName, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name").text = "SASU ABCD"
    cac_PartyTaxScheme = etree.SubElement(cac_Party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyTaxScheme")
    cac_TaxScheme = etree.SubElement(cac_PartyTaxScheme, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")
    etree.SubElement(cac_TaxScheme, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode").text = "VAT"

    cac_PartyLegalEntity = etree.SubElement(cac_Party, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyLegalEntity")
    etree.SubElement(cac_PartyLegalEntity, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}RegistrationName").text = "ORANGE FRANCE"

    cac_RegistrationAddress=etree.SubElement(cac_PartyLegalEntity, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}RegistrationAddress")
    etree.SubElement(cac_RegistrationAddress, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName").text = "1 rue de la paix"
    etree.SubElement(cac_RegistrationAddress, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName").text = "Paris"
    etree.SubElement(cac_RegistrationAddress, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone").text = "75001"

    cac_country=etree.SubElement(cac_RegistrationAddress, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Country")
    etree.SubElement(cac_country, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode").text = "FR"

    #IDENTITE DU CLIENT / ACHETEUR : ORANGE FRANCE

    cac_AccountingCustomerParty=etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingCustomerParty")

    cac_Party_cust = etree.SubElement(cac_AccountingCustomerParty, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party")
    cac_PartyIdentification_cust = etree.SubElement(cac_Party_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification")

    cbc_ID_Accounting_Customer = etree.SubElement(cac_PartyIdentification_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID") ; cbc_ID_Accounting_Customer.attrib['schemeName'] = "1" ; cbc_ID_Accounting_Customer.text = "FR123456789"

    cac_PartyName_cust=etree.SubElement(cac_Party_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName")

    etree.SubElement(cac_PartyName_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name").text = "SASU ABCD"


    cac_PostalAddress_cust=etree.SubElement(cac_Party_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PostalAddress")
    cac_AddressLine_cust=etree.SubElement(cac_PostalAddress_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AddressLine")
    etree.SubElement(cac_AddressLine_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName").text="12 Place Lucie et Raymond Aubrac 63000 Clermont-Ferrand"
    etree.SubElement(cac_AddressLine_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone").text="63000"
    cac_Country_cust=etree.SubElement(cac_PostalAddress_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Country")
    etree.SubElement(cac_Country_cust, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode").text="FR"

    #LIVRAISON – IDENTITE DU LIVRE, DATE Adresse du client à livré Orange France

    cac_Delivery=etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Delivery")
    cac_DeliveryLocation = etree.SubElement(cac_Delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DeliveryLocation")
    etree.SubElement(cac_DeliveryLocation, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Description").text="12 Place Lucie et Raymond Aubrac 63000 Clermont-Ferrand"
    cac_Address_delivery = etree.SubElement(cac_DeliveryLocation, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Address")
    etree.SubElement(cac_Address_delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName").text="12 Place Lucie et Raymond Aubrac 63000 Clermont-Ferrand"
    etree.SubElement(cac_Address_delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AdditionalStreetName").text="Clermont-Ferrand"
    etree.SubElement(cac_Address_delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName").text="Clermont-Ferrand"
    etree.SubElement(cac_Address_delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone").text="63000"
    cac_Country_delivery=etree.SubElement(cac_Address_delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Country")
    etree.SubElement(cac_Country_delivery, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode").text="FR"

    #PAIEMENT DE LA FACTURE
    cac_PaymentMeans=etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentMeans")
    etree.SubElement(cac_PaymentMeans, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentMeansCode").text="42"
    cac_PayeeFinancialAccount = etree.SubElement(cac_PaymentMeans, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PayeeFinancialAccount")
    etree.SubElement(cac_PayeeFinancialAccount, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text="XLLL022525"

    #Pied de la facture: MONTANT de la TVA

    cac_tax_total = etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxTotal")
    cbc_tax_amount = etree.SubElement(cac_tax_total, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount") ; cbc_tax_amount.attrib['currencyID'] = "EUR"

    # cac_TaxSubtotal = etree.SubElement(cac_tax_total, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal")
    # cbc_TaxableAmount = etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxableAmount") ; cbc_TaxableAmount.attrib['currencyID'] = "EUR" ; cbc_TaxableAmount.text = "150.00"
    # cbc_TaxAmount = etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount") ; cbc_TaxAmount.attrib['currencyID'] = "EUR" ; cbc_TaxAmount.text = "30.00"
    # cbc_percent = etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent") ; cbc_percent.text = "20.00"
    #
    # cac_TaxCategory= etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory")
    # cac_TaxScheme_pied= etree.SubElement(cac_TaxCategory, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")
    # etree.SubElement(cac_TaxScheme_pied, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text="VAT"

    cac_LegalMonetaryTotal = etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}LegalMonetaryTotal")
    cbc_TaxExclusiveAmount = etree.SubElement(cac_LegalMonetaryTotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxExclusiveAmount") ; cbc_TaxExclusiveAmount.attrib['currencyID'] = "EUR" ; cbc_TaxExclusiveAmount.text = "150.00"
    cbc_TaxInclusiveAmount = etree.SubElement(cac_LegalMonetaryTotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxInclusiveAmount") ; cbc_TaxInclusiveAmount.attrib['currencyID'] = "EUR" ; cbc_TaxInclusiveAmount.text = "180.00"

    cbc_PayableAmount = etree.SubElement(cac_LegalMonetaryTotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PayableAmount") ; cbc_TaxInclusiveAmount.attrib['currencyID'] = "EUR" ; cbc_TaxInclusiveAmount.text = "180.00"



    #Les lignes de la facture
    cac_InvoiceLine = etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoiceLine")
    etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "2"
    cac_InvoicedQuantity = etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoicedQuantity") ; cac_InvoicedQuantity.attrib['unitCode'] = "MTR" ; cac_InvoicedQuantity.text = "5.0"
    cbc_LineExtensionAmount = etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineExtensionAmount") ; cbc_LineExtensionAmount.attrib['currencyID'] = "EUR" ; cbc_LineExtensionAmount.text = "150.00"

    cac_OrderLineReference= etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}OrderLineReference")
    etree.SubElement(cac_OrderLineReference, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineID").text = "2"
    cac_DespatchLineReference= etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DespatchLineReference")
    etree.SubElement(cac_DespatchLineReference, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineID").text = "1"

    cac_Item = etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Item")
    etree.SubElement(cac_Item, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Description").text = "Cable électrique"

    cac_StandardItemIdentification = etree.SubElement(cac_Item, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}StandardItemIdentification")
    etree.SubElement(cac_StandardItemIdentification, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "123456789"

    cac_ClassifiedTaxCategory= etree.SubElement(cac_Item, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ClassifiedTaxCategory")
    etree.SubElement(cac_ClassifiedTaxCategory, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent").text = "20.0"
    cac_TaxScheme_Line = etree.SubElement(cac_ClassifiedTaxCategory, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")
    etree.SubElement(cac_TaxScheme_Line, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "VAT"

    cac_price = etree.SubElement(cac_InvoiceLine, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Price")
    etree.SubElement(cac_price, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PriceAmount").text = "30.00"
    etree.SubElement(cac_price, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}BaseQuantity").text = "5.0"

    transalp_invoice = pd.read_csv("C:/Users/MohamedBassirouCissé/Documents/Transalp_ubl/transalp_invoice.csv")

    tax_amount_sum = transalp_invoice['TVA'].sum(); cbc_tax_amount.text = str(tax_amount_sum)
    tax_exclude_amount_sum = transalp_invoice['HT'].sum(); cbc_TaxExclusiveAmount.text = str(tax_exclude_amount_sum)
    tax_include_amount_sum = transalp_invoice['TTC'].sum(); cbc_TaxInclusiveAmount.text = str(tax_include_amount_sum)
    payable_amount_sum = transalp_invoice['TTC'].sum(); cbc_PayableAmount.text = str(payable_amount_sum)

    print("tax_amount_sum",tax_amount_sum)

    for index, row in transalp_invoice.iterrows():
        cac_TaxSubtotal = etree.SubElement(cac_tax_total,"{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal")
        cbc_TaxableAmount = etree.SubElement(cac_TaxSubtotal,"{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxableAmount") ; cbc_TaxableAmount.attrib['currencyID'] = "EUR"; cbc_TaxableAmount.text = str(row['HT'])
        cbc_TaxAmount = etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount"); cbc_TaxAmount.attrib['currencyID'] = "EUR"; cbc_TaxAmount.text = str(row['TVA'])
        cbc_percent = etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent"); cbc_percent.text = str(row['code TVA'])

        cac_TaxCategory = etree.SubElement(cac_TaxSubtotal, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory")
        cac_TaxScheme_pied = etree.SubElement(cac_TaxCategory, "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")
        etree.SubElement(cac_TaxScheme_pied, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "VAT"




        #print("row['TVA']:", type(row['TVA']))




    #print("transalp_invoice",transalp_invoice)


    # etree.SubElement(root, "IssueDate").text = invoice_data["issue_date"]
    #
    # # Add party name and address details
    # party = etree.SubElement(root, "AccountingCustomerParty")
    # party_name = etree.SubElement(party, "PartyName")
    # etree.SubElement(party_name, "Name").text = invoice_data["name"]
    # address = etree.SubElement(party, "PostalAddress")
    # etree.SubElement(address, "StreetName").text = invoice_data["street"]
    # etree.SubElement(address, "CityName").text = invoice_data["city"]
    # etree.SubElement(address, "CountrySubentity").text = invoice_data["state"]
    # etree.SubElement(address, "PostalZone").text = invoice_data["zipcode"]
    # etree.SubElement(address, "Country").text = invoice_data["country"]
    #
    # # Add invoice lines with products
    # # for product in invoice_data["products"]:
    # #     invoice_line = etree.SubElement(root, "InvoiceLine")
    # #     etree.SubElement(invoice_line, "ID").text = product["id"]
    # #     etree.SubElement(invoice_line, "InvoicedQuantity").text = str(product["quantity"])
    # #     etree.SubElement(invoice_line, "LineExtensionAmount").text = str(product["price"])
    # #
    # # # Add VAT and total amount
    # # etree.SubElement(root, "TaxTotal").text = str(invoice_data["vat"])
    # # etree.SubElement(root, "LegalMonetaryTotal").text = str(invoice_data["total_amount"])

    return root
# Function 2: Saves the invoice XML element to a file
def save_invoice_to_file(invoice, file_path):
    tree = etree.ElementTree(invoice)
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="utf-8")

def generate_random_product():
    return {
        "id": str(fake.random_int(min=1000, max=9999)),
        "name": fake.bs(),
        "quantity": fake.random_int(min=1, max=10),
        "price": round(fake.random.uniform(1, 100), 2)
    }


# Function 3: Generates random invoice data
def create_random_invoice_data():
    products = [generate_random_product() for _ in range(fake.random_int(min=1, max=5))]
    subtotal = sum(product["price"] for product in products)
    vat = round(subtotal * 0.2, 2)
    total_amount = subtotal + vat

    return {
        "id": str(fake.random_int(min=1000, max=9999)),
        "issue_date": str(fake.date_between(start_date='-30d', end_date='today')),
        "name": fake.name(),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zipcode": fake.zipcode(),
        "country": fake.country_code(),
        "products": products,
        "vat": vat,
        "total_amount": total_amount
    }

if __name__ == "__main__":
    os.makedirs("invoices", exist_ok=True)

    for i in range(1):
        invoice_data = create_random_invoice_data()
        invoice = create_ubl_invoice(invoice_data)
        save_invoice_to_file(invoice, f"invoices/invoice_{invoice_data['id']}.xml")