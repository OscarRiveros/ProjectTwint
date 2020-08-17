import twint

c = twint.Config()
c.Username = "@user"
c.Search = "#COVID19"
c.Database = "saludcoivd.db"
#c.User_full = True

twint.run.Search(c)
# twint.run.Followers(c)
