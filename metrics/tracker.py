class Tracker:
    counter = 0

    @classmethod
    def increment(cls):
        cls.counter += 1

    @classmethod
    def get_count(cls):
        return cls.counter
