import loady
import sys
import json
import time


class FakeQueue:
    def put(self, name):
        ts = time.strftime('%x %X')
        print('{}: {}'.format(ts, name))


def fake_trigger(name):
    ts = time.strftime('%x %X')
    print('{}: {}'.format(ts, name))


def run(config):
    with open(config, 'r') as cfg:
        config = json.load(cfg)

    typename = config.pop('typename')
    events = config.pop('events')
    trigger = loady.code.load(typename)

    t = trigger(None, events, **config)
    t.trigger = fake_trigger
    t.start()


if __name__ == '__main__':
    run(sys.argv[1])
