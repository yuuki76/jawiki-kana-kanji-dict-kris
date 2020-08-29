import pytest
from jawiki import skkdict

d = skkdict.parse_skkdict('SKK-JISYO.jawiki', encoding='utf-8')


@pytest.mark.parametrize("yomi", [
    ('きんぐぬー'),
    ('れいわ'),
    ('うちだかおる'),
    ('さかもとふじえ'),
    ('あかとりい'),
    ('いせきしこく'),
    ('きうちきょう'),
    ('おおとにー'),
    ('いんだらじゃえいげんまりゅう'),
    ('こちらかつしかくかめありこうえんまえはしゅつじょ'),
])
def test_yomo(yomi):
    assert yomi in d


@pytest.mark.parametrize("kanji,yomi", [
    ('アバンチュリエ級駆逐艦', 'あはんちゅりえきゆうくちくかん'),
    ('安蘇山', 'あそさん'),
    ('あに。', 'あにまる'),
    ('南夕子', 'みなみゆうこ'),
    ('青井惟董', 'あおいこれただ'),
    ('赤プル', 'あかぷる'),
    ('安藤孝子', 'あんどうたかこ'),
    ('EX大衆', 'いーえっくすたいしゅう'),
    ('古崤関', 'ここうかん'),
    ('鬼滅の刃', 'きめつのやいば'),
    ('鬱多羅僧', 'うったらそう'),
    ('三衣一鉢', 'さんねいっぱつ'),
    ('中川幸永', 'なかがわゆきえ'),
    ('姶良サティ', 'あいらさてぃ'),
    ('青木十良', 'あおきじゅうろう'),
    ('穴門みかん', 'あなとみかん'),
    ('Eye-Fi', 'あいふぁい'),
    ('ABBA', 'あば'),
    ('崎元酒造所', 'さきもとしゅぞうしょ'),
    ('志倉千代丸', 'しくらちよまる'),
    ('前田怜緒', 'まえだれお'),
    ('湊川四良兵衞', 'みなとがわしろべえ'),
    ('宮口しづえ', 'みやぐちしずえ'),
    ('吉本玲緒', 'よしもとれお'),
    ('若林令緒', 'わかばやしれお'),
    ('鷲谷いづみ', 'わしたにいずみ'),
    ('初井しづ枝', 'はついしずえ'),
    ('倉知玲鳳', 'くらちれお'),
])
def test_pair(kanji, yomi):
    print([kanji, yomi, d.get(yomi)])
    assert kanji in d.get(yomi)


@pytest.mark.parametrize("kanji,yomi", [
    # '''（初代）京山 華千代'''（きょうやま はなちよ、[[1904年]]（[[明治]]37年）[[8月11日]] - [[1983年]]（[[昭和]]58年）[[1月7日]]）
    # ('京山華千代' ,'きょうやまはなちよ'),
    ('お姉さま', 'ぼく'),
    ('109万本', 'いる'),
    ('擬餌状体', 'えすか'),
    ('銀河刑務所の囚人を全員脱獄させる。', 'えすか'),
    ('監督', 'あばんたいとる'),
    ('10代式守与太夫', 'しきもりよだゆう'),
    ('1703年の北アメリカ北東岸の襲撃', 'きたあめりかほくとうがんのしゅうげき'),
    ('島ぜんぶでおーきな祭', 'さい'),
    ('アジャリス', 'さんてぃあーご'),
    ('UTF-32', 'および'),
    ('江迎警察署 - 北部', 'および'),
    ('相補誤差関数', 'および'),
    ('二人で旅に出る理由は？', 'あいりす'),
    ('大切な者との記憶', 'きゅーぶ'),
    ('死者・行方不明者約2万2000人', 'うち'),
    ('死者273人', 'うち'),
    ('86校', 'うち'),
    ('INDIES', 'いんでぃーず'),
    ('ZAZZY', 'いんでぃーず'),
    ('長谷川榮', 'ゑい'),
    ('謝謝你，在世界的角落找到我', 'ありがとう'),
    ('謝謝你，在世界角落中找到我', 'ありがとう'),
    ('Five Colours in Her Hair', 'らいぶ'),
    ('LOVE Seiko Matsuda 20th Anniversary Best Selection', 'らゔ'),
    ('You♡I -Sweet Tuned by 5pb.-', 'ゆい'),
    ('尾道市土生幼稚園', 'めりー'),
    ('激突3&IMPACT.9', 'べーすめんともんすたー'),
    ('Guitar：Shin', 'しん'),
    ('Thank you, ROCK BANDS! 〜UNISON SQUARE GARDEN 15th Anniversary Tribute Album〜', 'さんきゅー'),
    ('日本初', 'かつ'),
    ('あなたがいるから、矢口真里', 'あなたがいるから'),
    ('島津安樹朗', 'あきお'),
    ('旭丘中学校、旭ヶ丘中学校、旭が丘中学校', 'あさひがおかちゅうがっこう'),
    ('旭酒造株式會社', 'あさひしゅぞう'),
    ('あしたはどっちだ、寺山修司', 'あしたはどっちだ'),
    ('青森県立木造高等学校', 'あおもりけんりつ'),
    ('青ヶ島酒造合資会社', 'あおがしましゅぞう'),
    ('御座船安宅丸', 'あたけまる'),
    ('福岡市立内浜小学校', 'うちはましょうがっこう'),
    ('東風汽車有限公司', 'とうふうきしゃ'),
    ('山添村立奈良県立山辺高等学校山添分校', 'やまべこうとうがっこうやまぞえぶんこう'),
    ('飯山愛宕中継局', 'いいやまあたご'),
    ('石包丁・石庖丁', 'いしぼうちょう'),
    ('覚醒具・打出の大槌', 'うちでのおおづち'),
    ('緒方三社川越し祭り', 'かわごしまつり'),
    ('無限責任広部銀行', 'ひろべぎんこう'),
    ('弁辺駅', 'べんべ'),
    ('福岡市立愛宕小学校', 'あたごしょうがっこう'),
])
def test_no_pair(kanji, yomi):
    assert yomi not in d or kanji not in d.get(yomi)

# はいっていてはいけないもの


@pytest.mark.parametrize("yomi", [
    ('いずれもろっくふぃるだむ'),
    ('のちの'),
    ('あーけーどすてぃっく'),
    ('ぐらびああいどる'),
    ('いわゆる'),
    ('ぼーこーどあるいはぼどーこーど'),
    ('さんばーすと'),
    ('いいか'),
    ('てれび'),
])
def test_not_in(yomi):
    assert yomi not in d

# あがる /△△通○○上ル/
# いえす /YES/YES!!!/YES, NO./Yes/
# いみ /忌み、斎み/
# いろは /iroha/優勝内国産馬連合競走/
# いわたみつおのちょうらじ /Voice of A&G Digital 岩田光央の超ラジ!/
# うちゅうけいじたましい /宇宙刑事魂 THE SPACE SHERIFF SPIRITS/
# うづ /精衛海を填
