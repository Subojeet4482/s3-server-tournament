"""SERVER-3  -  chat system, friends, chat profile, groups, world chat, Coin Battle game   (DB3)"""
from common.appfactory import create_app
from modules import chat_mod, game_mod, bomb_mod

app = create_app("s3", "Server-3 (chat / friends / game)", [chat_mod, game_mod, bomb_mod], caps=("chat",), dbs=("DB3",))
