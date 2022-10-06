import datetime
import json

import functions_framework
import pymongo
import os
import bson.json_util as json_util


@functions_framework.http
def workouts_month(request):
    if request.method == "GET":
        # request_json = request.get_json(silent=True)
        request_args = request.args
        month = request_args["month"]
        year = request_args["year"]
        client = pymongo.MongoClient(os.getenv("DB_URL"))
        db = client['workouts']
        work_collection = db['workouts']
        workouts_cursor = work_collection.find({"month": month}).sort("record", -1)
            # .find({"month": month, "creation_date": {"$gt": year}}).sort("record", -1)
        workouts = []
        for work in workouts_cursor:
            print(work.get("workout_date")[0:4])
            print("\n")
            if work.get("workout_date")[0:4] == year:
                workouts.append(work)
        print(">>> workouts data: \n")
        print(workouts)
        # d = Headers()
        # d.add('Content-Type', 'text/plain')
        return json_util.dumps(workouts), 200, {'ContentType': 'application/json'}
    return "TEST"
