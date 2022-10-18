nested_list = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None],
        ]

class FlatIterator:
    def __init__(self, n_l):
        self.my_list = n_l

    def __iter__(self):
        self.cursor = 0
        self.nest_cursor = -1
        self.full_list = []
        return self

    def __next__(self):
        self.nest_cursor += 1
        if len(self.my_list[self.cursor]) == self.nest_cursor:
            self.cursor += 1
            self.nest_cursor = 0
        if self.cursor == len(self.my_list):
            raise StopIteration
        self.full_list = self.my_list[self.cursor][self.nest_cursor]
        return self.full_list

def flat_generator(my_list):
    for my_list_o in my_list:
        for my_list_t in my_list_o:
            yield my_list_t

if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [items for items in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)