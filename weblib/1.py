import csv
from app import db,models

csvfile = file('1.csv', 'rb')
reader = csv.reader(csvfile)
for line in reader:
    tmp = models.Seat(num=int(line[0]),floor=int(line[1]),elec=int(line[2]),
                      water=int(line[3]),sun=int(line[4]),lift=int(line[5]))
    db.session.add(tmp)
db.session.commit()

csvfile.close() 
