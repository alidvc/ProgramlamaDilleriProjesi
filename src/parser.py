class SyntaxAnalyzer:
    def __init__(self):
        # Basit bir context-free grammar için üretim kuralları
        self.grammar = {
            'S': [('E',)],  # Başlangıç sembolü
            'E': [('T', 'OPERATOR', 'T'), ('IDENTIFIER', '=', 'E'), ('NUMBER',)],
            'T': [('NUMBER',), ('IDENTIFIER',)]
        }
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def shift_reduce_parse(self, tokens):
        stack = []
        i = 0
        while i < len(tokens):
            stack.append(tokens[i])
            # Redüksiyon denemesi
            while len(stack) >= 3:
                if (stack[-3][0] in ['NUMBER', 'IDENTIFIER'] and
                    stack[-2][0] == 'OPERATOR' and
                    stack[-1][0] in ['NUMBER', 'IDENTIFIER']):
                    stack[-3:] = [('E', 'expression')]
                elif (stack[-3][0] == 'IDENTIFIER' and
                      stack[-2][0] == 'OPERATOR' and stack[-2][1] == '=' and
                      stack[-1][0] == 'E'):
                    stack[-3:] = [('E', 'assignment')]
                else:
                    break
            i += 1
        return stack