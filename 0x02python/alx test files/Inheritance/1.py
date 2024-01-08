class MyList(list):
    def print_sorted(self):
        list = self[:]
        list.sort()
        print(list)
        