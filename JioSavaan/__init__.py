from JioSavaan.core.bot import Anony, # nobita
from JioSavaan.core.dir import dirr
from JioSavaan.core.git import git
from JioSavaan.core.userbot import Userbot
from JioSavaan.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()
#iapp = nobita

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
