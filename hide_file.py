import subprocess
import crc_task
import os



def start():
    if len(open("user_info.inf", "r").readlines()) != 0:
        password = input("enter password:")
        info = open("user_info.inf")
        password_crc = info.readline()
        if str(crc_task.get_control_sum(password)) == password_crc[:-1]:
            main(info)
        else:
            print("access denied")
    else:
        open("user_info.inf", "w").write(str(crc_task.get_control_sum(input("user data not founded. enter password:"))))
        hide("user_info.inf")
        print("complete!")
        start()

def main(info):
    while(True):
        print('1. Hide new file')
        print('2. Show hidden files')
        print('3. Unhide one of the files')
        command=input()
        if(command=="1"):
            hide(input("file address:"))
        elif(command=="2"):
            for file in info.readlines():
                print(file)
        elif(command=="3"):
            for i in range(0..len(info.readlines())):
                print(str(i)+':'+file)




def hide(file_address:str):
    subprocess.check_call(["attrib", "+S", "+H", file_address])


def unhide(file_address: str):
    subprocess.check_call(["attrib", "-S", "-H", file_address])
