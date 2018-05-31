class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    # Fix is : set base condition
	if stream.__class__ == EvenStream:
        stream.current=0
    else:
        stream.current=1
    for _ in range(n):
        print stream.get_next()

queries = int(raw_input())
for _ in range(queries):
    stream_name, n = raw_input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())