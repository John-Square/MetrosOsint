import os
import sys
import shlex
import subprocess
import smtplib
from platform import python_version  
import cryptocode
import stdiomask
import patoolib
import pyfiglet
import colorama
from colorama import Fore, Back
from pyunpack import Archive

class Main:
    def __init__(self):
        self.start_program = True
        while self.start_program == True:
            self.init()
    def init(self):
        try:
            self.command_input = input("\nMetros-osint> ")
            if self.command_input.replace(" ", "") != "":
                self.command_input_split = shlex.split(self.command_input)
                try:
                    self.command()
                except IndexError:
                    self.indexeror_()
        except KeyboardInterrupt:
            self.start_program = False
            print("\t")
    def command(self):
        if (
            str(self.command_input_split[0]).lower() == "help"
            or str(self.command_input_split[0]).lower() == "/?"
            or str(self.command_input_split[0]).lower() == "?"
        ):
            print("\nAll the commands:")
            print("     • email              — Sending data by mail.")
            print("     • archive            — Work with archives.")
            print(
                "     • profile            — Creating a contact personal information about a person."
            )
            print("     • cls, clear, clean  — Screen cleaning.")
            print("     • exit, quit, ^C     — Exit from the program.")
            print("     • $cmd               — Executing a console command.")
            print("     • help, /?, ?        — Displaying a list of program commands.")
            print("Syntax:")
            print("     <command> <parameter>")
            print("     <email>   (--send)")
            print("     <archive> (--archive, --unzipping)")
            print("     <profile> (--new, --open, ln=ru, ln=en)")
            print("     <$cmd>    <parameter>")
            print("\n[*] To display command help, enter only the name of the command.")
        if str(self.command_input_split[0]).lower() == "$cmd":
            os.system(self.command_input.replace("$cmd", ""))
        if (
            str(self.command_input_split[0]).lower() == "exit"
            or str(self.command_input_split[0]).lower() == "quit"
            or str(self.command_input_split[0]).lower() == "^c"
        ):
            self.start_program = False
        if (
            str(self.command_input_split[0]).lower() == "cls"
            or str(self.command_input_split[0]).lower() == "clear"
            or str(self.command_input_split[0]).lower() == "clean"
        ):
            try:
                subprocess.call("cls")
            except:
                subprocess.call("clear")
        if (
            str(self.command_input_split[0]).lower() == "archive"
            and str(self.command_input_split[1]).lower() == "--unzipping"
        ):
            file = input("File path and unzip path [path_rar:path]: ")
            file_rar_ = shlex.split(file.replace(":", " "))
            file_rar = str(file_rar_[0])
            file_path = str(file_rar_[1])
            patoolib.extract_archive(file_rar, outdir=file_path)
        if (
            str(self.command_input_split[0]).lower() == "archive"
            and str(self.command_input_split[1]).lower() == "--archive"
        ):
            file = input("File path and packing path [path:path_rar]: ")
            file_rar_ = shlex.split(file.replace(":", " "))
            file_rar = str(file_rar_[0])
            file_path = str(file_rar_[1])
            patoolib.create_archive(file_rar, (file_path,))
        if (
            str(self.command_input_split[0]).lower() == "email"
            and str(self.command_input_split[1]).lower() == "--send"
        ):
            email = input("Email authorization: ")
            password_email = stdiomask.getpass(prompt="Password: ", mask="*")
            smtp = input("Smtp serve format: [smtp:port]")
            smtp = shlex.split(smtp.replace(":", " "))
            smtp_server = str(smtp[0])
            smtp_port = str(smtp[1])
            to_email = input("Where: ")
            file_send = input("File: ")
            if os.path.isfile(file_send) != False:
                server = smtplib.SMTP_SSL("smtp.{}".format(smtp_server), int(smtp_port))
                server.login(email, password_email)
                server.sendmail(
                    email,
                    to_email,
                    open(file_send, encoding="utf-8", errors="ignore").read(),
                )
                server.quit()
                print("[*] Message sent.")
            else:
                print("[!] File not found: {}".format(file_send))
        if (
            str(self.command_input_split[0]).lower() == "profile"
            and str(self.command_input_split[1]).lower() == "--open"
        ):
            self.file_name_ = input("File name: ")
            if os.path.isfile(self.file_name_) != False:
                self.key_ = stdiomask.getpass(prompt="Key: ", mask="*")
                self.password_ = stdiomask.getpass(prompt="Password: ", mask="*")
                key_result_ = cryptocode.decrypt(
                    open(self.file_name_, encoding="utf-8", errors="ignore").read(),
                    str(self.key_),
                )
                result = cryptocode.decrypt(key_result_, self.password_)
                try:
                    subprocess.call("cls")
                except:
                    subprocess.call("clear")
                print(result)
                print("\n[*] File name: {}".format(self.file_name_))
            else:
                print("[!] File not found: {}".format(self.file_name_))
        if (
            str(self.command_input_split[0]).lower() == "profile"
            and str(self.command_input_split[1]).lower() == "--new"
        ):
            if str(self.command_input_split[-1]).lower() == "ln=en":
                self.name = input("Name: ")
                self.surname = input("Last name: ")
                self.patronymic = input("Patronymic: ")
                self.name_transcription = input("Transcription of name: ")
                self.surname_transcription = input("Transcription of surname: ")
                self.patronymic_transcription = input("Patronymic transcription: ")
                self.pseudonym = input("Pseudonym: ")
                self.organization = input("Organization: ")
                if self.organization.lower() != "none":
                    self.department = input("Department: ")
                    self.position = input("Position: ")
                else:
                    self.department = "none"
                    self.position = "none"
                self.telephone = input("Phone: ")
                self.mail_address = input("Mail address: ")
                self.address = input("Address: ")
                self.web_site = input("Website: ")
                self.date_of_birth = input("Date of birth: ")
                self.sip = input("SIP: ")
                self.note = input("Note: ")
                self.facebook = input("Facebook: ")
                self.vk = input("Vk: ")
                self.twitter = input("Twitter: ")
                self.ok = input("Ok: ")
                self.youtube = input("Youtube: ")
                self.whatsapp = input("Whatsapp: ")
                self.viber = input("Viber: ")
                self.tiktok = input("Tik Tok: ")
                self.instagram = input("Instagram: ")
                self.telegram = input("Telegram: ")
                self.all_social_newtworks = input("Other social networks: ")
                print("\n")
                self.file_name = input("Path and filename: ")
                self.key = stdiomask.getpass(prompt="Key: ", mask="*")
                self.password = stdiomask.getpass(prompt="Password: ", mask="*")
                self.result = f"""Name:\t\t\t\t{self.name}
Surname:\t\t\t{self.surname}
Middle name:\t\t\t{self.patronymic}
Surname transcription:\t\t\t{self.name_transcription}
Name transcription:\t\t\t{self.surname_transcription}
Middle name transcription:\t\t\t{self.patronymic_transcription}
Alias:\t\t\t{self.pseudonym}
Organization:\t\t\t{self.organization}
Department:\t\t\t{self.department}
Position:\t\t\t{self.position}
Phone:\t\t\t{self.telephone}
Postal address:\t\t\t{self.mail_address}
Address:\t\t\t{self.address}
Website:\t\t\t{self.web_site}
Date of birth:\t\t\t{self.date_of_birth}
SIP:\t\t\t{self.sip}
Note:\t\t\t{self.note}
Facebook:\t\t\t{self.facebook}
Vk:\t\t\t{self.vk}
Twitter:\t\t\t{self.twitter}
Ok:\t\t\t{self.ok}
Youtube:\t\t\t{self.youtube}
whatsapp:\t\t\t{self.whatsapp}
Viber:\t\t\t{self.viber}
Tik Tok:\t\t\t{self.tiktok}
Instagram:\t\t\t{self.instagram}
Telegram:\t\t\t{self.telegram}
Other social networks:\t\t\t{self.all_social_newtworks}
"""
                result_key = cryptocode.encrypt(self.result, self.key)
                result_file = cryptocode.encrypt(result_key, self.password)
                _file = open(self.file_name, "w+")
                _file.write(result_file)
                _file.close()
            elif str(self.command_input_split[-1]).lower() == "ln=ru":
                self.name = input("Имя: ")
                self.surname = input("Фамилия: ")
                self.patronymic = input("Отчество: ")
                self.name_transcription = input("Транскрипция имени: ")
                self.surname_transcription = input("Транскрипция фамилии: ")
                self.patronymic_transcription = input("Транскрипция отчества: ")
                self.pseudonym = input("Псевдоним: ")
                self.organization = input("Организация: ")
                if self.organization.lower() != "none":
                    self.department = input("Отдел: ")
                    self.position = input("Позиция: ")
                else:
                    self.department = "none"
                    self.position = "none"
                self.telephone = input("Телефон: ")
                self.mail_address = input("Почтовый адрес: ")
                self.address = input("Адрес: ")
                self.web_site = input("Веб-сайт: ")
                self.date_of_birth = input("Дата рождения: ")
                self.sip = input("SIP: ")
                self.note = input("Примечание: ")
                self.facebook = input("Facebook: ")
                self.vk = input("Vk: ")
                self.twitter = input("Twitter: ")
                self.ok = input("Ok: ")
                self.youtube = input("Youtube: ")
                self.whatsapp = input("WhatsApp: ")
                self.viber = input("Viber: ")
                self.tiktok = input("Tik Tok: ")
                self.instagram = input("Instagram: ")
                self.telegram = input("Telegram: ")
                self.all_social_newtworks = input("Другие социальные сети: ")
                print("\n")
                self.file_name = input("Путь и имя файла: ")
                self.key = stdiomask.getpass(prompt="Ключ: ", mask="*")
                self.password = stdiomask.getpass(prompt="Пароль: ", mask="*")
                self.result = f"""Имя:\t\t\t\t{self.name}
Фамилия:\t\t\t{self.surname}
Отчество:\t\t\t{self.patronymic}
Транскрипция фамилии:\t\t{self.name_transcription}
Транскрипция имени:\t\t{self.surname_transcription}
Транскрипция отчества:\t\t{self.patronymic_transcription}
Псевдоним:\t\t\t{self.pseudonym}
Организация:\t\t\t{self.organization}
Отдел:\t\t\t\t{self.department}
Позиция:\t\t\t{self.position}
Телефон:\t\t\t{self.telephone}
Почтовый адрес:\t\t\t{self.mail_address}
Адрес:\t\t\t\t{self.address}
Веб-сайт:\t\t\t{self.web_site}
Дата рождения:\t\t\t{self.date_of_birth}
SIP:\t\t\t\t{self.sip}
Примечание:\t\t\t{self.note}
Facebook:\t\t\t{self.facebook}
Vk:\t\t\t\t{self.vk}
Twitter:\t\t\t{self.twitter}
Ok:\t\t\t\t{self.ok}
Youtube:\t\t\t{self.youtube}
WhatsApp:\t\t\t{self.whatsapp}
Viber:\t\t\t\t{self.viber}
Tik Tok:\t\t\t{self.tiktok}
Instagram:\t\t\t{self.instagram}
Telegram:\t\t\t{self.telegram}
Другие социальные сети:\t\t{self.all_social_newtworks}
"""
                result_password = cryptocode.encrypt(self.result, self.password)
                result_key = cryptocode.encrypt(result_password, self.key)
                _file = open(self.file_name, "w+")
                _file.write(result_key)
                _file.close()
    def indexeror_(self):
        if str(self.command_input_split[0]).lower() == "profile":
            print("\nprofile — Creating a contact personal information about a person.")
            print("Syntax:")
            print("          profile (--new) <ln>")
            print("          profile (--new) <ln=ru_or_ln=en>")
            print("          profile (--open)")
            print("Sample data:")
            print("          • Name")
            print("          • Last name")
            print("          • Patronymic")
            print("          • Name transcription")
            print("          • Transcription of last name")
            print("          • Transcription of middle name")
            print("          • Alias")
            print("          • Organization")
            print("          • Department")
            print("          • Position")
            print("          • Phone")
            print("          • Postal address")
            print("          • Address")
            print("          • Website")
            print("          • date of birth")
            print("          • SIP")
            print("          • Note")
            print("          • Facebook")
            print("          • vk")
            print("          • Twitter")
            print("          • Ok")
            print("          • Youtube")
            print("          • whatsapp")
            print("          • Viber")
            print("          • Tik Tok")
            print("          • Instagram")
            print("          • Telegram")
            print("          • Other social networks")
            print("Key:")
            print("          210 — Personal data.")
            print("          211 — Person details or contact.")
            print("          212 — Enemy information.")
            print("          213 — Relative.")
            print("          214 — Colleague/friend.")
        elif str(self.command_input_split[0]).lower() == "email":
            print("\nemail — Sending data by mail.")
            print("Syntax:")
            print("          email (--send)")
            print("Data input:")
            print("     Authorization:")
            print("          • Email     ")
            print("          • Password  ")
            print("     Send:")
            print("          • smtp_server:smtp_port — Example: gmail.com:465")
            print(
                "          • Where — Smtp server must match the server of both sender and receiver."
            )
            print("          • File  — Extracting the contents of a file.")
        elif str(self.command_input_split[0]).lower() == "archive":
            print("\narchive — Work with archives.")
            print(
                "          This command can be used as storing personal data (data type depends on the key)."
            )
            print("Syntax:")
            print(
                "          --archive   — [path:path_rar] Example: archive.rar:file.txt"
            )
            print("          --unzipping — [path_rar:path] Example: archive.rar:folder")
class Boot:
    def __init__(self):
        print(Fore.RED+pyfiglet.figlet_format("Metros Osint")+Fore.WHITE)
        print("[*] Metros Open Source Intelligence [version 1.0] 2022.")
        print("\n[*] Detailed information on the website: metros-software.ru")
        print(
            "[*] Technical support metros:            metrostechnicalsupp0rt@gmail.com"
        )
        Main()
        print("\n[*] Completing Metros Open Source Intelligence...\n")
if __name__ == "__main__":
    try:
        if sys.argv[1] == "--version" or sys.argv[1] == "-v":
            print("[*] Metros Open Source Intelligence [version 1.0] 2022.")
        if sys.argv[1] == "--clear":
            try:
                subprocess.call("cls")
            except:
                subprocess.call("clear")
            Boot()
    except:
        Boot()