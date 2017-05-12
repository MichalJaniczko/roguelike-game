
def print_table(inventory, order=None):
    """
    Function print dict given in parametr "invnetory"
    with specyfic order given in parametr "order" by int values of each key.
    If no argument given order is randmo, for "count,desc" is from the biggest to the smallest values,
    for "count,asc" form the smallest to the biggest. Everything is printed in formated table with right-just
    values and keys.
    """
    if not order:       # no argumen given, random roder
        sort_inv = list(inventory.items())      # keys-values change to list of tuplets for imtu to print part
    # argument for desecending order given, temporary function using index = 1 element of tuplets as key for sorting
    elif order.lower() == "count,desc":
        sort_inv = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    # argument for ascending order given, temporary function using index = 1 element of tuplets as key for sorting
    elif order.lower() == "count,asc":
        sort_inv = sorted(inventory.items(), key=lambda x: x[1])
    # if player give wrong argument table will print as unordered with communicat
    else:
        print("Wrong order given. You simply don't know how order your inventory")
        sort_inv = list(inventory.items())

    # part where we check what is longer (column name or printed output (int - dictionay values)
    # and use correct len as column width)
    # int are converted here to strings to we can get len of the longest of it (first sorted)
    list_of_counts = [str(sorted(inventory.values())[value_index]) for value_index in range(len(inventory.values()))]
    len_longest_counts = len(list_of_counts[-1])
    if len_longest_counts < len("count"):
        width_count = len("count")
    else:
        width_count = len_longest_counts

    # part where we check what is longer (column name or printed output (string - dictionary keys)
    # and use correct len as column width)
    len_longest_item_name = len(sorted(inventory.keys(), key=len)[-1])
    if len_longest_item_name < len("item name"):
        width_item = len("item name")
    else:
        width_item = len(sorted(inventory, key=len)[-1])

    # print part of function, + 2 and + 4 added to used width
    # to ensure space between left edge of terminal (+2) and between columns (+4)
    # total number of items (sum of dict values) is mede here also
    total_item_count = 0
    print("Inventory:")
    print("{0:{fill}>{width_count}}{1:{fill}>{width_item}}".format("count", "item name", fill=" ",
          width_count=width_count+2, width_item=width_item+4))
    print("-"*(6 + width_count + width_item))
    for item in range(len(sort_inv)):
        total_item_count += sort_inv[item][1]
        print("{0:{fill}>{width_count}}{1:{fill}>{width_item}}".format(sort_inv[item][1], sort_inv[item][0],
              fill=" ", width_count=width_count+2, width_item=width_item+4))
    print("-"*(6 + width_count + width_item))
    print("Total number of items: ", total_item_count)


def add_to_inventory(inventory, item):
    if item in inventory.keys():
        inventory[item] += 1
    else:
        added_item = 1
        inventory.setdefault(item, added_item)
    return inventory