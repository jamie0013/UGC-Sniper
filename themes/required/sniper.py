# EXAMPLE SNIPER WITH ONLY THE VARIABLES

class Sniper:
    def __init__(self):
        self.errors = 0
        self._time = 0
        self.speed = 0
        self.finder_speed = 0
        self.bought = 0
        self.boughtpaid = 0
        self.checks_made = 0
        self.ratelimits = 0
        self.proxies_switched = 0
        self.stats = "N/A"
        self.proxy = "N/A"
        self.version = VERSION

        self.limiteds = []

        self.mode = ""
        self.mode_time = False
        self.minutes = int(conf["time wait minutes"])
        self.unix = math.floor(conf["time wait unix"])
        self.cooldown = 0
        self.checker_cooldown = 0
        self.userinfo = {"id": 1, "name": "J3ldo", "displayName": "J3ldo"}