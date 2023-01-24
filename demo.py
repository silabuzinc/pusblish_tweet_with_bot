import tweepy
import inspect
from rich import print
import configparser

config = configparser.ConfigParser(interpolation=None)
config.read("./config.ini")


def getClient(user):
    consumer_key = config["twitter"]["consumer_key"]
    consumer_secret = config["twitter"]["consumer_secret"]
    access_token = config[user]["access_token"]
    access_token_secret = config[user]["access_token_secret"]
    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    return client


def main():
    client = getClient("giru")
    message = """
    El gran olvidado de la primera vuelta al mundo 🗺 : el capitán burgalés Gonzalo Gómez de Espinosa
    
    Viaje de #Magallanes - #Elcano
    #ImperioEspañol
    
    https://www.youtube.com/watch?v=Lsn1I0bQrQc
    """
    text_tweet = inspect.cleandoc(message)
    print(len(text_tweet))
    client.create_tweet(text=text_tweet)  # , quote_tweet_id="1511399666096779273")


if __name__ == "__main__":
    main()