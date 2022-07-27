
import redis
import pickle


class RedisConn:

    #Todo: add values seperately (uav, gcs, etc...)


    def __init__(self, host='localhost', port=6379, db=0, reset_values=True):

        self.client = redis.Redis(host=host, port=port, db=db)

        self.keys = ['test']

        if reset_values: self.reset_values()
        

    def set_value(self, key, value, pickle_encode=True, ex=None):

        value = pickle.dumps(value) if pickle_encode else value
        self.client.set(key, value, ex=ex)


    def get_value(self, key, pickle_decode=True):

        value = self.client.get(key)
        if not value: return None
        return pickle.loads(value) if pickle_decode else value


    def reset_values(self, keys=None):

        if keys is None: keys = self.keys

        for key in keys: self.client.delete(key)

if __name__ == '__main__':

    r = RedisConn()

    value = ('a', 'b', 'c') #! you can't add tupple directly (need to code st. like pickle)

    r.set_value('test', value)
    print(r.get_value('test'))

    r.reset_values()