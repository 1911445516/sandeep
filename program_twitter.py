import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "49JDrIFCoF6jhHHTGDTuVTfTU",
    "consumer_secret"     : "i7wfOFV5HE59jR2CnOC6pDxuFfuw51Qps14J8WhfppKRba6R4D",
    "access_token"        : "966151914764361728-FRxjv1UXoe41pjSjm4zkZLPgqWp2UWr",
    "access_token_secret" : "EWBmVLUzHVQsknkhXCyIJrrhCtxL6qstY63ICy8ge2nZg" 
    }

  api = get_api(cfg)
  tweet = "Hello, guys!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
