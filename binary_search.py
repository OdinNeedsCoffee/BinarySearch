def binarySearch(a_list, item_in_list):
    if item_in_list not in a_list:
        print("Value not in the list")
    else:
        count = 0
        if len(a_list) <= 1:
            return a_list
        else:
            a_list.sort()
            first_entry = 0
            last_entry = len(a_list) - 1

            while first_entry <= last_entry:
                mid_point = (first_entry + last_entry) // 2  # damit mid_point kein float ist
                if a_list[mid_point] == item_in_list:
                    print(f'Needed splits: {count}\nList: {a_list}\nSearched item: {item_in_list}')
                    return True
                else:
                    if a_list[mid_point] > item_in_list:
                        last_entry = mid_point - 1
                        count += 1
                    else:
                        first_entry = mid_point + 1
                        count += 1


a_list = [1, 2, 6, 23, 78, 56, 98, 23]
binarySearch(a_list,23)
