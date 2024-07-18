import configparser

config = configparser.ConfigParser()
config.read('app.config')

MIN_QUALITY = int(config['quality_limits']['min_quality'])
MAX_QUALITY = int(config['quality_limits']['max_quality'])


class UpdateStrategy:
    def update(self, item):
        raise NotImplementedError("Subclasses must implement update method")


class NormalItemStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality > MIN_QUALITY:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > MIN_QUALITY:
            item.quality -= 1


class AgedBrieStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality < MAX_QUALITY:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < MAX_QUALITY:
            item.quality += 1


class SulfurasStrategy(UpdateStrategy):
    def update(self, item):
        pass  # Sulfuras does not change


class BackstagePassStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality < MAX_QUALITY:
            item.quality += 1
            if item.sell_in < 11 and item.quality < MAX_QUALITY:
                item.quality += 1
            if item.sell_in < 6 and item.quality < MAX_QUALITY:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = MIN_QUALITY


class ConjuredStrategy(UpdateStrategy):
    def update(self, item):
        if item.quality > MIN_QUALITY:
            item.quality -= 2
            if item.quality < MIN_QUALITY:
                item.quality = MIN_QUALITY
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > MIN_QUALITY:
            item.quality -= 2
            if item.quality < MIN_QUALITY:
                item.quality = MIN_QUALITY
