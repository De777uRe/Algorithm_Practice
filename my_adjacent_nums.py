# Given a number n, print all the numbers up to n that ONLY contain adjacent digits that differ by one exactly
# e.g. 12, 32, 23, 545, 565, 898

def adjacent_nums(n):
    output_list = []
    valid_nums = {1: [i for i in range(10)]}

    for num in range(n+1):
        if num in valid_nums[1]:
            output_list.append(num)
        else:
            num_copy = num
            num_copy_string = str(num_copy)
            is_valid = True
            while len(str(num_copy)) > max(valid_nums.keys()):
                if abs(int(num_copy_string[-1]) - int(num_copy_string[-2])) == 1:
                    num_copy //= 10
                    num_copy_string = str(num_copy)
                else:
                    is_valid = False
                    break
            if num_copy in [number for sublist in valid_nums.values() for number in sublist]:
                output_list.append(num)

    return output_list


if __name__ == "__main__":
    print(adjacent_nums(10000))

