import os
import shutil

from lxml import etree
from faker import Faker
import pandas as pd
import transalp_params_funct as tpf
import orange_params_funct as opf
import params_tech as ptf
from pathlib import Path

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
    # INFORMATIONS GENERALES DE LA FACTURE UBL
    # /Invoice
    root = etree.Element('{urn:oasis:names:specification:ubl:schema:xsd:Invoice-2}Invoice', nsmap=nsmap)
    root.attrib[
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation'] = 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 http://docs.oasis-open.org/ubl/os-UBL-2.1/xsd/maindoc/UBL-Invoice-2.1.xsd'

    # /Invoice/cbc:UBLVersionID
    etree.SubElement(root,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UBLVersionID").text = opf.UBLVersionID

    # /Invoice/cbc:ID
    etree.SubElement(root,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = tpf.invoice_cbc_id

    # /Invoice/cbc:IssueDate
    etree.SubElement(root,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IssueDate").text = tpf.invoice_cbc_issueDate

    # /Invoice/cbc:InvoiceTypeCode
    etree.SubElement(root,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoiceTypeCode").text = str(
        tpf.cbc_invoice_typeCode)

    # /Invoice/cbc:DocumentCurrencyCode
    etree.SubElement(root,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}DocumentCurrencyCode").text = tpf.cbc_document_currencyCode

    # /Invoice/cac:OrderReference
    cac_order_reference = etree.SubElement(root,
                                           "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}OrderReference")

    # IDENTITE DU FOURNISSEUR / VENDEUR : TRANSALP

    # /Invoice/cac:AccountingSupplierParty
    cac_AccountingSupplierParty = etree.SubElement(root,
                                                   "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingSupplierParty")

    # /Invoice/cac:AccountingSupplierParty/cac:Party
    cac_Party = etree.SubElement(cac_AccountingSupplierParty,
                                 "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification
    cac_PartyIdentification = etree.SubElement(cac_Party,
                                               "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID
    cbc_ID_supplier_party = etree.SubElement(cac_PartyIdentification,
                                             "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID");
    cbc_ID_supplier_party.attrib['schemeName'] = "1";
    cbc_ID_supplier_party.text = tpf.ID_supplier_fiscal

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName
    cac_PartyName = etree.SubElement(cac_Party,
                                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name
    etree.SubElement(cac_PartyName,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name").text = tpf.Supplier_name

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/
    cac_PartyTaxScheme = etree.SubElement(cac_Party,
                                          "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyTaxScheme")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme
    cac_TaxScheme = etree.SubElement(cac_PartyTaxScheme,
                                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:TaxTypeCode
    etree.SubElement(cac_TaxScheme,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode").text = tpf.TaxTypeCode

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/
    cac_PartyLegalEntity = etree.SubElement(cac_Party,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyLegalEntity")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationName
    etree.SubElement(cac_PartyLegalEntity,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}RegistrationName").text = tpf.Supplier_name

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress
    cac_RegistrationAddress = etree.SubElement(cac_PartyLegalEntity,
                                               "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}RegistrationAddress")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:StreetName
    etree.SubElement(cac_RegistrationAddress,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName").text = tpf.StreetName

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName
    etree.SubElement(cac_RegistrationAddress,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName").text = tpf.CityName

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:PostalZone
    etree.SubElement(cac_RegistrationAddress,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone").text = tpf.PostalZone

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cac:Country
    cac_country = etree.SubElement(cac_RegistrationAddress,
                                   "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Country")

    # /Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cac:Country/cbc:IdentificationCode
    etree.SubElement(cac_country,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode").text = tpf.CountryName

    # IDENTITE DU CLIENT / ACHETEUR : ORANGE FRANCE

    # /Invoice/cac:AccountingCustomerParty
    cac_AccountingCustomerParty = etree.SubElement(root,
                                                   "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingCustomerParty")

    # /Invoice/cac:AccountingCustomerParty/cac:Party
    cac_Party_cust = etree.SubElement(cac_AccountingCustomerParty,
                                      "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party")

    # /Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification
    cac_PartyIdentification_cust = etree.SubElement(cac_Party_cust,
                                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification")

    # /Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID
    cbc_ID_Accounting_Customer = etree.SubElement(cac_PartyIdentification_cust,
                                                  "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID");
    cbc_ID_Accounting_Customer.attrib['schemeName'] = "1";
    cbc_ID_Accounting_Customer.text = opf.customer_id_fiscal

    # /Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName
    cac_PartyName_cust = etree.SubElement(cac_Party_cust,
                                          "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName")

    # /Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name
    etree.SubElement(cac_PartyName_cust,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name").text = opf.customer_name

    # Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress
    cac_PostalAddress_cust = etree.SubElement(cac_Party_cust,
                                              "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PostalAddress")

    # Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine
    cac_AddressLine_cust = etree.SubElement(cac_PostalAddress_cust,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AddressLine")

    # Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:AddressLine/cbc:StreetName
    etree.SubElement(cac_AddressLine_cust,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName").text = opf.customer_streetName

    # Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone
    etree.SubElement(cac_AddressLine_cust,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone").text = opf.customer_postalZone

    # Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country
    cac_Country_cust = etree.SubElement(cac_PostalAddress_cust,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Country")

    # Invoice/cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode
    etree.SubElement(cac_Country_cust,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode").text = opf.customer_countryName

    # LIVRAISON – IDENTITE DU LIVRE, DATE Adresse du client à livré Orange France
    # /Invoice/cac:Delivery
    cac_Delivery = etree.SubElement(root,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Delivery")

    # /Invoice/cac:Delivery/cac:DeliveryLocation
    cac_DeliveryLocation = etree.SubElement(cac_Delivery,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DeliveryLocation")

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cbc:Description
    etree.SubElement(cac_DeliveryLocation,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Description").text = opf.customer_name

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address
    cac_Address_delivery = etree.SubElement(cac_DeliveryLocation,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Address")

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:StreetName
    etree.SubElement(cac_Address_delivery,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName").text = opf.customer_streetName

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:AdditionalStreetName
    etree.SubElement(cac_Address_delivery,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AdditionalStreetName").text = opf.customer_streetName

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:CityName
    etree.SubElement(cac_Address_delivery,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName").text = opf.customer_cityName

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address/cbc:PostalZone
    etree.SubElement(cac_Address_delivery,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone").text = opf.customer_postalZone

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address/cac:Country
    cac_Country_delivery = etree.SubElement(cac_Address_delivery,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Country")

    # /Invoice/cac:Delivery/cac:DeliveryLocation/cac:Address/cac:Country/cbc:IdentificationCode
    etree.SubElement(cac_Country_delivery,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode").text = opf.customer_countryName

    # PAIEMENT DE LA FACTURE
    # /Invoice/cac:PaymentMeans
    cac_PaymentMeans = etree.SubElement(root,
                                        "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentMeans")

    # /Invoice/cac:PaymentMeans/cbc:PaymentMeansCode
    etree.SubElement(cac_PaymentMeans,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PaymentMeansCode").text = opf.customer_paymentMeansCode

    # /Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount
    cac_PayeeFinancialAccount = etree.SubElement(cac_PaymentMeans,
                                                 "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PayeeFinancialAccount")

    # /Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID
    etree.SubElement(cac_PayeeFinancialAccount,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = opf.customer_iban

    # Pied de la facture: MONTANT de la TVA

    # /Invoice/cac:TaxTotal
    cac_tax_total = etree.SubElement(root,
                                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxTotal")
    # /Invoice/cac:TaxTotal/cbc:TaxAmount
    cbc_tax_amount = etree.SubElement(cac_tax_total,
                                      "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount");
    cbc_tax_amount.attrib['currencyID'] = "EUR"

    # Pied de la facture: MONTANT TOTAL DE LA FACTURE
    # /Invoice/cac:LegalMonetaryTotal
    cac_LegalMonetaryTotal = etree.SubElement(root,
                                              "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}LegalMonetaryTotal")

    # /Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount
    cbc_TaxExclusiveAmount = etree.SubElement(cac_LegalMonetaryTotal,
                                              "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxExclusiveAmount");
    cbc_TaxExclusiveAmount.attrib['currencyID'] = "EUR";
    cbc_TaxExclusiveAmount.text = ""

    # /Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount
    cbc_TaxInclusiveAmount = etree.SubElement(cac_LegalMonetaryTotal,
                                              "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxInclusiveAmount");
    cbc_TaxInclusiveAmount.attrib['currencyID'] = "EUR";
    cbc_TaxInclusiveAmount.text = ""

    # /Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount
    cbc_PayableAmount = etree.SubElement(cac_LegalMonetaryTotal,
                                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PayableAmount");
    cbc_TaxInclusiveAmount.attrib['currencyID'] = "EUR";
    cbc_TaxInclusiveAmount.text = ""

    # Recuperation les factures de Transalp dans le dossier InputFile et la lecture en Pandas
    if invoice_data.endswith('.csv') or invoice_data.endswith('.xlsx') or invoice_data.endswith('.xls'):

        if invoice_data.endswith('.xlsx') or invoice_data.endswith('.xls'):

            transalp_invoice = pd.read_excel(ptf.inputfilepath + invoice_data)

        else:

            transalp_invoice = pd.read_csv(ptf.inputfilepath + invoice_data)

    else:
        return


    # Calcul de la somme totale des valeurs de la TVA
    tax_amount_sum = transalp_invoice['TVA'].sum();
    cbc_tax_amount.text = str(tax_amount_sum)

    # Calcul de la somme totale des valeurs de la facture hors taxe
    tax_exclude_amount_sum = transalp_invoice['HT'].sum();
    cbc_TaxExclusiveAmount.text = str(tax_exclude_amount_sum)

    # Calcul de la somme totale des valeurs de la facture TTC
    tax_include_amount_sum = transalp_invoice['TTC'].sum();
    cbc_TaxInclusiveAmount.text = str(tax_include_amount_sum)

    # Calcul de la somme totale des valeurs de la facture à payer TTC
    payable_amount_sum = transalp_invoice['TTC'].sum();
    cbc_PayableAmount.text = str(payable_amount_sum)

    # Recuperation de la reference de commande de Orange France
    transalp_orange_reference = transalp_invoice['Num contrat'][0]

    etree.SubElement(cac_order_reference,
                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = str(
        transalp_orange_reference)

    # print("tax_amount_sum",tax_amount_sum)

    for index, row in transalp_invoice.iterrows():
        # Valeurs pieds de la facture
        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/
        cac_TaxSubtotal = etree.SubElement(cac_tax_total,
                                           "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal")

        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount
        cbc_TaxableAmount = etree.SubElement(cac_TaxSubtotal,
                                             "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxableAmount");
        cbc_TaxableAmount.attrib['currencyID'] = "EUR";
        cbc_TaxableAmount.text = str(row['HT'])

        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxAmount
        cbc_TaxAmount = etree.SubElement(cac_TaxSubtotal,
                                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount");
        cbc_TaxAmount.attrib['currencyID'] = "EUR";
        cbc_TaxAmount.text = str(row['TVA'])

        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:Percent
        cbc_percent = etree.SubElement(cac_TaxSubtotal,
                                       "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent");
        cbc_percent.text = str(row['code TVA'])

        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory
        cac_TaxCategory = etree.SubElement(cac_TaxSubtotal,
                                           "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory")

        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID

        cac_TaxScheme_pied = etree.SubElement(cac_TaxCategory,
                                              "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")

        # /Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID
        etree.SubElement(cac_TaxScheme_pied,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "VAT"

        # Valeurs des lignes de la facture

        # /Invoice/cac:InvoiceLine
        cac_InvoiceLine = etree.SubElement(root,
                                           "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoiceLine")

        # /Invoice/cac:InvoiceLine/cbc:ID
        etree.SubElement(cac_InvoiceLine,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "2"

        # /Invoice/cac:InvoiceLine/cbc:InvoicedQuantity
        cac_InvoicedQuantity = etree.SubElement(cac_InvoiceLine,
                                                "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}InvoicedQuantity");
        cac_InvoicedQuantity.attrib['unitCode'] = "MTR";
        cac_InvoicedQuantity.text = str(row['Qté'])

        # /Invoice/cac:InvoiceLine/cbc:LineExtensionAmount
        cbc_LineExtensionAmount = etree.SubElement(cac_InvoiceLine,
                                                   "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineExtensionAmount");
        cbc_LineExtensionAmount.attrib['currencyID'] = "EUR";
        cbc_LineExtensionAmount.text = str(row['HT'])

        # /Invoice/cac:InvoiceLine/cac:OrderLineReference
        cac_OrderLineReference = etree.SubElement(cac_InvoiceLine,
                                                  "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}OrderLineReference")

        # /Invoice/cac:InvoiceLine/cac:OrderLineReference/cbc:LineID
        etree.SubElement(cac_OrderLineReference,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineID").text = "2"

        # /Invoice/cac:InvoiceLine/cac:DespatchLineReference
        cac_DespatchLineReference = etree.SubElement(cac_InvoiceLine,
                                                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DespatchLineReference")

        # /Invoice/cac:InvoiceLine/cac:DespatchLineReference/cbc:LineID
        etree.SubElement(cac_DespatchLineReference,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineID").text = "1"

        # /Invoice/cac:InvoiceLine/cac:Item
        cac_Item = etree.SubElement(cac_InvoiceLine,
                                    "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Item")

        # /Invoice/cac:InvoiceLine/cac:Item/cbc:Name
        etree.SubElement(cac_Item,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name").text = str(
            row['Des'])  # "Fourniture des poteaux chez Orange"

        # /Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID
        cac_StandardItemIdentification = etree.SubElement(cac_Item,
                                                          "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}StandardItemIdentification")

        # /Invoice/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID
        etree.SubElement(cac_StandardItemIdentification,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = str(
            row['Ref poteau chez orange'])

        # /Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory
        cac_ClassifiedTaxCategory = etree.SubElement(cac_Item,
                                                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ClassifiedTaxCategory")

        # /Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:Percent
        etree.SubElement(cac_ClassifiedTaxCategory,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent").text = str(
            row['code TVA'])

        # /Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme
        cac_TaxScheme_Line = etree.SubElement(cac_ClassifiedTaxCategory,
                                              "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme")

        # /Invoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cac:TaxScheme/cbc:ID
        etree.SubElement(cac_TaxScheme_Line,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID").text = "VAT"

        # /Invoice/cac:InvoiceLine/cac:Price
        cac_price = etree.SubElement(cac_InvoiceLine,
                                     "{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Price")

        # /Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount
        etree.SubElement(cac_price,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PriceAmount").text = str(
            row['PU'])

        # /Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity
        cbc_BaseQuantity = etree.SubElement(cac_price,
                                            "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}BaseQuantity")

        # /Invoice/cac:InvoiceLine/cac:Price/cbc:BaseQuantity/cbc:unitCode
        etree.SubElement(cbc_BaseQuantity,
                         "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}unitCode").text = tpf.Unitemesure

    return root


# Function 2: Saves the invoice XML element to a file

# Save the invoice to a file
def save_invoice_to_file(invoice, file_path):
    tree = etree.ElementTree(invoice)
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="utf-8")