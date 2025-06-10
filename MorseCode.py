class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), 
         ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
         ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
         ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
         ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..')]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

def make_morse_tree():
    root = TNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root
        for c in code:
            if c == '.':
                if node.left is None:
                    node.left = TNode(None, None, None)
                node = node.left
            elif c == '-':
                if node.right is None:
                    node.right = TNode(None, None, None)
                node = node.right
        node.data = tp[0]
    return root

def decode(root, code):
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
        if node is None:
            return None
    return node.data

morseCodeTree = make_morse_tree()
input_str = input("Input: ").upper()

mlist = []
for ch in input_str:
    if ch.isalpha():
        code = encode(ch)
        mlist.append(code)

print("Morse Code: ", mlist)

print("Decoding: ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()

