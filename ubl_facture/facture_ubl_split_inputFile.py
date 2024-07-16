import pandas as pd
import os
from datetime import datetime
import transalp_params_funct as tpf
import params_tech as ptf

# Fonction pour diviser un fichier Excel en plusieurs fichiers en fonction d'une colonne
def split_excel_by_column(file_path, column_name, output_dir):
    # Lire le fichier Excel dans un DataFrame
    df = pd.read_excel(file_path)

    # Créer le répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Grouper par la colonne spécifiée
    grouped = df.groupby(column_name)

    # Enregistrer chaque groupe dans un fichier Excel séparé
    for group_name, group_df in grouped:
        output_file = os.path.join(output_dir, f"{group_name}.xlsx")
        group_df.to_excel(output_file, index=False)
        print(f"Saved {output_file}")


def split_excel_by_column_main(file_path, column_name, output_dir):
    # Split the input file by customer
    for file in os.listdir(ptf.inputfilepath):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
        split_excel_by_column(ptf.inputfilepath + file, 'Num fac', ptf.inputfilepath)

