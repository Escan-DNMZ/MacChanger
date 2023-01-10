import subprocess
import optparse
import re

def AddParseObject():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="Interface",help="Interface to change!")
    parse_object.add_option("-m","--mac-adress",dest="macAdress",help="Mac adress to change!")
  
    return  parse_object.parse_args()

def ChangeMac(user_interface,user_macAdress):
    print("Mac Changed !")
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_macAdress])
    subprocess.call(["ifconfig",user_interface,"up"])


def ControlNewMac(MacAdress):
    new_mac = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", MacAdress)
    

    if new_mac:
        return new_mac.group(0)
    else:
        return None

if __name__ == "__main__":
    (user_input, arguments) = AddParseObject()
    ChangeMac(user_input.Interface,user_input.macAdress)
    Finalized_mac = ControlNewMac(user_input.macAdress)
    
    if Finalized_mac == user_input.macAdress:
        print("Success!")
    else:
        print("Wrong mac adress!")