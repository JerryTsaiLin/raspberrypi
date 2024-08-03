import os.path
import random
from datetime import datetime

def created_logfile(folder:str,file:str)->str:
    current_path=os.path.abspath(__name__)#取得目前檔案路徑
    directory_name=os.path.dirname(current_path) #取得目前目錄名稱
    data_path=os.path.join(directory_name,folder)#目前資料夾路徑上加上data目錄
    if not os.path.isdir(data_path):
        print("沒有data的目錄,手動建立目錄")
        os.mkdir(data_path)
    else:
        print("目錄已建立!") 

    log_path=os.path.join(data_path,file)

    if not os.path.isfile(log_path):
        with open(log_path,mode='w',encoding='utf-8',newline=None) as file:
            file.write("時間,溼度,溫度\n")

    else:
        print("have file")

  
    return log_path


def record_info(log_path):
   
    now=datetime.now()
    now_str=now.strftime('%Y-%m-%d %H:%M:%S')

    humidity=str(random.randint(330,820)/10)
    celsius=str(random.randint(50,400)/10)

    with open(log_path,mode='a',encoding='utf-8', newline='') as file:
    # file.write('2024-07-27 15:30:33, 70.5,29.5\n')
        file.write(now_str + ', ' + humidity + ',' + celsius + "\n")


def main():
    log_path=created_logfile(folder='data',file='iot.log')

    record_info(log_path)
   

   

if __name__=='__main__':
    main()

