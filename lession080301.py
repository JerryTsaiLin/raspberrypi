from  tools.file import created_logfile,record_info
from datetime import datetime



def main():
    now=datetime.now()
    current_file_file=now.strftime('%Y_%m_%d.log')

    log_path=created_logfile(file=current_file_file)

    record_info(log_path)
   

   

if __name__=='__main__':
    main()

