import unidecode as u, os
'''A simple program to change a text or csv file into all ascii characters.'''

#Try to open the file. If it doesn't open, send a message that something is wrong with the file.
try:
    file = input('Please enter the path to the file. Make sure to include the extension at the end!\n')
    
    #Get the directory and base name of the file and then create a new output name.
    dir_ = os.path.dirname(file) + '\\'
    base = os.path.basename(file)
    newfile = os.path.splitext(base)[0] + '_cleaned.csv'
    output = dir_ + newfile

    #Open the file and the new output and clean the data
    with open(file) as f, open(output, 'w') as o:
        for line in f:
            line = u.unidecode(line)
            o.write(line)
except FileNotFoundError as err:
    print('There was something wrong with the file name. Please make sure it is spelled correctly with the full path and extension (.txt or .csv) at the end!\nError:' + str(err))
