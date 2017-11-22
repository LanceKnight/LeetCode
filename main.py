#406
def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people.sort(key=lambda (h,k): (-h,k))
    print people
    new_list = []
    for person in people:
        new_list.insert(person[1],person)
        print new_list
    return new_list

print reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])