delete from m_card_type;
REPLACE INTO `m_card_type` (`card_type_id`,`class`,`is_superior`,`type_name`) VALUES
 ('1','1','0','ボーカリスト'),
 ('2','2','0','バラドル'),
 ('3','3','0','モデル'),
 ('4','4','0','プレイヤー'),
 ('5','5','0','ダンサー'),
 ('6','1','1','ゴッドボイス'),
 ('7','2','1','コメディエンヌ'),
 ('8','3','1','アクトレス'),
 ('9','4','1','スタープレイヤー'),
 ('10','5','1','トリックスター'),
 ('11','6','0','ノータイプ'); ');
