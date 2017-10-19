"""
Merge two sorted arrays and return it as a new array.
# NOTE: YOU CAN NOT USE ANY SORTING LIBRARIES
"""


def merge_two_list_helper(list1, list2):
    # YOUR CODE GOES HERE
    list3=[]
    while len(list1)>0 and len(list2)>0:

        if list1[0]>list2[0]:
    #            list3.append(list2[0])
            a=list2.pop(0)
        else:
    #            list3.append(list1[0])
            a=list1.pop(0)
            
        list3.append(a)
    if len(list1)>0:
        list3=list3+list1
    else:
        list3=list3+list2         

    return list3
    


# DO NOT CHANGE THIS FUNCTION
def merge_two_list(list1, list2):
	return merge_two_list_helper(list1, list2)


# test cases
def main():
    list1 = [1,3,5]
    list2 = [2,4,6]
    print("merging [1,3,5] and [2,4,6]......")
    print("expected result is [1,2,3,4,5,6]")
    print("your output is {}".format(merge_two_list(list1, list2)))


if __name__ == "__main__":
    main()
