if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #print(student_marks)
    l1 = (student_marks[query_name])
    print("{:.2f}".format(sum(l1)/len(l1)))

