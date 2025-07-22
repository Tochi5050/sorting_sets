def merge_sort(nums): #[1,5,3,2,8,7,6,4]
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)

    left_list = merge_sort(nums[0:pivot]) #
    right_list = merge_sort(nums[pivot:]) # [8, 7, 6, 4]
    return merge(left_list, right_list) #[1, 2, 3, 5]


def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []

    print(left_list, "left_list")
    print(right_list,"right_list")
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1

    # append what is remained in either of the lists

    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])

    return ret

print(merge_sort([1,5,3,2,8,7,6,4])) #Topdown solution