class Money:
    def __init__(self, denomination, amount=0):
        self._denomination = denomination
        self._amount = amount

    def get_denomination(self):
        return self._denomination

    def set_amount(self, amount):
        if amount >= 0:
            self._amount = amount

    def get_amount(self):
        return self._amount

    def add(self, amount):
        self._amount += amount

    def remove(self, amount):
        if amount <= self._amount:
            self._amount -= amount


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def set_next(self, node):
        self._next = node

    def get_next(self):
        return self._next


class LinkedList:
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def insert(self, node):
        if self._length == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.set_next(node)
            self._tail = node

        self._length += 1

    def get_head(self):
        return self._head


class Distribution:
    def __init__(self):
        self._distribution = LinkedList()

        for denomination in [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]:
            coin = Money(denomination)
            node = Node(coin)

            self._distribution.insert(node)

    def get_user_input(self):
        node = self._distribution.get_head()

        while node is not None:
            coin = node.get_value()

            amount = int(input("HOW MANY {}: ".format(coin.get_denomination())))
            coin.set_amount(amount)

            node = node.get_next()

    def display(self):
        node = self._distribution.get_head()

        while node is not None:
            coin = node.get_value()

            print("{} : {}".format(coin.get_denomination(), coin.get_amount()))

            node = node.get_next()

    def get_sum(self):
        _sum = 0

        node = self._distribution.get_head()

        while node is not None:
            coin = node.get_value()

            _sum += coin.get_amount() * coin.get_denomination()

            node = node.get_next()

        return _sum

    def get_denomination(self, denomination):
        node = self._distribution.get_head()

        while node is not None:
            coin = node.get_value()

            if coin.get_denomination() == denomination:
                return coin

            node = node.get_next()

    def transfer(self, distribution, denomination, amount=None):
        coin_one = self.get_denomination(denomination)
        coin_two = distribution.get_denomination(denomination)

        if amount is None:
            amount = coin_one.get_amount()

        coin_one.remove(amount)
        coin_two.add(amount)

    def distribute(self, distribution, target):
        node = self._distribution.get_head()

        while True:
            if (node is None) or (distribution.get_sum() == target):
                break
            elif node.get_value().get_denomination() == 5:
                node = node.get_next()
            elif distribution.get_sum() > target:
                distribution.transfer(self, node.get_value().get_denomination(), 1)
                node = node.get_next()
            elif node.get_value().get_amount() == 0:
                node = node.get_next()
            else:
                self.transfer(distribution, node.get_value().get_denomination(), 1)


# Get stock information
books = int(input("Books"))
jackpot_sheets = int(input("Jackpot sheets: "))
dabbers = int(input("Dabbers"))

# Calculate earnings
gross_earnings = (books * 7) + (jackpot_sheets * 3)

skycity_takings = gross_earnings * 0.3
variety_takings = gross_earnings * 0.7 + (dabbers * 3)

expected_float = skycity_takings + variety_takings + 500

# Display earnings
print("=====CALCULATIONS=====")
print("Skycity takings: {}".format(skycity_takings))
print("Variety takings: {}".format(variety_takings))
print("Expected float: {}".format(expected_float))

# Get float distribution
float_distribution = Distribution()
print("=====USER INPUT=====")
float_distribution.get_user_input()
float_distribution.display()

# Calculate short
float_sum = float_distribution.get_sum()
float_difference = float_sum - expected_float

variety_takings += float_difference

print("DIFFERENCE BETWEEN EXPECTED ({}) and actual ({}) : {}".format(expected_float, float_sum, float_difference))

# Distribute skycity takings
skycity = Distribution()
float_distribution.distribute(skycity, skycity_takings)
print("======SKYCITY======")
skycity.display()
print("Target: {}, Actual: {}".format(skycity_takings, skycity.get_sum()))

# Distribute variety takings
variety = Distribution()
float_distribution.transfer(variety, 0.5)
float_distribution.transfer(variety, 0.2)
float_distribution.transfer(variety, 0.1)
float_distribution.distribute(variety, variety_takings)
print("======VARIETY======")
variety.display()
print("Target: {}, Actual: {}".format(variety_takings, variety.get_sum()))

# Check float balances
print("======FLOAT======")
float_distribution.display()
print(float_distribution.get_sum())
print("Target: 500.0, Actual: {}".format(float_distribution.get_sum()))
