import sys,time,os 

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

user = "Macgaiver"
passcode = "11996"



while True:
  a = str(input(f"{yellow}>>Enter Your Username     : {rst}"))
  if (a == user):
    print(f"{green}Correct Username{rst}")
    b = str(input(f"{yellow}>>Enter your Password     : {rst}"))
    if ( b == passcode):
      print(f"{green}Correct passcode{rst}")
      break
    else:
      print(f"{red}Wrong passcode{rst}")
  else:
    print(f"{red}Wrong Username{rst}")
    





logo = f"""{red}███╗░░░███╗░█████╗░░█████╗{rst}
{green}████╗░████║██╔══██╗██╔══██╗{rst}
{yellow}██╔████╔██║███████║██║░░╚═╝{rst}
{black}██║╚██╔╝██║██╔══██║██║░░██╗{rst}
{purple}██║░╚═╝░██║██║░░██║╚█████╔╝{rst}
{cyan}╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░{rst}

"""
def animetion (art):
  for i in logo:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.005)
animetion (logo)


def add (x, y):
  return x+y
def subtract (x, y):
  return x-y
def multiply (x, y):
  return x*y
def divided (x, y):
  return x/y
  
num1 = float(input(f"{yellow}Enter Your 1st Number : {rst}"))
num2 = float(input(f"{yellow}Enter Your 2nd Number : {rst}"))

print ("\033[1;92m1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divided\33:[0m")

choice = input(f"{yellow}Enter Your Choice [1/2/3/4] : {rst}")

if choice == "1":
  print (f'{green}{num1} + {num2} = {num1+num2}')
elif choice == "2":
  print (f'{green}{num1} - {num2} = {num1-num2}')
elif choice == "3":
  print (f'{green} {num1} x {num2} = {num1*num2}')
elif choice == "4":
  print (f'{green} {num1} ÷ {num2} = {num1/num2}')
else:
  print (f"{red}Invalid Input{rst}")