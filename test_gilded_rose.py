import unittest
from gilded_rose import Item, GildedRose

class TestGildedRose(unittest.TestCase):

    def test_normal_item_before_sell_date(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_on_sell_date(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 18)

    def test_normal_item_after_sell_date(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -2)
        self.assertEqual(items[0].quality, 18)

    def test_normal_item_quality_never_negative(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_before_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 21)

    def test_aged_brie_on_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 22)

    def test_aged_brie_after_sell_date(self):
        items = [Item(name="Aged Brie", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -2)
        self.assertEqual(items[0].quality, 22)

    def test_aged_brie_quality_never_exceeds_max(self):
        items = [Item(name="Aged Brie", sell_in=10, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 50)

    def test_backstage_pass_long_before_sell_date(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 21)

    def test_backstage_pass_medium_close_to_sell_date_upper_bound(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_medium_close_to_sell_date_lower_bound(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 5)
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_very_close_to_sell_date_upper_bound(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_very_close_to_sell_date_lower_bound(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_on_sell_date(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)

    def test_backstage_pass_after_sell_date(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -2)
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_before_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 18)

    def test_conjured_item_on_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 16)

    def test_conjured_item_after_sell_date(self):
        items = [Item(name="Conjured Mana Cake", sell_in=-1, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -2)
        self.assertEqual(items[0].quality, 16)

    def test_conjured_item_quality_never_negative(self):
        items = [Item(name="Conjured Mana Cake", sell_in=10, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 0)

if __name__ == '__main__':
    unittest.main()
