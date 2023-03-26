import requests
# import os

# os.getenv("key")

#export key using export KEY=value
abi_chat_id = "5052607310"
bot_token =""
chat_id = "510122498"
def send_message(bot_message):
    global chat_id, bot_token
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    response.raise_for_status()
# print(response.json())

send_message("Test message 1")

def get_chat_response():
    telegram_updates_api_url = "https://api.telegram.org/bot6135807067:AAFxIp2Mj7nLgogO2ZOT8tdrqktmsiyElBw/getUpdates"
    chat_responses = requests.get(telegram_updates_api_url)
    chat_reponses_json = chat_responses.json()
    # result_set = chat_reponses_json.get("result")
    # print(chat_reponses_json.get("result")[-1]["message"]["text"])
    return chat_reponses_json


user_chat_id = get_chat_response().get("result")[-1]["message"]["from"]["id"]


# print("\n"+str(user_chat_id))
if str(user_chat_id) == chat_id:
    message_text = get_chat_response().get("result")[-1]["message"]["text"]
    print(get_chat_response().get("result")[-1]["message"]["text"])
    send_message(message_text)
# print("\n\n\n")
# print(result_set[-1])

