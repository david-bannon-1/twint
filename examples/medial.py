#! python

# Use below instruction to run this example
# git clone https://github.com/david-bannon-1/twint.git
# export PYTHONPATH=$PWD/twint
# python ./twint/examples/medial.py

import twint

tweets = []
c = twint.Config()
c.Username = 'NewsroomNZ'
c.Limit = 20
c.Store_object = True
c.Videos = True
c.Store_object_tweets_list = tweets
twint.run.Search(c)

for i in range(len(tweets)):
    print("==================================================")
    print("tweets[{0}]:".format(i))
    print("==================================================")
    if not tweets[i].video:
        continue
    for v in range(len(tweets[i].videos)):
        print("==================================================")
        print("        video {0}".format(v))
        print("==================================================")
        for k, v in tweets[i].videos[v].items():
            print("{0}: {1}".format(k, v))

