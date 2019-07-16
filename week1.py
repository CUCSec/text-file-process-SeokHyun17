num=0
with open('log_files/201811113023.log', encoding='utf8') as f:
    for line in f:
        stu_id = line.split(', ')[1]
        a = stu_id.split('：')[1]
        if a == '201811113023':
            num = num+1
print(num)