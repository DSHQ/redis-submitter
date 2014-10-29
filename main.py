__author__ = 'ob3'



from core.model import Model
from lib.worker import Worker
from conf.database import redis
import json
import logging

from data.default import template

db = Model()
worker = Worker()

worker.setName('Thread 1')
worker.start()
# worker.join()

pattern = template()


subs = db.redis.pubsub()

for pat in pattern.pattern_subscriber:
    subs.psubscribe(pat)

logging.info("start listening")

for item in subs.listen():
    # print item
    if item['pattern'] is not None:
        try:
            item['data'] = json.loads(item['data'])
        except:
            continue

        logging.info("publishing message")
        out = json.dumps(item)
        db.redis.lpush(redis.queue_key, out)
        # print item
        pass