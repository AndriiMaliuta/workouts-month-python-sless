import json

import functions_framework
import pymongo
import os


@functions_framework.http
def workouts_month(request):
    if request.method == "GET":
        # request_json = request.get_json(silent=True)
        request_args = request.args
        month = request_args["month"]
        client = pymongo.MongoClient(os.getenv("DB_URL"))
        db = client['workouts']
        work_collection = db['workouts']
        # today = datetime.datetime.now()
        workouts_cursor = work_collection.find({"month": month})
        workouts = []
        for work in workouts_cursor:
            workouts.append(work)
        return json.dumps(workouts)
    return "TEST"
