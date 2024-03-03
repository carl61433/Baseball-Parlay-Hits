class player():
    numPlayers = 0
    def __init__(self, name, stats):
        player.numPlayers += 1
        self.name = name
        self.stats = []

    def getName(self) -> str:
        return self.name
    
    def getStats(self):
        return self.stats
    



