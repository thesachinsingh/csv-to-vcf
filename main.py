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



#main function that combines all the functions
def main():
    # retrieving all csv files from the folder
    files = os.listdir(folder_path)

    counter = 0
    for i in files:
        print(f'File to be converted : {i}')
        file_path = os.path.join(folder_path, i)
        #print(f'Opening file with file_path : {file_path}')
        valid_numbers = []
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for num_list in reader:
                pass
                #print(num_list)
            
            # extracting cleaned data in valid_numbers list
            for x in range(len(num_list)):
                #cleaning the data to only select valid entries
                if len(num_list[x]) >= 10:
                    valid_number = num_list[x].replace(' ', '')
                    #print(valid_number)
                    valid_numbers.append(valid_number)
            print("Cleaned and extracted the data...")

        #filename without extension
        file_name = i.replace('.csv', '')
        #print(f'file_name without extension : {file_name}')
        for x in valid_numbers:
            one_vcard = make_vcard(x)
            write_into_vcf(one_vcard, file_name)
        
        counter+=1
        print(f'{counter} files written successfully')
        print("----------------------------------------")



if __name__ == '__main__':
    main()