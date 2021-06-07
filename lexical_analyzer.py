import string

sentence = 'lehren essen lampe'
input_string = sentence.lower() + '#'

alphabet_list = list(string.ascii_lowercase)
state_list = ['q0','q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29']

transition_table = {}
for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state, alphabet)] ='error'
    transition_table[(state, alphabet)] ='error'
    transition_table[(state, '#')] = 'error'
    transition_table[(state, ' ')] = 'error'

transition_table['q0', ' '] = 'q0'

transition_table['q0', 'l'] = 'q4'
transition_table['q4', 'e'] = 'q7'
transition_table['q7', 'h'] = 'q8'
transition_table['q8', 'r'] = 'q18'
transition_table['q18', 'e'] = 'q19'
transition_table['q19', 'n'] = 'q7'
transition_table['q7', ' '] = 'q29'
transition_table['q7', '#'] = 'accept'
transition_table['q29', ' '] = 'q29'
transition_table['q29', '#'] = 'accept'

transition_table['q29', 's'] = 'q22'
transition_table['q29', 'e'] = 'q20'
transition_table['q29', 't'] = 'q11'
transition_table['q29', 'l'] = 'q4'
transition_table['q29', 'v'] = 'q1'

transition_table['q0', 's'] = 'q22'
transition_table['q22', 'c'] = 'q27'
transition_table['q27', 'h'] = 'q28'
transition_table['q28', 'u'] = 'q14'
transition_table['q14', 'l'] = 'q9'
transition_table['q9', 'e'] = 'q10'
transition_table['q10', 'r'] = 'q7'

transition_table['q0', 't'] = 'q11'
transition_table['q11', 'i'] = 'q12'
transition_table['q12', 's'] = 'q13'
transition_table['q13', 'c'] = 'q14'
transition_table['q14', 'h'] = 'q7'

transition_table['q0', 's'] = 'q22'
transition_table['q22', 't'] = 'q24'
transition_table['q24', 'u'] = 'q25'
transition_table['q25', 'h'] = 'q26'
transition_table['q25', 'l'] = 'q7'

transition_table['q0', 's'] = 'q22'
transition_table['q22', 'c'] = 'q27'
transition_table['q27', 'h'] = 'q28'
transition_table['q28', 'u'] = 'q14'
transition_table['q14', 'h'] = 'q7'

transition_table['q0', 'l'] = 'q4'
transition_table['q4', 'a'] = 'q5'
transition_table['q5', 'm'] = 'q6'
transition_table['q6', 'p'] = 'q3'
transition_table['q3', 'e'] = 'q7'

transition_table['q0', 'v'] = 'q1'
transition_table['q1', 'a'] = 'q2'
transition_table['q2', 's'] = 'q3'
transition_table['q3', 'e'] = 'q7'

transition_table['q0', 'e'] = 'q20'
transition_table['q20', 's'] = 'q21'
transition_table['q21', 's'] = 'q18'
transition_table['q18', 'e'] = 'q19'
transition_table['q19', 'n'] = 'q7'

transition_table['q0', 't'] = 'q11'
transition_table['q11', 'r'] = 'q15'
transition_table['q15', 'i'] = 'q16'
transition_table['q16', 'n'] = 'q17'
transition_table['q17', 'k'] = 'q18'
transition_table['q18', 'e'] = 'q19'
transition_table['q19', 'n'] = 'q7'

transition_table['q0', 's'] = 'q22'
transition_table['q22', 'e'] = 'q23'
transition_table['q23', 'h'] = 'q18'
transition_table['q18', 'e'] = 'q19'
transition_table['q19', 'n'] = 'q7'



idx_char = 0
state = 'q0'
currrent_token = ''
while state!='accept':
    currrent_char = input_string[idx_char]
    currrent_token += currrent_char
    state = transition_table[(state, currrent_char)]
    if state == 'q29':
        print('current token : ', currrent_token, ' valid')
        currrent_token = ''
    if state == 'error':
        print('error')
        break;
    idx_char = idx_char + 1

if state == 'accept':
    print('semua token dinput :', sentence, ' valid')



    
