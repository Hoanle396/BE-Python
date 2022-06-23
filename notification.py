# from gcm import * 
# gcm = GCM("AIzaSyDejSxmynqJzzBdyrCS-IqMhp0BxiGWL1M") 
# data = {'the_message': 'You have x new friends', 'param2': 'value2'}  
# reg_id = 'APA91bHDRCRNIGHpOfxivgwQt6ZFK3isuW4aTUOFwMI9qJ6MGDpC3MlOWHtEoe8k6PAKo0H_g2gXhETDO1dDKKxgP5LGulZQxTeNZSwva7tsIL3pvfNksgl0wu1xGbHyQxp2CexeZDKEzvugwyB5hywqvT1-UxxxqpL4EUXTWOm0RXE5CrpMk'  
# gcm.plaintext_request(registration_id=reg_id, data=data)

from flask import Flask
from flask_apscheduler import APScheduler
i=0
app = Flask(__name__)
scheduler = APScheduler()

def scheduleTask():
   print("This test runs every 5 seconds")

if __name__ == '__main__':
    scheduler.add_job(id = 'Scheduled Task', func=scheduleTask, trigger="interval", seconds=5)
    scheduler.start()
    app.run(host="0.0.0.0")