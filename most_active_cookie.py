import sys
import argparse # library for CLI parsing

parser = argparse.ArgumentParser(description = 'Finds the most active cookie ID on a certain day')
parser.add_argument("log", type = argparse.FileType('r'), metavar = '', help = 'Log file in csv format')
parser.add_argument("-d", "--date", type = str, metavar = '', help = 'Date in 0000-00-00 (year, month, day) format as string')
args = parser.parse_args()

def main():
    # assume that date -d will always be given (?)
    with args.log as log:
        cookies = {} # dictionary of cookies on the specified date and their count 
        
        for line in log:    
            words = line.split(',')
            
            cookie = words[0]
            date = words[1][0:10]

            if date == args.date:
                if cookie in cookies:
                    cookies[cookie] += 1
                else:
                    cookies[cookie] = 1
        
        # find most commonly occuring cookies
        max_freq = 0 # current maximum frequency 
        freq_cookies = [] # current most frequent cookies

        for cookie in cookies:
            if cookies[cookie] > max_freq:
                max_freq = cookies[cookie]
                freq_cookies = [cookie]
            elif cookies[cookie] == max_freq:
                freq_cookies.append(cookie)
        
        # join freq_cookies into multiline string
        all_cookies = "\n".join(freq_cookies)
        print(all_cookies)
        return(all_cookies)

if __name__ == '__main__':
    main()
    
    
    

                
