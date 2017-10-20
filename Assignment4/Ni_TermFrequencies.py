import string

__author__ = 'cni12345'


# main() function:
# 1) Calls create_voc_dictionary to create a dictionary with UAT vocabulary terms.
#    create_voc_dictionary will return the dictionary and it is assigned to the variable, voc_frequencies
# 2) Calls count_voc_term_frequencies with the newly created vocabulary dictionary as an input argument.
#    After this call, the voc_frequencies will contain the updated vocabulary frequencies, and the
#    returned value, term_frequencies, is a dictionary that contains the term frequencies
# 3) Calls display_results with the 2 dictionaries as input arguments to display the results
# Do not change the main() method.
def main():
    voc_frequencies = create_voc_dictionary()
    term_frequencies = count_voc_term_frequencies(voc_frequencies)
    all_voc = count_all_term_frequencies()
    display_results(term_frequencies, all_voc)


# This function creates a vocabulary dictionary from the uat_voc.txt file,
# and returns the dictionary to the main() function.
# This dictionary will be updated by the count_voc_term_frequencies function
# to contain the frequency of vocabulary terms found in the article.
def create_voc_dictionary():
    try:
        voc_file = open('uat_voc.txt', 'r')

        # Read lines from uat_voc.txt and place each term into dictionary called vocab, replace '\n' char with ''
        vocab = dict([(i.replace('\n', ''), 0) for i in voc_file.readlines()])
        return vocab

    except OSError:
        print('Unable to read uat_voc.txt file')
    except Exception as error:
        print(error)


# This function reads the HowBigDataIsChangingAstronomy.txt file.
# It creates a dictionary that contains the frequencies of each term in the file.
# It also updates the vocabulary dictionary passed as an input parameter.
# It returns the dictionary with term frequencies to the main() function.
def count_voc_term_frequencies(voc):
    try:
        input_file = open('HowBigDataIsChangingAstronomy.txt', 'r')
        all_terms = []
        terms = []
        # Read the text file and saved normalized terms in array all_terms
        for i in input_file.readlines():
            all_terms.extend(remove_punctuation(i))

        for i in all_terms:
            for j in i.split(' '):
                terms.append(j.replace('\n', ''))

        dictionary = voc

        # If i is in terms (from uat_voc that are used in HowBigData...) then count the number of times it occurs in txt
        for i in dictionary.keys():
            if i in terms:
                dictionary[i] = all_terms.count(i)
        return dictionary

    except OSError:
        print('Unable to read HowBigDataIsChangingAstronomy.txt file')
    except Exception as error:
        print(error)

def count_all_term_frequencies():
    try:
        input_file = open('HowBigDataIsChangingAstronomy.txt', 'r')
        all_terms = []
        terms = []

        # Read the text file and saved normalized terms in array all_terms
        for i in input_file.readlines():
            all_terms.extend(remove_punctuation(i))

        for i in all_terms:
            for j in i.split(' '):
                terms.append(j.replace('\n', ''))

        dictionary = dict([(i, 0) for i in terms if len(i) > 0])

        # If i is in terms and is not a whitespace, count number of occurrences for each term in the HowBigData... txt
        for i in dictionary.keys():
            if i in terms and len(i) > 0:
                dictionary[i] = terms.count(i)

        return dictionary

    except OSError:
        print('Unable to read HowBigDataIsChangingAstronomy.txt file')
    except Exception as error:
        print(error)


# Same as assignment 3
def remove_punctuation(text):
    clean_words = []  # create an empty list
    text = text.rstrip()  # remove trailing whitespace characters
    words = text.split()  # create a list of words from the text
    for word in words:  # normalize and add to list
        clean_words.append(word.strip(string.punctuation).lower())
    return clean_words


# Sort the 2 dictionaries, and display the top 10 results of each
def display_results(term, voc):
    print('All Terms Frequencies\t\t\tVocabulary Term Frequencies')
    # Sort the terms and it's value from most frequent to least frequent
    term = [(v, k) for (k, v) in term.items()]
    term.sort()
    term.reverse()
    term = [(k, v) for (v, k) in term]
    voc = [(v, k) for (k, v) in voc.items()]
    voc.sort()
    voc.reverse()
    voc = [(k, v) for (v, k) in voc]

    # Prints the 10 most frequently used words from uat_voc that were in HowBigData...txt and 10 most frequently used
    # in HowBigData...txt
    for (i, j) in zip(term[0:10], voc[0:10]):
        print('{:5s} occurs {:3d} times\t\t\t{:5s} occurs {:3d} times'.format(j[0], j[1], i[0], i[1]))

main()
