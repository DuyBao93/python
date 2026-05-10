# netsh wlan set hostednetwork mode=allow ssid="" key=""

import subprocess
from getpass import getpass
#disconn = subprocess.run(['netsh', 'wlan', 'disconnect'])

# f = open("temple_pass.txt",'r+')
# list_pass = f.readlines()
# new = [element.rstrip() for element in list_pass] #remove /n in the last word
# 
# def run_as_admin(command):
#     process = subprocess.Popen(['runas', '/user:dell', command], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     # process.stdin.write((password.encode() + b'\r\n') *2)
#     # process.stdin.flush()
#     stdout, stderr = process.communicate()
#     return stdout, stderr, process.returncode
# def set_hosted():
#     subprocess.run(['netsh', 'wlan', 'set', 'hostednetwork' , 'mode=', 'allow', 'ssid=', '"Telecom-5"', 'key=', '"07102221"' ])
def run_as_admin(command, password):
    process = subprocess.run(['runas', '/user:dell', command])
    subprocess.Popen([password])
    return process
if __name__ == "__main__":
    # command_to_execute = "netsh wlan set hostednetwork mode=allow ssid=Telecom-5 key=07102221" 
    command_to_execute = "cmd /c dir"
    # admin_password = getpass("enter your password : ")
    admin_password = "Vob@o231019"
    process = run_as_admin(command_to_execute, admin_password)
    print(process.returncode)
    # conn = subprocess.run(['netsh', 'wlan', 'connect', 'name=','"Telecom-5"', 'ssid=','"Telecom-5"'])
    # if conn.returncode == 0:
    #     print("Connected")
    # else:
    #     print("fail")

# process = subprocess.run(["runas", "/user:dell", "/'set_hosted()/'"], check=True)
# f.writelines("\n98765432")
# conn = subprocess.run(['netsh', 'wlan', 'connect', 'name=','"Telecom-5"', 'ssid=','"Telecom-5"'])
#prof = subprocess.run(['netsh', 'wlan', 'show', 'profile'])

#inter = subprocess.run(['netsh', 'wlan', 'show', 'interface'])

#print(conn)
#print(conn.returncode)
# command = ["python", "-c", "import sys; print(sys.stdin.read())"]
# data_to_send = "Hello from parent process\n".encode()

# process = subprocess.Popen(
#     command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
# )
# process.stdin.write(data_to_send)
# process.stdin.close()

# stdout, stderr = process.communicate()

# print("Output:", stdout.decode())
# print("Error:", stderr.decode())
# print("Return code:", process.returncode)