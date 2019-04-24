# Script to generate the tex file for the change log from a change tracking
# data file.

from pathlib import Path
import csv

class MissingLogFile(Exception):
    pass

# if changelog.csv exists, use it
# otherwise, produce an error
def get_log_lines():
    '''Return the log data in reverse chronologic order'''
    csv_name = Path('./changelog.csv')
    if csv_name.exists():
        return csv_log_parse(csv_name)
    raise MissingLogFile("No log file to build changelog from!")
    
def csv_log_parse(fpath):
    '''Returns a list of log entries from a csv file in reverse chronological order'''
    
    def csv_date_key(x):
        '''Convert a date + seq into a key for sorting
        More than 1000 edits in a single data is unexpected...'''
        key = int(x['date'])*1000
        key += int(x['seq'])
        return key
                
    with fpath.open() as file:
        dreader = csv.DictReader(file)
        data = []
        for row in dreader:
            data.append(row)
        sorted(data, key=csv_date_key )
        lines = []
        for row in data:
            lines.append('\makechangelogline{%s}{%s}{%s}{%s}\n' %
                (row['date'],row['seq'],row['author'],row['text']) )
        return lines

def main():
    lines = get_log_lines()
    with open('changelog.tex','w') as logfile:
        for line in lines:
            logfile.write(line)

if __name__=="__main__":
    main()