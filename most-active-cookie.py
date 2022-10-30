import sys
import argparse

parser = argparse.ArgumentParser(description = 'Finds the most active cookie ID on a certain day')
parser.add_argument("log", type = argparse.FileType('r'), metavar = '', help = 'Log file in csv format')
parser.add_argument("-d", "--date", type = str, metavar = '', help = 'Date in 0000-00-00 (year, month, day) format as string')
args = parser.parse_args()

if __name__ == '__main__':
    print(f"log-file = {args.log}, date = {args.date}")