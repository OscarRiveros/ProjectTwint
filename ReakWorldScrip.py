import twint

# get the followers first
c = twint.Config()
c.Username = "@user"
c.Store_object = True
c.User_full = True

twint.run.Followers(c)

# save them in a list
target_followers = twint.output.users_list

# iterate over them and save in a new list
K_followers = []

for user in target_followers:
    if user.followers >= 100:
        K_followers.append(user)

# now we can save them in an CSV file, for example
with open('K_followers.csv', 'w') as output:
    output.write('id,username,followers, following, location\n')
    for u in K_followers:
        output.write('{},{},{},{},{}\n'.format(
            u.id, u.username, u.followers, u.following, u.location))
