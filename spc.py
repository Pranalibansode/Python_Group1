import random
def gameWin(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            print('\nyou wrape the stone with your paper\n')
            return True
        elif you=='c':
            print('\ncomputer break the cesar with his stone\n')
            return False
    elif comp=='p':
        if you=='c':
            print('\nyou cut the paper with your cesar\n')
            return True
        elif you=='s':
            print('\ncomputer wrape the stone with his paper\n')
            return False
    elif comp=='c':
        if you=='s':
            print('\nyou break the cesar with your stone\n')
            return True
        elif you=='p':
            print('\ncomputer cut the paper with his cesar\n')
            return False
    


print('''
__        __   _                          
\ \      / /__| | ___ ___  _ __ ___   ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
  \ V  V /  __/ | (_| (_) | | | | | |  __/
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
  _          _   _                        
 | |_ ___   | |_| |__   ___               
 | __/ _ \  | __| '_ \ / _ \              
 | || (_) | | |_| | | |  __/              
  \__\___/   \__|_| |_|\___|              
    ____                                  
   / ___| __ _ _ __ ___   ___             
  | |  _ / _` | '_ ` _ \ / _ \            
  | |_| | (_| | | | | | |  __/            
   \____|\__,_|_| |_| |_|\___|            
                                          ''')




print('comp turn : stonr(s),paper(p), Cesar(c)? :')
randNo=random. randint(1,3)

if (randNo==1):
    comp='s'
elif(randNo==2):
    comp='p'
else:
    comp='c'

you=input('your turn : stonr(s),paper(p), Cesar(c)? :')
print('\n')
print(""" ****************RESULTS****************""")
print('\n')

a=gameWin(comp, you)
if a==None:
    print("our game is tie")
elif a:
    print("you win ^-^")
else:
    print("you loss ×_×" )

print('\n')
print('computer choose : ',comp, '\n')
if comp=='s':
# Rock
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif comp=='p':
# Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
# Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

print('you choose : ',you, '\n')
if you=='s':
# Rock
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif you=='p':
# Paper
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
else:
# Scissors
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)







                   
                       
