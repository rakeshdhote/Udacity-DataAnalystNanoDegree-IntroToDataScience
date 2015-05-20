import csv
import pandas as pd
import numpy as np
import string

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved.

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:

    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        rfile = open(name,'rb')                       #read file
        read_file_object = csv.reader(rfile,skipinitialspace=True)  # read file object-skip white spaces

        wfilename = 'updated_'+name                 # write file name
        wfile = open(wfilename,'wb')                #write file
        write_file_object = csv.writer(wfile)       #write file object

        for rowr in read_file_object:               # reading each row in a file
            cinit = rowr[0:3][:]                    # first three column entries of each rowr
            rowr_len = len(rowr)                    # rowr length
            data_fix_incr = 5                       # fix data increment
            iterations = (rowr_len-3)/data_fix_incr

            for i in range(1, iterations+1):          #writing each row in the updated_+name file
                roww = cinit + rowr[(i*data_fix_incr-2):((i+1)*data_fix_incr-2)][:]
                write_file_object.writerow(roww)

        rfile.close()
        wfile.close()

if __name__ == "__main__":
    input_files = ['turnstile_110528.txt', 'turnstile_110604.txt']
    fix_turnstile_data(input_files)