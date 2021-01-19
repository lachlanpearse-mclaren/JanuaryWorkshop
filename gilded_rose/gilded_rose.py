class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def increase_quality(self,item):
        item.quality = item.quality + 1
    
    def decrease_quality(self,item):
        item.quality = item.quality - 1
    
    def update_item(self,item):

        item_decreases_in_value = item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert"
        item_has_dynamic_quality = item.name != "Sulfuras, Hand of Ragnaros"

        if item_decreases_in_value:
                if item.quality > 0:
                    if item_has_dynamic_quality:
                        self.decrease_quality(item)
        else:
            if item.quality < 50:
                self.increase_quality(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            self.increase_quality(item)
                    if item.sell_in < 6:
                        if item.quality < 50:
                            self.increase_quality(item)
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item_has_dynamic_quality:
                            self.decrease_quality(item)
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    self.increase_quality(item)
