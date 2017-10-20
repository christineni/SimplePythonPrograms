import string

__author__ = 'cni12345'

# Global variables
lines = 0
word_count = 0
length = 0
stopwords = 0
key_density = 0


def main():
    global lines, file, word_count, length, stopwords, key_density

    # Try opening text file, if file does not exist then exception is thrown
    try:
        file = open('LearnToCode_LearnToThink.txt', 'r+')
    except IOError:
        print("Cannot open file")

    # Store the contents of the file in variable content
    content = file.readlines()

    # Loop through the content line by line
    for line in content:
        txt = remove_punctuation(line)
        # Count the number of lines in the file
        lines += 1
        # Count the number of words in the file
        word_count += len(txt)
        # Loop through the file word by word
        for word in line:
            # If the word is a stopword, increase stopword count by 1
            if word in create_stopword_list():
                stopwords += 1
            # Count the number of characters in the file
            for _ in word:
                length += 1

    # Calculates the percentage of words in the file that are not stopwords
    key_density = ((word_count - stopwords) / word_count) * 100

    # Print results to console
    print("Total lines: ", lines)
    print("Total length: ", length)
    print("Total stopword count: ", stopwords)
    print("Total word count: ", word_count)
    print("Keyword density: ", format(key_density, ',.2f'))

    # Write the results to a file
    write_results_to_file(str(lines))
    write_results_to_file(str(length))
    write_results_to_file(str(stopwords))
    write_results_to_file(str(word_count))
    write_results_to_file(str(key_density))


# Function that returns a text file containing a list of stopwords
def create_stopword_list():
    stopwords_list = open('stopwords.txt', 'r')
    stop = stopwords_list.readline()
    stopwords_list.close()
    return stop


# Function to normalize text by removing punctuation and convert to lowercase
def remove_punctuation(text):
    clean_words = []

    text = text.rstrip()

    words = text.split()
    for word in words:
        clean_words.append(word.strip(string.punctuation).lower())
    return clean_words


# Function to write results to a file
def write_results_to_file(t):
    file.write(t)


# Call the main function
main()
