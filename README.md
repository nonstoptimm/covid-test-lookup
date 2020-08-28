# COVID19 Test Checker
## Problem
Did you get tested for COVID-19 at Berlin Central Station or Berlin ZOB and you're tired of checking their PDF at [MDI Limbach Berlin](https://mdi-limbach-berlin.de)?<br>
I totally feel with you, as I had to wait forever to get my test results. Yawn!<br>

## Solution
In order to avoid wasting my time, I developed a basic script to check for your test __every five minutes__. I did not want to send a request every minute because the infrastructure might break down considering the level of digitalization here in Germany when it comes to stuff like this ;)!<br>
Happy waiting and stay healthy!

## Instructions
- Make sure you have Python installed 
- Open a command line of your choice
- run `pip install pdfplumber`
- run `python test_check.py --id [insert your id]`
- If you want to check for another date than today, add `--date YYYYMMDD`, e.g. `--date 20200820`
- Cheers!

PS: I know that this script might be a bit overengineered, but that is what quarantine does with you.
