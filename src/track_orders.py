from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))

    # Prato favorito por cliente;
    def get_most_ordered_dish_per_customer(self, customer):
        find_customer_favorite_food = []
        for order in self.orders:
            if (order[0] == customer):
                find_customer_favorite_food.append(order[1])
        customer_food_counter = Counter(find_customer_favorite_food)
        return customer_food_counter.most_common(1)[0][0]

    # Pratos nunca pedidos por cada cliente;
    def get_never_ordered_per_customer(self, customer):
        menu = set()
        for order in self.orders:
            menu.add(order[1])

        customer_order = set()
        for order in self.orders:
            if (order[0] == customer):
                customer_order.add(order[1])
        return menu.difference(customer_order)

    # Dias nunca visitados por cada cliente;
    def get_days_never_visited_per_customer(self, customer):
        days = set()
        for order in self.orders:
            days.add(order[2])

        customer_days = set()
        for order in self.orders:
            if (order[0] == customer):
                customer_days.add(order[2])
        return days.difference(customer_days)

    # Dia mais movimentado;
    def get_busiest_day(self):
        day_counter = Counter(self.orders)
        return day_counter.most_common(1)[0][0][2]

    # Dia menos movimentado;
    def get_least_busy_day(self):
        day_counter = Counter(self.orders)
        return day_counter.most_common()[-1][0][2]
