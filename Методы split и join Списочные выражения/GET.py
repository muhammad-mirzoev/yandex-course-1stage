url = input().strip()
key = input().strip()

query_string = url.split('?')[1]

pairs = query_string.split('&')

for pair in pairs:
    k, v = pair.split('=')
    if k == key:
        print(v)
        break
