from tools import *
post = {'character_id':1}
select2 = "card_name"
table = 'm_card'
print(create_command(post,select2,table))
print(select('/static/db/t7s.db',create_command(post,select2,table)))