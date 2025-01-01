shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    menus.sort()

    def binary_search(target, data):
        start = 0
        end = len(data) - 1

        while start <= end:
            mid = (start + end) // 2
            if data[mid] == target:
                return True
            elif data[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    for order in orders:
        if not binary_search(order, menus):
            return False
        return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)