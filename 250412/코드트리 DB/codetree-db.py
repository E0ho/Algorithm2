# DB 테이블
# init, insert, delete, rank, sum

# dic = { key : value }


Q = int(input())

db = {}
key_set = set()
value_set = set()

for _ in range(Q):
    inp = list(input().split())

    cmd = inp[0]

    if cmd == "init":
        if db:
            del db
            del key_set
            del value_set
        db = {}
        key_set = set()
        value_set = set()


    elif cmd == "insert":
        key = inp[1]
        value = int(inp[2])

        if (key in key_set) or (value in value_set):
            print(0)
        
        else:
            db[key] = value
            key_set.add(key)
            value_set.add(value)
            print(1)


    elif cmd == "delete":
        key = inp[1]
        if key not in key_set:
            print(0)
        else:
            value = dic[key]
            del dic[key]
            key_set.remove(key)
            value_set.remove(key)
            print(value)

    elif cmd == "rank":
        k = int(inp[1])
        if k > len(db):
            print("None")
        else:
            sort_db = sorted(db.items(), key = lambda x : x[1])
            print(sort_db[k-1][0])

    else:
        sum_val = 0

        k = int(inp[1])

        for ele in db.values():
            if ele <= k:
                sum_val += ele
        print(sum_val)