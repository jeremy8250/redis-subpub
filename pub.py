import redis


class Publisher:
    def __init__(self):
        self.conn = redis.Redis(host='10.211.55.6', port=6379)

    def msg_gen(self):
        msg_body = "message_"
        seq = list(range(1, 10001))
        msg_list = []
        for i in seq:
            msg_list.append((msg_body + str(i)))
        return msg_list

    def publish(self, channel, msg):
        # 向特定频道发布消息
        self.conn.publish(channel, msg)


if __name__ == '__main__':
    publisher = Publisher()
    msg_data = publisher.msg_gen()
    for data in msg_data:
        publisher.publish("channel1", data)
    for data in msg_data:
        publisher.publish("channel2", data)
    for data in msg_data:
        publisher.publish("channel3", data)
    for data in msg_data:
        publisher.publish("channel4", data)
    for data in msg_data:
        publisher.publish("channel5", data)
