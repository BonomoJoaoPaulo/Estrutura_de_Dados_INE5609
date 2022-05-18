from HashTable import HashTable

hash_size = int(input())
command = None

T = HashTable(hash_size)

while command != -1:
    command = int(input())
    if command == 0:
        string_submitted = input()
        T.insert(string_submitted)
    elif command == 1:
        string_submitted = input()
        T.pop(string_submitted)

for i in T.table:
    print(i)
