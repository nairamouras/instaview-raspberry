import os 
  
restart = input("Do you wish to restart your computer ? (y / n): ") 
  
if restart == 'n':
    print("saindo...")
    exit() 
else: 
    os.system("shutdown /h")
    os.system("shutdown /r /t 30")