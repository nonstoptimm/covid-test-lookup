# COVID19 Test Checker
Did you get tested for COVID-19 at Berlin Central Station or Berlin ZOB and you're tired of checking their and the hilarious pdf at [MDI Limbach Berlin](https://mdi-limbach-berlin.de)?
I totally feel with you, as I had to wait forever to get my test results. Yawn!
In order to avoid wasting my time, I developed a basic script that automatically checks for your test results __every five minutes__. I did not want to send a request every minute because the infrastructure might break down considering the level of digitalization here in Germany when it comes to stuff like this ... happy waiting and stay healthy!

__Instructions:__
- Make sure you have Python installed 
- Open a command line of your choice
- run `pip install pdfplumber`
- run `python test_check.py --id [insert your id]`
- If you want to check for another date than today, add `--date YYYYMMDD`, e.g. `--date 20200820`
- Cheers!
