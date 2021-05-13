# import requests
# import json
# import sqlite3

# city = input("ქალაქი: \n")
# city = "Rustavi"
# APIkey ='37c34af76979802bd994715e3671c7ad'
#
# payload = {"q" : city, "appid" : APIkey, "units" : "metric"}
# resp = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)
# print(resp.headers)
# print(resp.content)
# print(resp.status_code)
# res = json.loads(resp.text)
# print("ამჟამინდელი ტემპერატურა: ",res["main"]['temp'])
# print(json.dumps(res,indent=4))
# with open("data.json",'w') as f:
#     json.dump(res,f,indent=4)
#
#
# print(res['coord'])


# conn = sqlite3.connect('newtable.sqlite')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS weather(
#                 city varchar primary key ,
#                 weather integer);''')
#
# cursor.execute('''INSERT INTO weather(city,weather) VALUES('Rustavi',30)''')
# conn.commit()
# conn.close()