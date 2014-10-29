from conf.database import redis as redis_conf
import redis as engine



class Model(object):

    redis = None
    redis_conf = redis_conf.redis1

    def __init__(self):
        self.redis = engine.StrictRedis(host=self.redis_conf['host'], port=self.redis_conf['port'], db=self.redis_conf['db'])
