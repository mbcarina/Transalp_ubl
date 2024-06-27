import os
import shutil

import transalp_params_funct as tpf
import params_tech as ptf

from facture_ubl_process import create_ubl_invoice, save_invoice_to_file

if __name__ == "__main__":

    # Get the list of invoices
    Invoices= os.listdir(ptf.inputfilepath)

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
            save_invoice_to_file(invoice, outputfilepath + f"/Facture_{invoice_data}.xml".replace(file_format,""))

            # Move the invoice to the archive directory
            shutil.move(ptf.inputfilepath + invoice_data, archiveFilePath)

