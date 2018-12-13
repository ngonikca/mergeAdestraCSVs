import os, csv, datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
out_filename = 'merged-' + str(datetime.datetime.now()) + '.csv'

os.chdir('files')

if os.path.exists(".DS_STORE"):
    os.remove(".DS_STORE")

i = 0
for file in os.listdir():
    print(file)
    filename = os.path.splitext(file)[0]

    with open(file, 'r') as current_csv:
        csvread = csv.reader(current_csv, delimiter=',')
        
        if i != 0:
            next(csvread) #saltamos el header si no es el primer archivo
        
        for row in csvread:
            row.append(filename)
            row_final = ', '.join(row)

            #abrimos el csv final
            with open(os.path.join(os.pardir, out_filename), 'a') as csvfile:
                csvfile.write(row_final)
                csvfile.write('\n')
        
        i += 1