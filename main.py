class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, number, name):
        self.contacts[number] = name

    def delete_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]

    def find_contact(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return "not found"

def process_queries(queries):
    phone_book = PhoneBook()
    result = []
    for query in queries:
        if query[0] == 'add':
            phone_book.add_contact(int(query[1]), query[2])
        elif query[0] == 'del':
            phone_book.delete_contact(int(query[1]))
        elif query[0] == 'find':
            result.append(phone_book.find_contact(int(query[1])))
    return result

if __name__ == '__main__':
    n = int(input())
    queries = [input().split() for i in range(n)]
    result = process_queries(queries)
    print('\n'.join(result))
