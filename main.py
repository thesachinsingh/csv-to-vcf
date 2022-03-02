import csv
import os

#should have a folder named "csvfiles" in the present working directory
#path of folder named csvfiles - it should have all csv files
folder_path = os.path.join(os.getcwd(), "csvfiles")

#should have a folder named vcards in the present working directory
#this folder will have all vcards after the script runs successfully
vcards_path = os.path.join(os.getcwd(), "vcards")

#creating a vcard frm a phone number
def make_vcard(ph_number):
    return [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'FN:{ph_number}',
        f'TEL;TYPE=CELL:{ph_number}',
        'END:VCARD'
    ]

#writing a vcard to a vcf file
def write_into_vcf(vcard, filename_to_write_to):
    complete_vcf_file_path = os.path.join(vcards_path, f'{filename_to_write_to}.vcf')
    with open(complete_vcf_file_path, 'a') as vf:
        vf.writelines([l + '\n' for l in vcard])
