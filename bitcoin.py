import requests
import time
import datetime

BITCOIN_API_URL = "https://blockchain.info/ticker"


def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    try:
        if response == 'Response [200]':
            #pass
            print(response)
            #check that .json() did NOT return an empty dict
        if len(response.json()):
            response_dict = response.json()
            #print(response.json())
            #print(response_dict["USD"])
            usd_dict = response_dict["USD"]
            print(usd_dict['last'])
            return usd_dict['last']
    except ValueError:
        print("no JSON returned")


def main():
    last_time = datetime.datetime.now()  # keep track of the time
    last_time_inseconds = last_time.timestamp()
    print(f'last time: {int(last_time_inseconds)}')
    bitcoin_history = []
    SECONDS_BETWEEN_AVERAGE = 60

    while True:
        price = get_latest_bitcoin_price()
        bitcoin_history.append(price)
        # Sleep for 10 seconds
        time.sleep(10)
        current_time = datetime.datetime.now()
        current_time_inseconds = current_time.timestamp()
        print(f'current time: {int(current_time_inseconds)}')
        # print Average value over the last 10 minutes
        if (int(current_time_inseconds) - int(last_time_inseconds)) >= SECONDS_BETWEEN_AVERAGE:
            print(f'This is bitcoin history: {bitcoin_history}')
            bitcoin_average = sum(bitcoin_history) / len(bitcoin_history)
            print(f'Bitcoin Average is: {"{:.2f}".format(bitcoin_average)}')
            last_time_inseconds = current_time_inseconds
            bitcoin_history = [] #Reset the list

if __name__ == '__main__':
    main()
