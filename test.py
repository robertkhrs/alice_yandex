from requests import post

print(post('http://127.0.0.1:5000/post',
           json={
               "meta": {
                   "locale": "ru-RU",
                   "timezone": "UTC",
                   "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                   "interfaces": {
                       "screen": {},
                       "payments": {},
                       "account_linking": {}
                   }
               },
               "session": {
                   "message_id": 4,
                   "session_id": "3ca92223-d955-474f-bb9b-945a32eadd01",
                   "skill_id": "7b8700dd-de6a-49ec-802e-52df16c98f3a",
                   "user": {
                       "user_id": "46C129B4B6779900C9B190E8E63D19DF317F676EED91989B2A50AB58ABCBAFB1"
                   },
                   "application": {
                       "application_id": "D1798DFD7A5774631E718BDA43E30943E2EDD9F29603753E6DECB5AEBE4E5F55"
                   },
                   "new": False,
                   "user_id": "D1798DFD7A5774631E718BDA43E30943E2EDD9F29603753E6DECB5AEBE4E5F55"
               },
               "request": {
                   "command": "ладно",
                   "original_utterance": "Ладно",
                   "nlu": {
                       "tokens": [
                           "ладно"
                       ],
                       "entities": [],
                       "intents": {}
                   },
                   "markup": {
                       "dangerous_context": False
                   },
                   "type": "SimpleUtterance"
               },
               "version": "1.0"
           }).json())
