import twint


import twint

c = twint.Config()

c.Username = "oscarrriveros"
c.Limit = 20
c.Store_object = True
twint.run.Lookup(c)
twint.run.Followers(c)

followers = twint.output.follows_list


"""
# Configure
c = twint.Config()
c.Username = "@oscarrriveros"
c.Search = "Muerte"

# Run
twint.run.Search(c)
#twint.run.Lookup(c)
#twint -u @oscarrriveros -o file.csv --csv
import twint

c = twint.Config()

c.Username = "@frioss_"
c.Limit = 20
c.Store_object = True

twint.run.Followers(c)
followers = twint.output.follows_list
"""
"""
import twint

c = twint.Config()

c.Username = "@frioss_"
c.Limit = 20
c.Store_object = True
c.User_full = True

twint.run.Followers(c)
users = twint.output.users_list


"""
"""
import twint

c = twint.Config()
c.Username = "@frioss_"
twint.run.Following(c)
#twint.run.Search(c)


import twint

c = twint.Config()

c.Username = "@frioss_"
c.Custom["tweet"] = ["id"]
c.Custom["user"] = ["bio"]
c.Limit = 10
c.Store_csv = True
c.Output = "none"

twint.run.Search(c)"""
