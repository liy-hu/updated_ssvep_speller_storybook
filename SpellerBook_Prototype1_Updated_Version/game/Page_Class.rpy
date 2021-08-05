init python:
    import re

    class Page:
        # Initializes class Page
        # Parameters: page number(int), list_of_pages(list of strings where each item in the list is the entire string text of a page)
        # sentences(empty list), words(empty list), words_to_highlight(list)
        # Returns: no returns
        def __init__(self, page_number, list_of_pages, sentences, words, words_to_highlight):
            self.page_number = page_number
            self.list_of_pages = list_of_pages
            self.sentences = sentences
            self.words = words
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
                return  len(whole_text)-len(splitted_text[-1])-len(punctuation)
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
                total_sentences += shown_text.count(punctuation_divider)
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
                    i += 1

            # Sorts the order_of_punctuations so that the end punctuations with the smaller indices will be first in the list.
            sorted_order_of_punctuations = sorted(order_of_punctuations)

            # Initializes the counter that tracks the number of sentences that have been appended to the instance attribute sentences.
            # Initializes the new_index and old_index to zero which will be used to "pick out" sentences from the string that contains
            # all the text on a page.
            # Initializes the last_line used to indicate the last sentence in the string
            n = 0
            new_index = 0
            old_index = 0
            last_sentence = total_sentences - 1


            # Loops through each condition ensuring that it is not "picking out" more sentences than there are the total number of
            # sentences
            while n < total_sentences:
                # Initializes the new_index to the index of the first end punctuation found in the string and as loop iterates it
                # initializes it to the next end punctuation found in the string.
                new_index = sorted_order_of_punctuations[n]

                # If loop reaches the last sentence of the string it is compared to two conditions
                if n == last_sentence:
                    # This tests whether or not the previous index had a  '"' char after it or in other words if the
                    # previous sentence ended with a '"' char instead of an end punctuation. If so, the string will look
                    # for the next index (old_index+1) to find the start of the new sentence as (old_index) would be where '"' is.
                    # If not, it will use (old_index).
                    if shown_text[old_index] == '"':
                        self.sentences.append(shown_text[old_index+1:].strip())
                    else:
                        self.sentences.append(shown_text[old_index:].strip())

                # If not the last sentence, the sentence in question will go through two conditions, with the second condtion
                # nested with two more conditions

                # This tests whether or not the sentence ends with '"' char instead of an end punctuation. If so, it will include
                # this '"' char along with the end punctuation by adding one to the end index (new_index+1) of the string indexing
                elif shown_text[new_index+1] == '"' :

                    if shown_text[old_index] == '"' and old_index > 0:
                        self.sentences.append(shown_text[old_index+1:new_index+2].strip())

                    else:
                        self.sentences.append(shown_text[old_index:new_index+2].strip())


                else:
                    # This tests whether or not the previous sentence ends with a '"' char instead of an end punctuation.
                    # If so, it will not include it and go to the next index (old_index+1) to find the start of the sentence.
                    # The condition old_index > 0 ensures that this applies to sentences after the first sentence as the first sentence
                    # has an old_index = 0 and would not have an old_index where the char is '"' since it is the first sentence and there
                    # would be no sentences prior to it.
                    # If it does not end with a '"' char or is the first sentence, it will just use the (old_index) to find the start of the sentence.
                    if shown_text[old_index] == '"' and old_index > 0:
                        self.sentences.append(shown_text[old_index+1:new_index+1].strip())

                    else:
                        self.sentences.append(shown_text[old_index:new_index+1].strip())


                # This updates the old_index so that the old_index indicates the first char of the next sentence or whatever comes
                # after the end punctuation. Ex ( Could be a letter or could be '"')
                old_index = new_index+1
                # This counter keeps track of how many sentences have been appended to the instance attribute
                n += 1

        # breaks down entire string of text of a page into a list of words and appends it to the words class attribute
        # Parameters: no parameters
        # Returns: no returns
        def get_words(self):
            # Creates a translation table and applies it to the entire string of text of a page to get rid of punctuation
            # so that the string can be split based on spaces and create a list of words puncutation free.
            translation_table = dict.fromkeys(map(ord, '!.?",'), None)
            self.list_of_pages[self.page_number-1] = self.list_of_pages[self.page_number-1].translate(translation_table)
            self.words = self.list_of_pages[self.page_number-1].split()


        # selects words to highlight based on the type of word we want to highlight either from its length or a word dictionary and append
        # it to instance attribute self.words_to_highlight
        # Parameters: type(string), word dictionary (dictionary), word length(int)
        # Returns: no returns

        def select_words_to_highlight(self, type, word_dict, word_length):

            # If words to highlight is based on word length then it will loop through the self.words (instance attribute)
            # while ensuring that it is case-insensitive and finds words in self.words that satisfy the length and appends
            # it to the self.words_to_highlight (instance attribute)

            if type == "length":
                for a_word in self.words:
                        updated_a_word = a_word.lower()
                        if len(updated_a_word) == word_length:
                            self.words_to_highlight.append(updated_a_word)

            # If words to highlight is based on a word dictionary then it will first loop through the self.words (instance attribute)
            # and test whether or not a word in self.words exists in the word dictionary. If it does then the value of the key (word)
            # is updated by adding one. After updating the word dictionary, the word dictionary will be looped through to check which
            # words have a value of 1 if it does then it is appended to self.words_to_highlight

            elif type == "word_file":
                for a_word in self.words:
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
            # Initializes a highlight color
            # Initializes a empty varible and an empty list
            highlight_words = self.words_to_highlight
            found_word = None
            found_words = []
            highlight_attributes = ["found_words", "sentence"]
            highlight_dict = dict.fromkeys(highlight_attributes, None)
            # This loops through the selected words to highlight and attempts to find a match object for the word in the given
            # sentence while ignoring letter case. If match exists then the start index of the word and the end index
            # are found and used to get the word from the sentence. This word is then appended to the list found_words
            for highlight_word in highlight_words:
                # This line of code is to ensure that re.search finds a word in a string and not a substring in a string.
                # Ex (To find word 'any' it will not return match if it reaches 'anyone', 'anyway' etc)
                my_regex = r'\b' + highlight_word + r'\b'
                match = re.search(my_regex, sentence, flags = re.ASCII | re.IGNORECASE)
                if match:
                    start_index = match.start()
                    end_index = match.end()
                    found_word = sentence[start_index:end_index]
                    if found_word not in found_words:
                        found_words.append(found_word)

            # If found_words is still an empty list it will return an unhighlighted sentence
            if not found_words:
                highlight_dict["sentence"] = sentence
                return highlight_dict

            # If found_words is not still empty
            elif found_words:
                # This checks whether or not the number specified to highlight makes sense with the number of words found.
                # (Ex Cannot highlight 4 words if there are only 3 words in found_words)
                if len(found_words) >= number_to_highlight:
                    i = 0

                    # This loops through to highlight a specified number
                    while i < number_to_highlight:

                        # Randomly chooses a word in found_words to highlight
                        word_to_change = found_words[i]
                        # Applies a the highlight color and underline
                        # highlight = "{u}{color="+highlight_color+"}" + word_to_change  + "{/color}{/u}"
                        highlight = "{=highlight}" + word_to_change  + "{/font}"
                        # Ensures that the word to replace with the highlighted word is again not a substring in a string but
                        # a word.
                        adjusted_word_to_change = r'\b' + word_to_change + r'\b'
                        # Replaces the unhighlighted word in the sentence with the highlighted word
                        highlighted_sentence = re.sub(adjusted_word_to_change, highlight, sentence, count =1, flags =0)
                        # Updates the sentence so that the already highlighted words will remain highlighted if user chooses
                        # to highlight more than one word.
                        sentence = highlighted_sentence
                        i+=1


                    highlight_dict["found_words"] = found_words
                    highlight_dict["sentence"] = sentence

                    return highlight_dict

                # If number specified to highlight does not make sense with the number of words found simply returns sentence
                elif len(found_words) < number_to_highlight:
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
                # sentence_attributes["input_word"] = renpy.call_screen ("say", None, previous_sentence)
                renpy.call_screen ("say", None, previous_sentence)
                sentence_attributes["input_word"] = word_change
                return sentence_attributes

                ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)
                # if orientation == "horizontal":
                #
                #     sentence_attributes["input_word"]  = renpy.call_screen ("nvl", previous_sentence)
                #     # sentence_attributes["input_word"] = word_change
                #     narrator(previous_sentence)
                #     nvl_clear()
                #
                # else:
                #     renpy.call_screen ("say", None, previous_sentence)
                #     sentence_attributes["input_word"] = word_change

                    # style.say_window = style.window_CUSTOM
                    # style.namebox = style.namebox_CUSTOMNAMEBOX
                    # style.say_dialogue = style.say_dialogue_CUSTOM
                    # style.textbox = style.CUSTOM_textbox
                    # style.vbox = style.vbox_CUSTOM
                    # style.input_style_text = style.CUSTOM_input_style_text
                #
                # elif orientation == "vertical":
                #     renpy.call_screen("say", None, previous_sentence)
                #     sentence_attributes["input_word"] = word_change
                # return sentence_attributes
                ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)

            else:
                displayable_sentence = self.sentences[sentence_number]
                if to_highlight == True:
                    highlight_sentence_attributes = self.highlight_words(displayable_sentence ,1)
                    words_to_compare = highlight_sentence_attributes["found_words"]
                    highlighted_sentence = highlight_sentence_attributes["sentence"]

                    sentence_attributes["words_to_compare"] = words_to_compare
                    sentence_attributes["highlighted_sentence"] = highlighted_sentence
                    # sentence_attributes["input_word"] = renpy.call_screen ("say", None, highlighted_sentence)
                    renpy.call_screen ("say", None, highlighted_sentence)
                    sentence_attributes["input_word"] = word_change
                    return sentence_attributes

                    ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)
                    # if orientation == "horizontal":
                    #     sentence_attributes["input_word"] = renpy.call_screen ("nvl", highlighted_sentence)
                    #     # sentence_attributes["input_word"] = word_change
                    #     narrator(highlighted_sentence)
                    #     nvl_clear()

                        # style.say_window = style.window_CUSTOM
                        # style.namebox = style.namebox_CUSTOMNAMEBOX
                        # style.say_dialogue = style.say_dialogue_CUSTOM
                        # style.textbox = style.CUSTOM_textbox
                        # style.vbox = style.vbox_CUSTOM
                        # style.input_style_text = style.CUSTOM_input_style_text

                    # else:
                    #     renpy.call_screen ("say", None, highlighted_sentence)
                    #     sentence_attributes["input_word"] = word_change
                    # elif orientation == "vertical":
                    #     renpy.call_screen("say",None, highlighted_sentence)
                    #     sentence_attributes["input_word"] =  word_change
                    # return sentence_attributes
                    ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)


                else:
                    sentence_attributes["words_to_compare"] = None
                    sentence_attributes["highlighted_sentence"] = displayable_sentence
                    # sentence_attributes["input_word"] = renpy.call_screen ("say",None, displayable_sentence)

                    renpy.call_screen ("say", None, displayable_sentence)
                    sentence_attributes["input_word"] = word_change
                    return sentence_attributes

                    ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)
                    # if orientation == "horizontal":
                    #     sentence_attributes["input_word"] = renpy.call_screen ("nvl", displayable_sentence)
                    #     # sentence_attributes["input_word"] = word_change
                    #
                    #     narrator(displayable_sentence)
                    #     nvl_clear()

                        # style.say_window = style.window_CUSTOM
                        # style.namebox = style.namebox_CUSTOMNAMEBOX
                        # style.say_dialogue = style.say_dialogue_CUSTOM
                        # style.textbox = style.CUSTOM_textbox
                        # style.vbox = style.vbox_CUSTOM
                        # style.input_style_text = style.CUSTOM_input_style_text

                    # else:
                    #     renpy.call_screen ("say", None, displayable_sentence)
                    #     sentence_attributes["input_word"] = word_change
                    # elif orientation == "vertical":
                    #     renpy.call_screen("say",None, displayable_sentence)
                    #     sentence_attributes["input_word"] = word_change

                    # return sentence_attributes
                    ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)
