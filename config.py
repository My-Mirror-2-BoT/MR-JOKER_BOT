# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/mrjoker/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7379273  # integer value, dont use ""
    API_HASH = "44f2305a4da8a1a2259de098a2fe46db"
    TOKEN = "2092128001:AAEixtiEGfb4-DwnL7XtQ0nVBGNNEKQlaL8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 940787324  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "ammxturtle"
    SUPPORT_CHAT = "lkhitech"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001641630640
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001641630640
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://wcsentxygtdipb:49a8b3ae97ef28248e2253de412887f4fbf6faad0f139e67c650b6a9189cb555@ec2-3-221-109-227.compute-1.amazonaws.com:5432/d4i5393abmmmjo"  # needed for any database modules
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "PwfI7MjOIsclMOUDh9X015uvQOeuabxIRnxjUMH7zJ4gnPWxj77jU42h1G62hjbq"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "LY3U6JWYJJLBVA6I"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "F5QOQPM9X22I"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "hmmm"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "hmmm"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
