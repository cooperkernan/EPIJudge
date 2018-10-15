from test_framework import generic_test


def stable_sort_list(L):
    # TODO - you fill in here.
#    list1 = [int(x) for x in L]
#    print(list1)
    return(sorted(L, key=int))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
