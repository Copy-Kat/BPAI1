import argparse
import re
import pandas as pd

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', metavar='f', type=str, help='Name of the csv file to be processed (eg. example.csv)')
parser.add_argument('--col', dest='col', action='store', default='ingredient', 
                    type=str, help='Name of the col to be processed (default: ingredient)')
parser.add_argument('--o', dest='out', action='store', default='_cleaned', 
                    type=str, help='Name of the output file (eg. out.csv default: <filename>_cleaned.csv)')

add_space_re = re.compile('([0-9]+)([a-z]+ )')

convert_to_float_re = re.compile('([0-9]* )?([0-9])/([0-9]*)')

def add_space(matchobj):
    return matchobj.group(1) + ' ' + matchobj.group(2)

def to_float(matchobj):
    if matchobj.group(1) is not None and matchobj.group(1) != ' ':
        try:
            return str(float(matchobj.group(1)) + (float(matchobj.group(2)) / float(matchobj.group(3))))
        except:
            print(matchobj.group(1) is None)
    return str((float(matchobj.group(2)) / float(matchobj.group(3))))

# def removeQuotation(s):
#     return s.replace('"', '')

args = parser.parse_args()

# read infile here
df = pd.read_csv(args.filename)

# add space in between the quantity and unit
df['INQs'] = df['INQs'].apply(lambda s: re.sub(add_space_re, add_space, s))

# convert unit to float (1 1/2 => 1.5)
df['INQs'] = df['INQs'].apply(lambda s: re.sub(convert_to_float_re, to_float, s))

# remove quotation marks
df['INQs'] = df['INQs'].apply(lambda s: re.sub(r'(\")', '', s))

# remve all things in backets
df['INQs'] = df['INQs'].apply(lambda s: re.sub(r'(\(.*\))', '', s))

if args.out != '_cleaned':
    df.to_csv(args.out)
else:
    df.to_csv(args.filename.replace('.csv', '_cleaned.csv'))

