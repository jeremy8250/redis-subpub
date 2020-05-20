import os
from threading import Thread

import redis


class SubPub:

    def __init__(self):
        self.conn = redis.Redis(host='10.211.55.6', port=6379)
        self.channel = "CHANNEL"

    def redis_sub(self):
        ps = self.conn.pubsub()
        ps.subscribe(self.channel)
        for item in ps.listen():
            print(item)

    def redis_pub(self, msg):
        self.conn.publish(self.channel, msg)


if __name__ == '__main__':
    subpub = SubPub()
    thread_sub = Thread(target=subpub.redis_sub())
    thread_sub.start()

    thread_pub = Thread(target=subpub.redis_pub(), args=("MESSAGE",))
    thread_pub.start()

