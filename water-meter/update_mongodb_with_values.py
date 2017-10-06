#!/usr/bin/python

import sys
import datetime
from pymongo import MongoClient

if len(sys.argv) > 1:
    amount = str(sys.argv[1])
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.water_meter

    usage = {"amount": amount, "date": datetime.datetime.utcnow()}

    usages = db.usages
    usage_id = usages.insert_one(usage).inserted_id
    print "Updated mongodb", usage_id
else:
   sys.exit()

