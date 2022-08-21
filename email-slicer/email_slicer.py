emails = input().split()
for email in emails:
    name = email.split("@")[0]
    print(f'Hey, {name.capitalize()}. Welcome on board!')