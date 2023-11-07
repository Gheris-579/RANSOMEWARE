import os

chiave = 83758743842768874632784523867546235462359

nome_file = "prova.txt" # Nome file
nome_file_cifrato = nome_file + '.encrypt'

dati_cifrati = bytearray()

with open(nome_file, 'rb') as input:
    dati_cifrati = bytearray()
    for byte in input.read():
        byte_cifrato = byte ^ chiave
        dati_cifrati.append(byte_cifrato)

with open(nome_file_cifrato, 'wb') as output:
    output.write(dati_cifrati)

os.remove(nome_file)
