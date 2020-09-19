from tools import *


db = "/static/db/t7s.db"
ver = version()
select_list = dict()

select_list["character_id"] = select(db, "SELECT character_id, first_name from m_character")
print(select_list["character_id"])
select_list["rarity_id"] = select(db, "SELECT rarity_id, rarity_abbreviation from m_rarity")
select_list["card_type_id"] = select(db, "SELECT card_type_id, type_name from m_card_type")

select_name_list = dict()
select_name_list["character_id"] = '角色'
select_name_list["rarity_id"] = '稀有度'
select_name_list["card_type_id"] = '卡片种类'
