import sys

input = sys.stdin.readline

def solve(contacts):
    contacts.sort()
    st = contacts[0]
    for contact in contacts[1:]:
        if st in contact:
            return "NO"
        else:
            st = contact
    return "YES"

for i in range(int(input())):
    n = int(input())
    contacts = []

    for j in range(n):
        contacts.append(input().rstrip())

    ans = solve(contacts)
    print(ans)