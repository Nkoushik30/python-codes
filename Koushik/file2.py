import csv
data = [
    ['s.no', 'name', 'rollno', 'section'],
    [1, 'koushik', 23, 'C'],
    [2, 'vivek', 24, 'C']
]
with open('table.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
