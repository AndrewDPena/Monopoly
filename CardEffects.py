class CardEffects(object):
    @staticmethod
    def move_player(player, destination):
        if int(destination) < 0:
            player.current -= int(destination)
        else:
            player.current = int(destination)

    @staticmethod
    def pay_player(player, amount):
        player.account += int(amount)

    @staticmethod
    def add_inventory(player, item):
        player.inventory.add(item)
