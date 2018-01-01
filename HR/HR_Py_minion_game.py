def minion_game(s):
    vowels = set('AEIOU')

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
            # print("Kevin", kevsc)
        else:
            stusc += (len(s)-i)
            # print("Stuart", stusc)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

minion_game("AEIOU")