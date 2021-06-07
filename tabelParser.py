sentence = 'guru melihat lampu'
tokens = sentence.lower().split()
tokens.append('EOS')

non_terminals = ['S', 'NN', 'VB']
terminals = ['lehrer', 'schuler', 'tisch', 'stuhl', 'schuh', 'lampe', 'vase', 'essen', 'trinken', 'sehen']

parse_table = {}

parse_table[('S', 'lehrer')] = ['NN', 'VB', 'NN']
parse_table[('S', 'schuler')] = ['NN', 'VB', 'NN']
parse_table[('S', 'tisch')] = ['NN', 'VB', 'NN']
parse_table[('S', 'stuhl')] = ['NN', 'VB', 'NN']
parse_table[('S', 'schuh')] = ['NN', 'VB', 'NN']
parse_table[('S', 'lampe')] = ['NN', 'VB', 'NN']
parse_table[('S', 'vase')] = ['NN', 'VB', 'NN']
parse_table[('S', 'essen')] = ['error']
parse_table[('S', 'trinken')] = ['error']
parse_table[('S', 'sehen')] = ['error']
parse_table[('S', 'EOS')] = ['error']

parse_table[('NN', 'lehrer')] = ['lehrer']
parse_table[('NN', 'schuler')] = ['schuler']
parse_table[('NN', 'tisch')] = ['tisch']
parse_table[('NN', 'stuhl')] = ['stuhl']
parse_table[('NN', 'schuh')] = ['schuh']
parse_table[('NN', 'lampe')] = ['lampe']
parse_table[('NN', 'vase')] = ['vase']
parse_table[('NN', 'essen')] = ['error']
parse_table[('NN', 'trinken')] = ['error']
parse_table[('NN', 'sehen')] = ['error']
parse_table[('NN', 'EOS')] = ['error']

parse_table[('VB', 'lehrer')] = ['error']
parse_table[('VB', 'schuler')] = ['error']
parse_table[('VB', 'tisch')] = ['error']
parse_table[('VB', 'stuhl')] = ['error']
parse_table[('VB', 'schuh')] = ['error']
parse_table[('VB', 'lampe')] = ['error']
parse_table[('VB', 'vase')] = ['error']
parse_table[('VB', 'essen')] = ['essen']
parse_table[('VB', 'trinken')] = ['trinken']
parse_table[('VB', 'sehen')] = ['sehen']
parse_table[('VB', 'EOS')] = ['error']

stack = []
stack.append('#')
stack.append('S')

idx_token = 0
symbol = tokens[idx_token]

while (len(stack) > 0):
    top = stack[len(stack)-1]
    print('top = ', top)
    print('symbol = ', symbol)
    if top in terminals:
        print('top adalah simbol teminal')
        if top==symbol:
            stack.pop()
            idx_token = idx_token + 1
            symbol = tokens[idx_token]
            if symbol == 'EOS':
                print('isi stack = ', stack)
                stack.pop()
        else:
            print('error')
            break;
    elif top in non_terminals:
        print('top adalah non-terminal')
        if parse_table[(top, symbol)][0] != 'error':
            stack.pop()
            symbol_to_be_pushed = parse_table[(top, symbol)]
            for i in range(len(symbol_to_be_pushed)-1,-1,-1):
                stack.append(symbol_to_be_pushed[i])
        else:
            print('error')
            break;
    else:
        print('error')
        break;
    print('isi stack', stack)