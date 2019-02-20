import redis


def check_redis_connection(**kwargs):
    host = kwargs['host']
    port = kwargs['port']
    db = kwargs['db']
    try:
        r = redis.Redis(host=host, port=port, db=db)
        r.set('foo', 'bar')
        value = r.get('foo')
        if value == 'bar':
            return True

        return False
    except Exception:
        return False
