# -*- coding: utf-8 -*-
from strategy_manager import AgedBrieStrategy, SulfurasStrategy, BackstagePassStrategy, ConjuredStrategy, NormalItemStrategy


class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassStrategy(),
            "Conjured Mana Cake": ConjuredStrategy()
        }

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, NormalItemStrategy())
            strategy.update(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
