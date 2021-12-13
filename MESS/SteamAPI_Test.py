
from auth import steamKey
import requests
tag = "76561198822364887"

urlFriends = f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={steamKey}&steamid={tag}&relationship=friend"
responseFriends = requests.get(urlFriends)
dataFriends = responseFriends.json()
print(dataFriends)

urlGames = f"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={steamKey}&steamid={tag}&format=json"
responseGames = requests.get(urlGames)
dataGames = responseGames.json()
print(dataGames)
