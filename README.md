# Metros Open Source Intelligence
## Description
The program was created for storing/storing/sending personal data of users.
<br>
![Alt-текст](https://cdn-icons-png.flaticon.com/128/286/286436.png "Metros Osint")
## Installation
- Python 3.8
```
pip install -r requirements.txt
```
```
git clone https://github.com/John-Square/MetrosOsint/
cd MetrosOsint
python3 MetrosOsint.py
```
## Usage
- Displaying the current version of the program
```
python3 MetrosOsint.py --version
python3 MetrosOsint.py -v
```
- Erase console contents and run prog
```
python3 MetrosOsint.py --clear
```
## All the commands
### Using the help command
- To display command help, enter only the name of the command.
```
• email              — Sending data by mail.
• archive            — Work with archives.
• profile            — Creating a contact personal information about a person.
• cls, clear, clean  — Screen cleaning.
• exit, quit, ^C     — Exit from the program.
• $cmd               — Executing a console command.
• help, /?, ?        — Displaying a list of program commands.
Syntax:
  <command> <parameter>
  <email>   (--send)
  <archive> (--archive, --unzipping)
  <profile> (--new, --open, ln=ru, ln=en)
  <$cmd>    <parameter>
```

### Using the email command
```
email — Sending data by mail.
Syntax:
  email (--send)
Data input:
  Authorization:
    • Email     
    • Password  
  Send:
    • smtp_server:smtp_port — Example: gmail.com:465
    • Where — Smtp server must match the server of both sender and receiver.
    • File  — Extracting the contents of a file.
```
### Using the archive command
- This command can be used as storing personal data (data type depends on the key).
```
archive — Work with archives.
Syntax:
  --archive   — [path:path_rar] Example: archive.rar:file.txt"
  --unzipping — [path_rar:path] Example: archive.rar:folder
```
### Using the profile command
- The key can be used by anyone, not only from the list below, it can be used as a pin code.
- Keys for data markup.
- If you set "organization" to none, the program will skip the two values "Department" and "Position".
```
profile — Creating a contact personal information about a person.
Syntax:
  profile (--new) <ln>
  profile (--new) <ln=ru_or_ln=en>
  profile (--open)
Sample data:
  • Name
  • Last name
  • Patronymic
  • Name transcription
  • Transcription of last name
  • Transcription of middle name
  • Alias
  • Organization
  • Department
  • Position
  • Phone
  • Postal address
  • Address
  • Website
  • date of birth
  • SIP
  • Note
  • Facebook
  • Vk
  • Twitter
  • Ok
  • Youtube
  • Whatsapp
  • Viber
  • Tik Tok
  • Instagram
  • Telegram
  • Other social networks
Key:
  210 — Personal data.
  211 — Person details or contact.
  212 — Enemy information.
  213 — Relative.
  214 — Colleague/friend.
```
## Technical support
- metrostechnicalsupp0rt@gmail.com
## Developer site
- [metros-software.ru](http://metros-software.ru)
<br>
Thank you!
