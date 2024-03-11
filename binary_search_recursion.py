def binary_search_rec(a_list, first, last, an_item, count=0):
    if an_item not in a_list:
        print("Value not in the list")
        return False, 0
    else:
        a_list.sort()
        if len(a_list) == 0:
            return False
        else:
            mid_point = (first + last) // 2
            if a_list[mid_point] == an_item:
                return True, count
            else:
                if an_item < a_list[mid_point]:
                    last = mid_point - 1
                    count += 1
                    return binary_search_rec(a_list, first, last, an_item, count)
                else:
                    first = mid_point + 1
                    count += 1
                    return binary_search_rec(a_list, first, last, an_item, count)


a_list = [1, 2, 6, 23, 78, 56, 98, 23, 79, 102, 4, 90]
found, steps = binary_search_rec(a_list, 0, len(a_list) - 1, 78)
print(f'Needed splits: {steps}\nList: {a_list}')
