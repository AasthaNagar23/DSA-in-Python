# Josephus Problem: circle mein people khade hain
# Har baar k-1 people skip honge aur kth person kill hoga.
# Last mein jo person survive karega, uski position print karni hai.

n = int(input())
k = int(input())

count = 0

for i in range(2, n + 1):
    # n ko include karne ke liye n+1
    count = (count + k) % i

# count 0-based position hai,
# isliye actual person number ke liye +1
print(count + 1)