# from operator import itemgetter

if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])
    # sorted(student_list, key=itemgetter(0))
    # student_list.sort(key=itemgetter(1))
    # print("student_list: ", student_list)
    # print(min(student_list, key=itemgetter(1)))
    second_highest = sorted(list(set([score for name, score in student_list])))[1]
    print('\n'.join([a for a, b in sorted(student_list) if b == second_highest]))