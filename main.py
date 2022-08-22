import requests
import time
import datetime

def request_api(servername):
    response=requests.get('http://'+servername+'/api/count').json()
    #response={"count": 42} #тестовый ответ
    return response
def main():
    servers=["maria.ru", "rose.ru", "sina.ru"]
    while servers!='maria': #Бесконечный цикл
        date=str(datetime.datetime.now()).split('.')[0]
        for server in servers:
            print(date+' '+server+' '+str(request_api(server).get("count")))
        time.sleep(60)
if __name__ == '__main__':
    main()

