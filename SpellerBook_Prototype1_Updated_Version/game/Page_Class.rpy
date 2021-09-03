init python:
    # import re

    class Page:
        # Function:         Initializes class Page
        # Parameters:       page_number (int), list_of_pages (list of strings where each item in the list is the entire string text of a page)
                            # sentences (empty list), words_to_highlight(empty list)
        # Returns:          no returns
        def __init__(self, page_number, list_of_pages, sentences, words_to_highlight):
            self.page_number = page_number
            self.list_of_pages = list_of_pages
            self.sentences = sentences
            self.words_to_highlight = words_to_highlight


        # Function:         Finds the index of a the nth punctuation mark
        # Parameters:       punctuation (char), nth_pos (int)
        # Returns:          the index of the nth punctuation mark
        def find_nth_punctuation(self, punctuation, nth_pos):
            # Variable stores all the text on a page in the form of a string
            whole_text = self.list_of_pages[self.page_number-1]
            # Splits all the text on a page into a list of strings according to the puncutation char and the (nth_pos+1) number of splits
            # ex_string = "Hello World. This is a beautiful world. I love this world."
            # nth_pos = 1
            # splitted_ex_string = ex_string.split (".", nth_pos + 1)
            # Output -----> splitted_ex_string = [ "Hello World", " This is a beautiful world", " I love this world."]

            splitted_text = whole_text.split(punctuation, nth_pos+1)

            # Checks to see whether or not a certain number of splits can be made
            if len(splitted_text) <= nth_pos+1:
                return -1

            # Finds the index position of the punctuation
            else:
                current_index = len(whole_text)-len(splitted_text[-1])-len(punctuation)

                try:
                    # Checks if the end puncutation is within quotations and adjusts its index
                    # position accordingly
                    if whole_text[current_index+1] == '"':
                        updated_index = current_index + 1
                        return updated_index


                except IndexError:
                    pass

                return current_index

            # len(ex_string)-len(splitted_ex_string[-1])-len(".") = 58-19-1 = 38


        # Function:         breaks down the entire string text of a page into individual strings where each string is a sentence and appends it to the
                            # sentence class attribute
        # Parameters:       punctuation_dividers (the list of text dividers)
        # Returns:          no returns
        def get_sentences(self, punctuation_dividers):
            # All the text on a page in the form of a string
            shown_text = self.list_of_pages[self.page_number-1]
            # Empty list that will store the index positions of the punctuations
            order_of_punctuations = []
            # Variable which stores the number of sentences on a page
            total_sentences = 0
            # Loop goes through a specific end punctuation each time, whether it is a '.' '!' or '?' and counts the number of
            # times the end punctuation is found in the string and saves this number to number_of_chars.
            for punctuation_divider in punctuation_dividers:
                number_of_chars = shown_text.count(punctuation_divider)

            # Loop iterates based on the number of times a specific end punctuation occurred in the string (number_of_chars)
            # and attempts to find the index of the (first, second, third, etc...) specific type of end punctuation (let's say '.')
            # in the string. This index is then appended to the list order_of_punctuations.
            # If index is not found the loop skips the appending to list and continues.
                i = 0
                while i < number_of_chars:
                    char_index =  self.find_nth_punctuation(punctuation_divider, i)
                    if char_index == -1:
                        i += 1
                    else:
                        order_of_punctuations.append(char_index)
                        i += 1
                    # Used to check if an end puncutation is repeated at the end of a sentence for emphasis. Ex ( He was... or This is amazing!!!)
                    # and ensures that the it is treated and shown as one sentence by only adding the index of the last end punctuation in the repeated
                    # sequence to the list of order_of_punctuations
                    if len(order_of_punctuations) > 1:

                        current_list_index = len(order_of_punctuations)-1
                        previous_list_index = current_list_index - 1

                        if order_of_punctuations[current_list_index]-1 == order_of_punctuations[previous_list_index]:
                            order_of_punctuations.remove(order_of_punctuations[previous_list_index])


            # Sorts the order_of_punctuations so that the end punctuations with the smaller indices will be first in the list.
            sorted_order_of_punctuations = sorted(order_of_punctuations)
            # Stores the overall number of sentences.
            total_sentences = len(sorted_order_of_punctuations)

            # Initializes the counter that tracks the number of sentences that have been appended to the instance attribute sentences.
            # Initializes the new_index and old_index to zero which will be used to "pick out" sentences from the string that contains
            # all the text on a page.
            n = 0
            new_index = 0
            old_index = 0

            # Loops through and updates the new_index and old_index to "pick out" the sentences from the entire page text all and appends
            # it to the instance attibutes sentences. Does this while ensuring that it is not "picking out" more sentences than there are total number of sentences

            if total_sentences >= 1:

                while n < total_sentences:
                    # Initializes the new_index to the index of the first end punctuation found in the string and
                    # initializes it to the next end punctuation found in the string with each iteration of the loop.
                    new_index = sorted_order_of_punctuations[n]

                    # Appends a "picked out" sentence to the instance attribute sentences
                    self.sentences.append(shown_text[old_index:new_index+1].strip())
                    # This updates the old_index so that the old_index indicates the first char of the next sentence
                    old_index = new_index + 1
                    # This counter keeps track of how many sentences have been appended to the instance attribute
                    n += 1


            # This ensures that if text on a page did not have any end punctuation, it would still be shown.
            elif shown_text != '':
                self.sentences.append(shown_text)

        # Function:         breaks down an entire sentence or string into a list of words
        # Parameters:       sentence (string)
        # Returns:          a list of words

        def get_words_in_sentence(self, sentence):
            translation_table = dict.fromkeys(map(ord, '!.?",'), None)
            sentence = sentence.translate(translation_table)
            return sentence.split()

        # Function:         selects words to highlight based on the type of word we want to highlight based on either its length or a word file and append
                            # it to instance attribute words_to_highlight
        # Parameters:       sentence_number (int), type (string), word_dict (dictionary), word_length(int), plus (boolean), minus (boolean)
        # Returns:          no returns
        def select_words_to_highlight(self, sentence_number, type, word_dict, word_length, plus, minus):

            # If words to highlight is based on a word length then it will loop through words_in_sentence
            # and find words in words_in_sentence that satisfy the specified length  and appends
            # it to the words_to_highlight (instance attribute)

            a_sentence = self.sentences[sentence_number]
            words_in_sentence = self.get_words_in_sentence(a_sentence)

            # used to store words found in a sentence to highlight based on a word file
            found_word = None
            # ensures that the instance attribute words_to_highlight is completely cleared before appending words pertaining to the new sentence
            self.words_to_highlight = []

            if type == "length":

                # If the user specifies to find words that are equal, greater or less than the specified length (Ex words that are 3 letters, longer or shorter)
                # then these words will also be appended to words_to_highlight
                if plus is True:

                    for a_word in words_in_sentence:
                        if len(a_word) >= word_length:
                            self.words_to_highlight.append(a_word)

                elif minus is True:

                    for a_word in words_in_sentence:
                        if len(a_word) <= word_length:
                            self.words_to_highlight.append(a_word)


                # If the user does not select plus or minus then it will just be the default setting which finds words that are of the specified length or 1 letter
                # longer than the specified length
                else:
                    i = 0
                    while i <=1 :
                        for a_word in words_in_sentence:
                            if len(a_word) == (word_length+i):
                                self.words_to_highlight.append(a_word)

                        i+=1

            # If words to highlight is based on a word dictionary then it will first loop through the words_in_sentence
            # and test whether or not a word in words_in_sentence exists in the word dictionary. If it does then the value of the key (word)
            # is updated by adding one in word_dict (dictionary). After updating the word_dict, the word_dict will be looped through to check which
            # keys (words) have a value of 1. If it does then it is found in the sentence and appended to words_to_highlight

            elif type == "word_file":
                for a_word in words_in_sentence:
                    updated_a_word = a_word.lower()
                    if updated_a_word in word_dict:
                        word_dict[updated_a_word] += 1

                for k in word_dict:
                    if word_dict[k] != 0:
                        my_regex = r'\b' + k + r'\b'
                        match = re.search(my_regex, a_sentence, flags = re.ASCII | re.IGNORECASE)
                        if match:
                            start_index = match.start()
                            end_index = match.end()
                            found_word = a_sentence[start_index:end_index]
                            self.words_to_highlight.append(found_word)


        # Function:         Applies the highlight to a specific number of the words in words_to_highlight for a given sentence
        # Parameters:       sentence (string), number_to_highlight(int)
        # Returns:          highlight_dict (dictionary)
        def highlight_words(self, sentence, number_to_highlight):
            # Initializes a variable to store words_to_highlight
            # Initializes a empty list and empty varible
            highlight_words = self.words_to_highlight
            words_changed = []
            word_to_change = None
            # Initializes the keys and then uses these keys to initialize the dictionary
            highlight_attributes = ["words_changed", "sentence"]
            highlight_dict = dict.fromkeys(highlight_attributes, None)

            # If highlight_words is an empty list it will return the dictionary which contains an
            # empty list words_changed and an unhighlighted sentence sentence
            if not highlight_words:
                highlight_dict["sentence"] = sentence
                return highlight_dict

            # If highlight_words is not an empty list
            elif highlight_words:

                # This checks whether or not the number specified to highlight makes sense with the number of words found.
                # (Ex Cannot highlight 4 words if there are only 3 words in found_words)
                if len(highlight_words) >= number_to_highlight:
                    # This sets a counter to keep track of how many words have been highlighted
                    i = 0
                    # This loops through to highlight a specified number of words
                    while i < number_to_highlight:

                        # Picks a random word to highlight
                        word_to_change = renpy.random.choice(highlight_words)

                        # Adds the randomly picked word to a list or words that will be highlighted
                        words_changed.append(word_to_change)

                        # Removes the randomly picked word from the list of eligible words to highlight so that it will not be highlighted again
                        highlight_words.remove(word_to_change)

                        # Applies a the highlight color and underline
                        highlight = "{=highlight}" + word_to_change  + "{/font}"

                        # Ensures that the word to replace with the highlighted word is again not a substring in a string but
                        # a word.
                        adjusted_word_to_change = r'\b' + word_to_change + r'\b'

                        # Replaces the unhighlighted word in the sentence with the highlighted word
                        highlighted_sentence = re.sub(adjusted_word_to_change, highlight, sentence, count =1, flags = re.ASCII | re.IGNORECASE)

                        # Updates the sentence so that the already highlighted words will remain highlighted if user chooses
                        # to highlight more than one word.
                        sentence = highlighted_sentence

                        # Updates the counter used to count the number of words that have been applied the highlight
                        i+=1

                    # Sets newly obtained values to the keys in the dictionary
                    highlight_dict["words_changed"] = words_changed
                    highlight_dict["sentence"] = sentence

                    return highlight_dict

                # If number specified to highlight does not make sense with the number of words found
                # return the dictionary which contains an empty list words_changed and an unhighlighted sentence sentence
                elif len(highlight_words) < number_to_highlight:
                    highlight_dict["sentence"] = sentence
                    return highlight_dict



        # Function:         Calls upon highlight_words method and then displays updated sentence to game screen.
                            # The it returns a dictionary containing attributes of the sentence just displayed
        # Parameters:       sentence_number (int), to_highlight (boolean), previous_words_to_compare (list of words),
                            # previous_sentence (string), orientation (string)
        # Returns:          sentence_attributes (dictionary)

        def display_sentence(self, sentence_number, to_highlight, previous_words_to_compare, previous_sentence, orientation):


            # Initializes keys for a dictionary that will store sentence attributes which the function will return
            attributes = [ "input_word", "words_to_compare", "highlighted_sentence" ]
            sentence_attributes = dict.fromkeys(attributes, None)

            # Checks to see whether or not a sentence will be re-displayed
            if previous_sentence is not None:
                # Updates the values of the keys in the sentence_attributes dictionary with the previous information
                # including the highlighted sentence and the list of words that were highlighted
                sentence_attributes["words_to_compare"] = previous_words_to_compare
                sentence_attributes["highlighted_sentence"] = previous_sentence

                # This checks the orientation of the book and displays it accordingly
                if orientation == "horizontal":
                    narrator(previous_sentence)
                    sentence_attributes["input_word"] = word_change
                    nvl_clear()

                else:
                    renpy.call_screen ("custom_say_screen", previous_sentence, not None)
                    sentence_attributes["input_word"] = word_change


            else:
                # Calls a new sentence to highlight and display
                displayable_sentence = self.sentences[sentence_number]
                # Checks to see if the user wants to display highlighted sentence and displays it. If not
                # the original sentence will be displayed.
                if to_highlight == True:
                    # Highlights the sentence with the specific number to highlight
                    highlight_sentence_attributes = self.highlight_words(displayable_sentence ,1)

                    words_to_compare = highlight_sentence_attributes["words_changed"]
                    highlighted_sentence = highlight_sentence_attributes["sentence"]

                    # Updates the values of the keys in the sentence_attributes dictionary
                    sentence_attributes["words_to_compare"] = words_to_compare
                    sentence_attributes["highlighted_sentence"] = highlighted_sentence

                    # This checks the orientation of the book and displays it accordingly
                    if orientation == "horizontal":
                        narrator(highlighted_sentence)
                        sentence_attributes["input_word"] = word_change
                        nvl_clear()

                    else:
                        renpy.call_screen ("custom_say_screen", highlighted_sentence, not None)
                        sentence_attributes["input_word"] = word_change

                # When the original unhighlighted sentence is displayed
                else:

                    # Updates the values of the keys in the sentence_attributes dictionary
                    sentence_attributes["words_to_compare"] = None
                    sentence_attributes["highlighted_sentence"] = displayable_sentence

                    # This checks the orientation of the book and displays it accordingly
                    if orientation == "horizontal":
                        narrator(displayable_sentence)
                        sentence_attributes["input_word"] = word_change
                        nvl_clear()

                    else:
                        renpy.call_screen("custom_say_screen", displayable_sentence, not None)
                        sentence_attributes["input_word"] = word_change

            return sentence_attributes
