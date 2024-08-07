import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 22857219))
API_HASH = getenv("API_HASH", "fc4240745f2feebfa7ef4de6fc14acf0")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6939587552:AAGUMZsejOH_ZgLTEzHmlEFLnv01SnFHHJg")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://rohat6432:Lolo1907@cluster0.welyfih.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 33))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 1001891680771))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 5988763828))

CEDRIC_ID = int(getenv("CEDRIC_ID", 5942562577))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AdanaliMuhendis/AviaxMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SohbetAlemi")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Alemciyiz")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 33))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "BAFcxgMAYSlg8_HFt2CUkQQaPs87NXaEUyoTWgyKh3GXibiCgWt5cc0RaWXr5tVtRVEqlQFDEhi8jiou61lAp_k6Iine_3YezzctRCq38HgFU9BuHY6zVo6ULYjOKuynAo3mPnZjD3RMrl8NfDDl6JOJd1c_HUUpOgpciSQstVRR9lK6BsKfyRP9zg8qB8lvGh7WKITgH0xUSpAEvmXiLlJuRx4dffKcy1B-ssnducbq-TYKuhTj3_echnjWNEtwvTwEyFWCuBs_hMzHfXpwFtlWEdEZu_aHLyKeePqu8wBMkLAtLPpEE5FJC_7dVFfBjtztRuIGKeDG9kX-3GilYSMs6jRRsQAAAAFiNE8RAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/Alem-Music-06-01"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/Alem-Music-06-01"
)
PLAYLIST_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
STATS_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
TELEGRAM_AUDIO_URL = "https://telegra.ph/Alem-Music-06-01"
TELEGRAM_VIDEO_URL = "https://telegra.ph/Alem-Music-06-01"
STREAM_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
SOUNCLOUD_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
YOUTUBE_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/Alem-Music-06-01"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/Alem-Music-06-01"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
