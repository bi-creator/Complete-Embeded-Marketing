import requests
import webbrowser
def postimg():
    url = 'http://127.0.0.1:8000/uploadImage'
    files = {'file': open('E:\\Embedded_Marketing\\m2\\runs\\detect\\exp\\crops\\handbag\\Frame.jpg', 'rb')}
    # requests.post(url, file=files)
    r = requests.post(url, files=files)
    print(r)
    lable='brown handbag women'
    webbrowser.open(f'http://localhost:3000/?itemName={lable}')
    return