import os, csv

dir_path = os.path.dirname(os.path.realpath(__file__))

print('Current dir: ' + dir_path)
print('Files available to merge: ')

if os.path.exists("merged.csv"):
    os.remove("merged.csv")
else:
    print("merged.csv file does not exist")

os.chdir('files')

for file in os.listdir():
    print(file)
    filename = os.path.splitext(file)[0]

    with open(file, 'r') as current_csv:
        csvread = csv.reader(current_csv, delimiter=',')
        next(csvread)
        for row in csvread:
            row.append(filename)
            row_final = ', '.join(row)
            #abrimos el csv final
            with open(os.path.join(os.pardir, 'merged.csv'), 'a') as csvfile:
                csvfile.write(row_final)
                csvfile.write('\n')