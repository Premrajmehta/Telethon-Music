import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21811692"))
    API_HASH = os.environ.get("API_HASH", "e4d341d803efd367f771547fc875a2bc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6283081154:AAHt7gLlpLzCcPufxyIh71PU6-db8X7VXnA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOI0Bux6XWv0DDnQ5Ocy-p0jkyVVRtAT4v6P92dbzLdwOnY068n_mJ7XcN4C68VVvZsMzo8R5iXejKsX6x5FAnb8JbbSy8qRXgzDNoBEmTniW0Z057t9sYrH9sNJtYiOelrCLn8fi1ANvTzdat2MkfdD3HpWoSbya6H9raZZ8QtofI6gfeVUn7Vg7yacGUQUA5jDC9Py9G_N9CS4NFuMd6tnnyyPHu-TKVWQ90Yy-3AvgJnE4afQO5R1vzR785UvRALBOPLIhZeMvwr7JAYPK8YmHTF2o4g6mp9twI-WXFoXdfscK-MbnuJUPN72bxtu7wHX3mL1M826HgIiAYO2y5RLtV90=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "None")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", "None")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Premrajmehtabot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1156137788")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "None") # Change it to "True"
