
from __future__ import print_function

from sys import argv

import redis, redis_lock

class RedisLockClient:
    LOCK_ID = 'relock'

    def __init__(self, **kwargs):
        self.redis = redis.StrictRedis(**kwargs)

    def do_lock(self, lock_name):
        lock = redis_lock.Lock(self.redis, lock_name, id=RedisLockClient.LOCK_ID)
        lock.acquire(blocking=True)
        return 'OK'

    def do_try(self, lock_name):
        lock = redis_lock.Lock(self.redis, lock_name, id=RedisLockClient.LOCK_ID)
        if lock.acquire(blocking=False):
            return 'OK'
        else:
            return 'FAIL'

    def do_release(self, lock_name):
        lock = redis_lock.Lock(self.redis, lock_name, id=RedisLockClient.LOCK_ID)
        lock.release(force=True)
        return 'OK'


def print_usage():
    print('Usage: relock.py <lock|try|release> <name of the lock>')

if __name__ == '__main__':
    if len(argv) < 3:
        print_usage()
        exit(1)

    command, lock_name = argv[1], argv[2]

    redis_client = RedisLockClient()
    try:
        if command == 'lock':
            result_code = redis_client.do_lock(lock_name)
        elif command == 'release':
            result_code = redis_client.do_release(lock_name)
        elif command == 'try':
            result_code = redis_client.do_try(lock_name)
        else:
            print('invalid command: %s' % command)
            print_usage()
            exit(1)

        print(result_code)
        exit(0)
    except Exception as e:
        print('FAIL\n%s' % e)
        exit(1)

