init python:
    # import re

    class Page:
        # Initializes class Page
        # Parameters: page number(int), list_of_pages(list of strings where each item in the list is the entire string text of a page)
        # sentences(empty list), words(empty list), words_to_highlight(list)
        # Returns: no returns
        def __init__(self, page_number, list_of_pages, sentences, words_to_highlight):
            self.page_number = page_number
            self.list_of_pages = list_of_pages
            self.sentences = sentences
            self.words_to_highlight = words_to_highlight


        # Finds the index of a the nth punctuation mark
        # Parameters: punctuation mark(char), position number(int)
        # Returns: the index of the nth punctuation mark
        def find_nth_punctuation(self, punctuation, nth_pos):
            # all the text on a page in the form of a string
            whole_text = self.list_of_pages[self.page_number-1]
            # splits all the text on a page into a list of strings according to the puncutation char and the (nth_pos+1) number of splits
            # ex_string = "Hello World. This is a beautiful world. I love this world."
            # nth_pos = 1
            # splitted_ex_string = ex_string.split (".", nth_pos + 1)
            # Output -----> splitted_ex_string = [ "Hello World", " This is a beautiful world", " I love this world."]

            splitted_text = whole_text.split(punctuation, nth_pos+1)

            if len(splitted_text) <= nth_pos+1:
                return -1
            else:
                current_index = len(whole_text)-len(splitted_text[-1])-len(punctuation)
                try:
                    # checks if the end puncutation is within quotations
                    if whole_text[current_index+1] == '"':
                        updated_index = current_index + 1
                        return updated_index

                    # elif whole_text[current_index+1] == '.':
                    #     updated_index = current_index + 1
                    #     return updated_index

                except IndexError:
                    pass

                return current_index

            # len(ex_string)-len(splitted_ex_string[-1])-len(".") = 58-19-1 = 38


        # breaks down the entire string text of a page into individual strings where each string is a sentence and appends it to the
        # sentence class attribute
        # Parameters: punctuation dividers(list of punctuation chars)
        # Returns: no returns
        def get_sentences(self, punctuation_dividers):
            # all the text on a page in the form of a string
            shown_text = self.list_of_pages[self.page_number-1]
            order_of_punctuations = []
            total_sentences = 0
            # Loop goes through a specific end punctuation each time, whether it is a '.' '!' or '?' and counts the number of
            # times the end punctuation is found in the string and saves this number to number_of_chars. This number is also added to the counter named total_sentences to
            # to count the overall number of sentences.
            for punctuation_divider in punctuation_dividers:
                # total_sentences += shown_text.count(punctuation_divider)
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
                        continue

                    order_of_punctuations.append(char_index)
                    # Used to check if an end puncutation is repeated at the end of a sentence for emphasis. Ex ( He was... or This is amazing!!!)
                    # and ensures that the it is treated and shown as one sentence by only adding the index of the last end punctuation in the repeated
                    # sequence to the list of order_of_punctuations
                    if len(order_of_punctuations) > 1:
                        current_list_index = len(order_of_punctuations)-1
                        previous_list_index = current_list_index - 1

                        if order_of_punctuations[current_list_index]-1 == order_of_punctuations[previous_list_index]:
                            order_of_punctuations.remove(order_of_punctuations[previous_list_index])

                    i += 1

            # Sorts the order_of_punctuations so that the end punctuations with the smaller indices will be first in the list.
            sorted_order_of_punctuations = sorted(order_of_punctuations)
            total_sentences = len(sorted_order_of_punctuations)

            # Initializes the counter that tracks the number of sentences that have been appended to the instance attribute sentences.
            # Initializes the new_index and old_index to zero which will be used to "pick out" sentences from the string that contains
            # all the text on a page.
            # Initializes the last_line used to indicate the last sentence in the string
            n = 0
            new_index = 0
            old_index = 0

            # Loops through each condition ensuring that it is not "picking out" more sentences than there are the total number of
            # sentences
            if total_sentences >= 1:
                while n < total_sentences:
                    # Initializes the new_index to the index of the first end punctuation found in the string and as loop iterates it
                    # initializes it to the next end punctuation found in the string.
                    new_index = sorted_order_of_punctuations[n]

                    # Appends a sentence to the instance attribute sentences
                    self.sentences.append(shown_text[old_index:new_index+1].strip())
                    # This updates the old_index so that the old_index indicates the first char of the next sentence
                    old_index = new_index + 1
                    # This counter keeps track of how many sentences have been appended to the instance attribute
                    n += 1

            # This ensures that if text on a page did not have any end punctuation, it would still be shown.
            elif shown_text != '':
                self.sentences.append(shown_text)

        # breaks down entire string of text of a page into a list of words and appends it to the words class attribute
        # Parameters: no parameters
        # Returns: no returns

        def get_words_in_sentence(self, sentence):
            translation_table = dict.fromkeys(map(ord, '!.?",'), None)
            sentence = sentence.translate(translation_table)
            return sentence.split()

        # selects words to highlight based on the type of word we want to highlight either from its length or a word dictionary and append
        # it to instance attribute self.words_to_highlight
        # Parameters: type(string), word dictionary (dictionary), word length(int)
        # Returns: no returns
        def select_words_to_highlight(self, sentence_number, type, word_dict, word_length, plus, minus):

            # If words to highlight is based on word length then it will loop through the self.words (instance attribute)
            # while ensuring that it is case-insensitive and finds words in self.words that satisfy the length and appends
            # it to the self.words_to_highlight (instance attribute)

            a_sentence = self.sentences[sentence_number]
            words_in_sentence = self.get_words_in_sentence(a_sentence)
            self.words_to_highlight = []

            if type == "length":

                # for a_word in words_in_sentence:
                #     updated_a_word = a_word.lower()
                #     if len(updated_a_word) == word_length:
                #             self.words_to_highlight.append(updated_a_word)

                # If the user specifies to find words that are either equal or greater than the specified length (Ex words that are 3 letters or longer - 3+)
                if plus is True:

                    for a_word in words_in_sentence:
                        if len(a_word) >= word_length:
                            self.words_to_highlight.append(a_word)

                elif minus is True:

                    for a_word in words_in_sentence:
                        if len(a_word) <= word_length:
                            self.words_to_highlight.append(a_word)


                # elif len(range)!= 0:
                #
                #     for a_word in self.words:
                #         updated_a_word = a_word.lower()
                #         for r in range:
                #             if len(updated_a_word) == r :
                #                 self.words_to_highlight.append(updated_a_word)

            # If no word of that length exist in the sentence, look for the a word with lengths (the next greater length) than that
                else:
                    i = 0
                    while len(self.words_to_highlight) == 0:
                        for a_word in words_in_sentence:
                            if len(a_word) == (word_length+i):
                                self.words_to_highlight.append(a_word)

                        i+=1


            # If words to highlight is based on a word dictionary then it will first loop through the self.words (instance attribute)
            # and test whether or not a word in self.words exists in the word dictionary. If it does then the value of the key (word)
            # is updated by adding one. After updating the word dictionary, the word dictionary will be looped through to check which
            # words have a value of 1 if it does then it is appended to self.words_to_highlight

            elif type == "word_file":
                for a_word in words_in_sentence:
                    updated_a_word = a_word.lower()
                    if updated_a_word in word_dict:
                        word_dict[updated_a_word] += 1

                for k in word_dict:
                    if word_dict[k] != 0:
                        self.words_to_highlight.append(k)


        # applies the highlight to a specific number of selected words to highlight in a given sentence
        # Parameters: sentence(string), number to highlight(int)
        # Returns: updated sentence(string)
        def highlight_words(self, sentence, number_to_highlight):
            # Initializes a variable for words to highlight
            # Initializes a empty varible and an empty list
            highlight_words = self.words_to_highlight
            words_changed = []
            word_to_change = None
            highlight_attributes = ["words_changed", "sentence"]
            highlight_dict = dict.fromkeys(highlight_attributes, None)

            # If highlight_words is an empty list it will return an unhighlighted sentence
            if not highlight_words:
                highlight_dict["sentence"] = sentence
                return highlight_dict

            # If highlight_words is not empty
            elif highlight_words:

                # This checks whether or not the number specified to highlight makes sense with the number of words found.
                # (Ex Cannot highlight 4 words if there are only 3 words in found_words)
                if len(highlight_words) >= number_to_highlight:
                    i = 0
                    # This loops through to highlight a specified number
                    while i < number_to_highlight:


                        # picks a random word to highlight
                        word_to_change = renpy.random.choice(highlight_words)

                        # adds the randomly picked word to a list or words that will be highlighted
                        words_changed.append(word_to_change)

                        # removes the randomly picked word from the list of eligeble words to highlight so that it won't be highlighted again
                        highlight_words.remove(word_to_change)

                        # ensures that the format of the word in the sentence stays the same (Ex. HAVE will stay in all capital letters)

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
                        i+=1


                    highlight_dict["words_changed"] = words_changed
                    highlight_dict["sentence"] = sentence

                    return highlight_dict

                # If number specified to highlight does not make sense with the number of words found simply returns sentence
                elif len(highlight_words) < number_to_highlight:
                    highlight_dict["sentence"] = sentence
                    return highlight_dict


        # Calls upon highlight_words method and then displays updated sentence to textbox in screen
        # Parameters: the nth sentence in the page_text, to_highlight(boolean)
        # Returns: no returns

        def display_sentence(self, sentence_number, to_highlight, previous_words_to_compare, previous_sentence, orientation):
            # If user wants to display highlighted sentence then the it will be displayed. If not
            # the original sentence will be displayed.
            attributes = [ "input_word", "words_to_compare", "highlighted_sentence" ]
            sentence_attributes = dict.fromkeys(attributes, None)


            if previous_sentence is not None:
                sentence_attributes["words_to_compare"] = previous_words_to_compare
                sentence_attributes["highlighted_sentence"] = previous_sentence

                if orientation == "horizontal":
                    narrator(previous_sentence)
                    sentence_attributes["input_word"] = word_change
                    nvl_clear()

                else:
                    renpy.call_screen ("custom_say_screen", previous_sentence, not None)
                    sentence_attributes["input_word"] = word_change

                return sentence_attributes

            else:
                displayable_sentence = self.sentences[sentence_number]

                if to_highlight == True:
                    highlight_sentence_attributes = self.highlight_words(displayable_sentence ,1)
                    words_to_compare = highlight_sentence_attributes["words_changed"]
                    highlighted_sentence = highlight_sentence_attributes["sentence"]

                    sentence_attributes["words_to_compare"] = words_to_compare
                    sentence_attributes["highlighted_sentence"] = highlighted_sentence

                    if orientation == "horizontal":

                        narrator(highlighted_sentence)
                        sentence_attributes["input_word"] = word_change
                        nvl_clear()

                    else:

                        renpy.call_screen ("custom_say_screen", highlighted_sentence, not None)
                        sentence_attributes["input_word"] = word_change

                    return sentence_attributes


                else:
                    sentence_attributes["words_to_compare"] = None
                    sentence_attributes["highlighted_sentence"] = displayable_sentence

                    if orientation == "horizontal":

                        narrator(displayable_sentence)

                        sentence_attributes["input_word"] = word_change
                        nvl_clear()

                    else:

                        renpy.call_screen("custom_say_screen", displayable_sentence, not None)
                        sentence_attributes["input_word"] = word_change

                    return sentence_attributes
