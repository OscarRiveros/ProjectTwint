import twint

c = twint.Config()
c.Username = "@user"
c.Database = "user.db"
c.User_full = True

twint.run.Followers(c)
