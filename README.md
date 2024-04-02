# Dorkextractor
 Fetches URLs from a google dork search specified in the command of the program

# 💾 Installation
 Firstly, you need to have Python3+ installed
 <br />
 Install the needed package(s)
 ```pip install -r requirements.txt```<br />

# 📌 Usage
 Dorkextractor is a CLI tool, so it takes arguments when the file is ran.<br />
 Examples:<br />
 <br />
 Show options:
 ```
 python dorkextractor.py -h
 ```
 
 ---> Examples:<br />
 Find 10 DB files:
```
python dorkextractor.py -s 'filetype:"db"' -a 10
```

Search for URL's with the title "Hacked by" and save it to a file
```
python dorkextractor.py -s 'intitle:"Hacked by"' -a 5 -o links.txt
```
Sometimes you will get an error about: Too many Requests for URL, if that happens you can try again, and if that doesnt work wait a bit of time then try again.
