import socket, struct, requests
import pyautogui as pag



debug = True



send = lambda set: requests.post("https://script.google.com/macros/s/AKfycbwvhNBhf5_kf7Yw2e6-evI6WjyjoadpVFgm8WQ6W1YGmr5wEhmWILGq-gnyuZxfTIyu/exec", headers={'Content-Type': 'charset=UTF-8'},data=str(set))
try:
    c = send("u")
    if send("ping") == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(("", 8889))
        while True:
            data, addr = s.recvfrom(4096)
            rawdata = bytearray(data)[0]
            if rawdata == 1:
                key = struct.unpack(c, rawdata)
                if debug:
                    send(key)
                    print(key)
                match key[3]:
                    case 28:
                        pag.press('d')
                        pass
                    case 29:
                        pag.press('a')
                        pass
                match key[4]:
                    case 30:
                        pag.press('w')
                        pass
                    case 31:
                        pag.press('s')
                        pass
    exit()
except Exception as e:
    print(e)
    exit()
