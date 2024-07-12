import requests

"""

[ UNDER CONSTRUCTION ]

"""

base_url = "http://192.168.1.58:80"

def allRelaysOn():
    url_on = f"{base_url}/relay/on"
    response_on = requests.get(url_on)
    print("Status Code (on):", response_on.status_code)
    print("Response Content (on):", response_on.text)

def allRelaysOff():
    url_off = f"{base_url}/relay/off"
    response_off = requests.get(url_off)
    print("Status Code (off):", response_off.status_code)
    print("Response Content (off):", response_off.text)

def specialPinControl(pinNumber:int):
    pin = pinNumber
    url_pin = f"{base_url}/relay/{pin}"
    params = {'relay_action': 'on'}
    response_pin = requests.get(url_pin, params=params)
    print("Status Code (pin):", response_pin.status_code)
    print("Response Content (pin):", response_pin.text)

pinList = [2, 4, 5, 18, 19, 21, 22, 23]
while 1:
    x = input(">> ")

    try:
        x = int(x)
        specialPinControl(pinNumber=int(x))
    except:
        if "on" in x:
            allRelaysOn()
        elif "off" in x:
            allRelaysOff()
        elif "sequence" in x:
            for i in pinList:   
                specialPinControl(pinNumber=i)
        
    
