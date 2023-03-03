import os, sys, time, pyshorteners

black="\033[1;90m"
white="\033[1;97m"
red="\033[1;91m"
green="\033[1;92m"
yellow="\033[1;93m"
blue="\033[1;94m"
purple="\033[1;95m"
cyan="\033[1;96m"  
rst="\033[0m"

os.system("clear")

username = "Macgaiver"
password = "11996"


def end():
  back = input()
  sys.exit()


os.system ("clear")


x = str(input(f"{blue}Enter Your Username : "))
if x == username:
  print (f"{green}Correct Username")
  y = str(input(f"{blue}Enter Your Password : "))
  if y == password:
    print (f"{green}Correct Password")
  else:
    print (f"{red}Wrong Password")
    time.sleep (1)
    print (f"{green}Press Enter To Exit")
    end()

else:
  print (f"{red}Wrong Username")
  time.sleep (1)
  print (f"{green}Press Enter To Exit")
  end()
  



os.system ("clear")

def animetion (text):
  for i in text:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.005)

logo = f'''
 {red}_    _      _                          
{blue}| |  | |    | |                         
{cyan}| |  | | ___| | ___ ___  _ __ ___   ___ 
{green}| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \

{purple}\  /\  /  __/ | (_| (_) | | | | | |  __/
 {yellow}\/  \/ \___|_|\___\___/|_| |_| |_|\___|

'''
animetion (logo)
time.sleep (0.5)




os.system ("clear")


  


banner = f'''
  {red}__  _____  __     ______            __                  
{blue} / / / / _ \/ /    / __/ /  ___  ____/ /____ ___  ___ ____
{yellow}/ /_/ / , _/ /__  _\ \/ _ \/ _ \/ __/ __/ -_) _ \/ -_) __/
{green}\____/_/|_/____/ /___/_//_/\___/_/  \__/\__/_//_/\__/_/   
                                                          
'''
details = f"""{green}                  Author   : Macgaiver
                  Github   : https://github.com/macgaiver11996
                  Telegram : t.me/M4C641V3R{rst}"""
           

symbol = f"{green}\n****************************************************************{rst}"

animetion (banner)
animetion (details)
animetion (symbol)




link = input(f"{yellow}\n\nEnter Your Link Here : ")
s = pyshorteners.Shortener()
provide = s.tinyurl.short(link)
print (f"{green}Your provide link in here >> {provide}")

print (f"{red}\n\nPress Enter To Exit")
end()