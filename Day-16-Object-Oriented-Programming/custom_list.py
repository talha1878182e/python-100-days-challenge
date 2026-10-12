class Mylist(list):
    def __add__(self, other):
        if len(self) != len(other):
            return "bu elemanlar toplanamaz"
        else:
            result = Mylist()
            for i in range(len(self)):
                result.append(self[i]+other[i])
        return result

list1 = Mylist([1,2,3,4,5])
list2 = Mylist([6,7,8,9,10])

print(list1+list2)
