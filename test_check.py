''' COVID19 Test Checker
Did you get tested for COVID-19 at Berlin Central Station or Berlin ZOB and you're tired of checking their and the hilarious pdf at MDI Limbach Berlin?
I totally feel with you, as I had to wait forever to get my test results. Yawn!
In order to avoid wasting my time, I developed a basic script to check for your test results ... happy waiting!

Instructions:
- Make sure you have Python installed 
- Open a command line of your choice
- Run "pip install pdfplumber"
- Run "python test_check.py --id [insert your id]"
- If you want to check for another date than today, add --date YYYYMMDD, e.g. --date 20200820
- Cheers!
'''

# Import some dependencies
import logging
import requests
import sys
import os
import time
import argparse
from datetime import datetime
import pdfplumber

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description='Arguments to specify document date (optional, taking todays date as default) and test id (mandatory).')
    parser.add_argument("--id", 
                        type=str,
                        help="Pass the test id")
    parser.add_argument("--date", 
                        type=str,
                        default=datetime.now().strftime('%Y%m%d'),
                        help="Pass the date as 'YYYYMMDD'")
    args = parser.parse_args()
    if args.id == None: 
        logging.critical('Test ID could not be detected, please pass it using --id')
        sys.exit()

    # Result lookup
    cov = []
    while len(cov) != 1:
        logging.warning(f'Starting to run and look for report of {args.date} ...')
        url = f'https://www.mdi-limbach-berlin.de/fileadmin/user_upload/Berlin/PDF/Testergebnisse-Covid/Corona_{args.date}.pdf'
        response = requests.get(url)
        if response.status_code == 200:
            logging.warning(f'Loaded report of {args.date} ...')
            # Write
            with open('results.pdf', 'wb') as f:
                f.write(response.content)
            # Processor
            try:
                logging.warning(f'Scanning for your results {args.id} ...')
                with pdfplumber.open('results.pdf') as pdf:
                    for page in range(len(pdf.pages)):
                        curr_page = pdf.pages[page].extract_text()
                        curr_page = curr_page.split("\n")
                        for line in curr_page:
                            if args.id in line:
                                logging.warning(f'FOUND YOUR RESULT -> {line}')
                                pdf.close()
                                os.remove('results.pdf')
                                sys.exit()
                logging.warning(f'Could not find your results :( I feel with you!')
            except Exception as e:
                logging.error(f'{e}')
        else:
            logging.warning(f'Report {args.date} not available ...')
        logging.warning(f'Going to sleep for 5 min...zZz...')
        time.sleep(300)
        logging.warning(f'Uaaaaah...woke up!')

if __name__ == "__main__":
    main()