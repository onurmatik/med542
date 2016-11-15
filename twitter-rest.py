from settings import *
from birdy.twitter import UserClient

client = UserClient(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)

resource = client.api.search.tweets.get(
    q='#trump',
    count=20,
)

for tweet in resource.data.statuses:
    print tweet
