import csv
data = open('reversecomplementtemplate.csv',encoding="utf-8")
csv_data=csv.reader(data)
data_lines=list(csv_data)

def rev_complement(seq):
    rev_complemented = ''
    reverse = seq[::-1]
    for i in reverse:
        if i.lower()=='a':
            rev_complemented = rev_complemented+'T'
        elif i.lower()=='c':
            rev_complemented = rev_complemented+'G'
        elif i.lower()=='g':
            rev_complemented = rev_complemented+'C'
        elif i.lower()=='t':
            rev_complemented = rev_complemented+'A'
    return rev_complemented

rc_list=[]
for i in data_lines:
    rc_intermediate_list=[]
    rc_intermediate_list.append(rev_complement(i[0]))
    rc_list.append(rc_intermediate_list)

file_to_output=open('reversecomplementoutput.csv','w',newline='')
csv_writer=csv.writer(file_to_output,delimiter=',')
csv_writer.writerows(rc_list)
file_to_output.close()