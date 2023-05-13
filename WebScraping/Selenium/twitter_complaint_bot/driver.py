from main import InternetSpeedTwitterBot

speed_test = InternetSpeedTwitterBot()
print(speed_test.get_internet_speed())
speed_test.tweet_at_provider()