from settings import *
from birdy.twitter import StreamClient


client = StreamClient(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)


resource = client.userstream.user.post(
    track = 'trump',
)


for data in resource.stream():
    print data
