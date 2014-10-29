__author__ = 'ob3'

from threading import Thread
from core.model import Model
from conf.database import redis as conf
import json
import time
from lib.submitter import Submitter

from siesta import API


from data.default import template

class Worker(Thread):

    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        db = Model()
        submitter = Submitter()
        while True:
            item = db.redis.rpop(conf.queue_key)

            if item is not None:
                item = json.loads(item)
                channel = item['channel'].split("::")

                pattern = template()
                if not (item['pattern'] in pattern.pattern_subscriber):
                    continue

                targets = pattern.pattern_subscriber[item['pattern']]
                for target in targets:
                    if target in pattern.subscriber_detail:

                        url = pattern.subscriber_detail[target]['url']
                        method = pattern.subscriber_detail[target]['method']

                        # import requests
                        # r = requests.get(url)
                        # methodToCall = getattr(submitter, method)
                        # result = methodToCall(url=url, data=item['data'])

                        result = submitter.request(url=url, method=method, data=item)
                        print result[1]





            else:
                time.sleep(1)

            pass
