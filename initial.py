from tools import *


db = "static/db/t7s.db"
ver = version()
select_list = dict()


select_list["Character"] = select(db, "SELECT character_id, first_name from m_character")
select_list["Rarity"] = select(db, "SELECT rarity_id, rarity_abbreviation from m_rarity")
select_list["Card type"] = select(db, "SELECT card_type_id, type_name from m_card_type")
select_list["Card class"] = select(db, "SELECT class, type_name from m_card_type")