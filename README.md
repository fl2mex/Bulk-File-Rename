# Bulk-File-Rename
Small and extremely crude utility program I've built in Python.<br>
Many mistakes will be made since I haven't used Python in a long time, and even longer since I've used Python to do anything but the basics.<br>
My school needed a tool for renaming files and the IT students were tasked with creating file renamers.<br>
# Running
Pretty simple, open up the python script, change the unbelievably simple code and change the rename file function options.<br>
No CLI options/flags ~~yet~~ maybe if I feel like it i'll implement some...<br>
### Example text output in command line
```
Renaming ABC1.txt to myASDF1.txt
Renaming ABC2.txt to myASDF2.txt
Renaming ABC3.txt to myASDF3.txt
Renaming ABC4.txt to myASDF4.txt
Renaming ABC5.txt to myASDF5.txt
```
### PYTHON-STRING-REGEX PATTERN KNOWLEDGE NEEDED!!!
Some basic ones:
```
".*" means any character any number of times
".*.txt" means any character any number of times followed by .txt
".*[0-9].*" means including any number
```
If you need more, look online for a regex practice/cheat sheet.<br>
I used [this one](https://regexr.com/) to learn about regex.
