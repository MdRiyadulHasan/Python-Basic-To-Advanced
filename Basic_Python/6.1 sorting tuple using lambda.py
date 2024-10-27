def bestStudents1(markList):
    ans = sorted(markList, key = lambda x : -x[1])
    return ans

def bestStudents(marks):
    ans = sorted(marks, key = lambda mark : mark[0], reverse = True)
    return ans

if __name__ == '__main__':
    students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95), ('John',75)]
    res = bestStudents(students)
    res1 = bestStudents1(students)
    print(res)
    print(res1)