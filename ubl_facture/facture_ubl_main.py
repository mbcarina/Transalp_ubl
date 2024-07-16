import os
import shutil

import transalp_params_funct as tpf
import params_tech as ptf
from datetime import datetime


from facture_ubl_process import create_ubl_invoice, save_invoice_to_file
from facture_ubl_split_inputFile import split_excel_by_column_main


if __name__ == "__main__":

    # Split the input file by customer
    try:
        split_excel_by_column_main(ptf.inputfilepath, 'Num fac', ptf.inputfilepath)

        Invoices = os.listdir(ptf.inputfilepath)

    except Exception as e:

        print(f"Error: {e}")

    if len(Invoices) > 0:

        # Create the output and archive directories
        outputfilepath = ptf.outputfilepath + "Facture_" + tpf.invoice_cbc_id
        archiveFilePath = ptf.archiveFilePath + tpf.invoice_cbc_id
        os.makedirs(outputfilepath, exist_ok=True)
        os.makedirs(archiveFilePath, exist_ok=True)

        for invoice_data in Invoices:

            # Create the invoice into ubl format
            invoice = create_ubl_invoice(invoice_data)
            file_format = invoice_data.split(".")[-1]

            # Save the invoice to a file

            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
            outputfile_name = 'INVOICE-' + tpf.customer_siren + '_FRS-' + timestamp

            save_invoice_to_file(invoice, outputfilepath + f"/{outputfile_name}.xml".replace(file_format,""))

            # Move the invoice to the archive directory
            shutil.move(ptf.inputfilepath + invoice_data, archiveFilePath)

