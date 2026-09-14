#A shared drive folder invoices/ has files named inconsistently (Invoice_1.txt, invoice2.TXT, INV-3.txt).
# Write list_txt_files(folder) using os.listdir() and .lower().endswith('.txt') to find all of them regardless of case.

import os
def list_txt_files(folder):
    files = []

    for file in os.listdir(folder):
        if file.lower().endswith('.txt'):
            files.append(file)

    return files

print(list_txt_files("invoices"))