# Import packages
from googlesearch import search
from colorama import Fore, just_fix_windows_console
import threading
import argparse

try:
    just_fix_windows_console() # Fix windows console sometimes not working
except:
    pass

# Ascii
print(Fore.WHITE + """                                     
   ____          _           _               _           
  |    \ ___ ___| |_ ___ _ _| |_ ___ ___ ___| |_ ___ ___ 
  |  |  | . |  _| '_| -_|_'_|  _|  _| .'|  _|  _| . |  _|
  |____/|___|_| |_,_|___|_,_|_| |_| |__,|___|_| |___|_|  """ + Fore.RESET)
print(f"                {Fore.MAGENTA}Made by Birdy{Fore.RESET}   |   {Fore.GREEN}v1.0{Fore.RESET}\n\n")

# Initilization
parser = argparse.ArgumentParser(description="Simple tool that is used to extract all URLs found in a Google Dork")
parser.add_argument("-s", "--search", type=str, help="the google dork search for links to be extracted from")
parser.add_argument("-o", "--output", type=str, help="option to save results to file")
parser.add_argument("-a", "--amount", type=int, help="amount of results to show")
args = parser.parse_args()

# Main
def write_url_to_file(url, output_file):
    with open(output_file, 'a') as f:
        f.write(url + '\n')

try:
    if args.search:
        threads = []
        for url in search(args.search, num_results=args.amount):
            print(url)
            if args.output:
                thread = threading.Thread(target=write_url_to_file, args=(url, args.output))
                thread.start()
                threads.append(thread)
                continue
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
except KeyboardInterrupt:
    print(f"[{Fore.RED}-{Fore.RESET}] Search ended by user")