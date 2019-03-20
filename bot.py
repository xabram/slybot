class TwitterBot:
    def __init__(self):
        self.importSecrets("./secrets.json")

    def importSecrets(self, secretFile):
        print("import: " + secretFile)

    def run(self):
        print("ehllo")
