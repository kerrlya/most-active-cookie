import argparse, logging # library for CLI parsing and logging

parser = argparse.ArgumentParser(description = 'Finds the most active cookie ID on a certain day')
parser.add_argument("log", type = argparse.FileType('r'), metavar = '', help = 'Log file in csv format')
parser.add_argument("-d", "--date", type = str, metavar = '', help = 'Date in 0000-00-00 (year, month, day) format as string')
args = parser.parse_args()

def input_check(log_file, date): 
    if ".csv" not in log_file.name:
        logging.ERROR("Log file must be .csv type")
    if not date:
        logging.ERROR("Date must be provide with -d")
    if len(date) < 10:
        logging.ERROR("Date must be provided in 0000-00-00 form as UTC time")
    if (date[4] != "-") or (date[7] != "-"):
        logging.warning("Date must be provided in 0000-00-00 form as UTC time")

def main(log_file, date):
    # assume that date -d will always be given (?)
    with log_file as log:
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
    input_check(args.log, args.date)
    main(args.log, args.date)
    
    
    

                
