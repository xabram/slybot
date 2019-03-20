import json, tweepy

class TwitterBot:
    secrets = {}
    api = None

    def __init__(self):
        self.importSecrets("./secrets.json")
        self.initApi()

    def importSecrets(self, secretFile):
        f = open(secretFile, "r")
        self.secrets = json.loads(f.read())

    def run(self):
        print("ehllo")
        user = self.api.me()
        print (user.name)

    def initApi(self):
        auth = tweepy.OAuthHandler(self.secrets["apiKey"], self.secrets["apiSecretKey"])
        auth.set_access_token(self.secrets["accessToken"], self.secrets["accessTokenSecret"])
        self.api = tweepy.API(auth)