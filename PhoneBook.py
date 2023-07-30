import os

PATH = "Your File Address Here" ##Example : C:\...##

def validation():
    if not os.path.exists(PATH):
        f = open(PATH, "w+")
        f.write("")



def add(name, number):
    validation()
    f = open(PATH, "a+")
    new_phone =f'{name}:{number} \n'
    f.write(new_phone)
    f.close()



def search(name):
    validation()
    f = open(PATH,"r")
    for line in f.readlines():
        if name == line.split(":")[0]:
            print(f'{name}  :  {line.split(":")[1]}')
    f.close()


def delete(name):
    validation()

    f = open(PATH, "r")
    new_database = ""
    for line in f.readlines():
        if not name == line.split(":")[0]:
            new_database += line
    f.close()
    f = open(PATH,'w')
    f.write(new_database)

def show_all():
    validation()
    f = open(PATH,"r")
    database= ""
    database = f.read()
    f.close()
    print(database)
  
ch = 1

while ch != 0:
    print('1-Add User \n2-Search Phone \n3-Delete Phone \n4-Show All \n0-Exit')
    ch = int(input('Enter Your Choice :'))
    os.system('cls')

    if ch == 1:
        name = input('Enter Name : ')
        number  = int(input('Enter Number : '))
        add(name,number)

    elif ch ==2:
         name = input('Enter Name :')
         search(name)
             
    elif ch ==3:
         name = input('Enter Name : ')
         delete(name)
             
    elif ch== 4:
        show_all()
