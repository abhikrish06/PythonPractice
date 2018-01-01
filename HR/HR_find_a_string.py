def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i + len(sub_string)] == sub_string:
            count = count + 1
            #print(count)
    return count

count_substring("ABCDCDC","CDC")