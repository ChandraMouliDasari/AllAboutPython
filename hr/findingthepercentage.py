n = int(input())
students_score = {}
for _ in range(n):
    name,*score = input().split()
    scores = list(map(float,score))
    students_score[name]=scores
    
query_name=input()
name=students_score[query_name]
total = sum(name)/3
final = "{:.2f}".format(total)
print(final)

