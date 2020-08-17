import twint
import pandas as pd
from collections import Counter


users = [
    '@user1',
    '@user2',
]


def get_followings(username):

    c = twint.Config()
    c.Username = username
   # c.Limit = 20
    c.Pandas = True

    twint.run.Following(c)
    list_of_followings = twint.storage.panda.Follow_df

    return list_of_followings['followings'][username]


followings = {}
following_list = []
for person in users:
    print('#####\nStarting: ' + person + '\n#####')
    try:
        followings[person] = get_followings(person)
        following_list = following_list + followings[person]
        Counter(following_list) .most_common(10)
    except KeyError:
        print('IndexError')
"""
follow_relations ={}
for following_user in followings.keys():
    follow_relation_list = []
    for followed_user in followings.keys():
        if followed_user in followings[following_user]:
            follow_relation_list.append(True)
        else:
            follow_relation_list.append(False)
    follow_relations[following_user] = follow_relation_list


"""
