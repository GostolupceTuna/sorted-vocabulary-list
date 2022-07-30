import os.path, pathlib

global current_path
current_path = pathlib.Path(__file__).parent.resolve()

class word_type():

    def __init__(self, name='None'):
        self.name = name
        self.dir = str(current_path) + '\\vocab lists\\' + self.name
        self.create_directories()
        return

    def __repr__(self):
        return self.name

    def create_directories(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
            for i in range(1,4):
                open('{dir}\\{name}_{list_no}.txt'.format(dir=self.dir, name=self.name, list_no=i), 'w')

    def add_vocab(self, vocab, list_no):
        target_file_dir = '{dir}\\{name}_{list_no}.txt'.format(dir=self.dir,
                                                               name=self.name,
                                                               list_no=list_no)

        # count resets in every 15 lines
        line_count = len(open(target_file_dir, 'r').read().split('\n')) % 15
        text_file = open(target_file_dir, 'a+')
        text_file.write(str(vocab)+ '\n')
        if line_count == 0:
            text_file.write('\n')

    def term_repetition(self, term):
        # iterate through every .txt file
        for i in range(1,4):
            text_file = open('{dir}\\{name}_{list_no}.txt'.format(dir=self.dir, name=self.name, list_no=i), 'r')
            for vocab_pair in text_file.read().split('\n'):
                if term.lower() == vocab_pair.split('    ')[0].lower():
                    return True, vocab_pair

        return False, None

nouns = word_type('Nouns')
verbs = word_type('Verbs')
adjectives = word_type('Adjectives')
adverbs = word_type('Adverbs')
phrases = word_type('Phrases')
others = word_type('Others')

type_dict = {'1': nouns, '2': verbs, '3': adjectives, '4': adverbs, '5': phrases, '6': others}

while True:

    print('\n', type_dict)
    try:
        selected_class = type_dict[input('Pick one: ')]
    except:
        continue

    print('Selected class: ', selected_class)
    term = input('\nEnter a term: ')
    definition = input('\nEnter the definition for the term: ')
    list_no = input('\nEnter list number: ')
    vocab = term + '    ' + definition
    print('\nTerm: {term}, Definition: {defi}, List Number: {list_no}'.format(term=term,
                                                                           defi=definition,
                                                                           list_no=list_no))

    repetition, repeated_vocab_pair = selected_class.term_repetition(term)
    if repetition:
        print('\nTerm repetition! '.upper(), ' -- Repeated vocab pair: ', repeated_vocab_pair)

    if input('\nSave? (y or n) ') == 'y':
        selected_class.add_vocab(vocab, list_no)
    else:
        continue
