import collections

def winner(erica, bob):
    dct = {'S':0, 'E':1, 'M':3, 'H':5}
    erica_score, bob_score = 0, 0

    erica_questions = collections.Counter(erica)
    bob_questions = collections.Counter(bob)

    for i in range(3):
        if erica[i] == 'S':
            erica_score += dct['S']
        elif erica[i] == 'E':
            erica_score += dct['E']
        elif erica[i] == 'M':
            erica_score += dct['M']
        elif erica[i] == 'H':
            erica_score += dct['H']

        if bob[i] == 'S':
            bob_score += dct['S']
        elif bob[i] == 'E':
            bob_score += dct['E']
        elif bob[i] == 'M':
            bob_score += dct['M']
        elif bob[i] == 'H':
            bob_score += dct['H']

    if erica_score > bob_score:
        return 'Erica'
    elif bob_score > erica_score:
        return 'Bob'
    else:
        if erica_questions['H'] > bob_questions['H']:
            return 'Erica'
        elif erica_questions['H'] < bob_questions['H']:
            return 'Bob'
        elif erica_questions['M'] > bob_questions['M']:
            return 'Erica'
        elif erica_questions['M'] < bob_questions['M']:
            return 'Bob'
        elif erica_questions['E'] > bob_questions['E']:
            return 'Erica'
        elif erica_questions['E'] < bob_questions['E']:
            return 'Bob'
        else:
            return 'Tie'

