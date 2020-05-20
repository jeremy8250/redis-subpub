import redis


class Subscriber:
    def __init__(self):
        self.conn = redis.Redis(host='10.211.55.6', port=6379)

    def subscribe(self, *channel):
        pub = self.conn.pubsub()
        pub.subscribe(*channel)
        data_list = []
        for key in pub.listen():
            if key['type'] == 'message':
                data_list.append(key['data'])
                print(key['channel'], key['data'], len(data_list))


if __name__ == '__main__':
    Subscriber().subscribe("channel1", "channel2", "channel3", "channel4", "channel5")
