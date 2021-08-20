
# Varibles used for custom input option in word origin and story selection preference screens
init:
    default my_word_file = ""
    default my_word_length = ""
    default my_story_name = ""


    default word_change = ""
    default attempts = 0


# Functions and styles used for custom input option in word origin and story selection preference screens
init python:
    def word_file_func(newstring):
        store.my_word_file = newstring

    def word_length_func(newstring):
        store.my_word_length = newstring

    def story_name_func(newstring):
        store.my_story_name = newstring


    style.input.size = 60
    style.input.color = "#000"

# Default values for difficulty level and word origin
default persistent.custom_change = False
default persistent.difficulty = 1
default persistent.type = "length"
default persistent.plus = None
default persistent.minus = None

# Setting default story
default persistent.story_choice = "Paper_Bag_Princess"

# Setting song choice
default persistent.song_choice = "None"

# Setting the number of attempts that user is allowed
default persistent.attempt_limit = 3


label start:
    $ style.say_window = style.window
    $ style.namebox = style.namebox

    # $ plus = True
    # $ minus = None

    # $ myfile_name = "textfiles/hello_world.txt"
    # $ write_file(myfile_name)
    jump passive_setting
    # Interactive Speller_Story_Book
    label interactive_setting:
        python:
            cname = "Character_List.txt"
            names, emotions, states= read_character_attributes_list(fname)
            created_characters = listing_character_object(names, emotions, states)


    # Passive Speller_Story_Book
    label passive_setting:



        # Used to determine the song choice
        if persistent.song_choice == "Here Comes The Sun":
            $ song_name = "audio/Here Comes The Sun (Remastered 2009).mp3"

        # ADD MORE SONGS HERE
            # elif persistnet.song_choice == "name of song":
                # $ song_name = "audio/name of song.txt"

        # Used to determine the story choice
        if persistent.story_choice == "Paper_Bag_Princess":
            $ story_name = "Paper_Bag_Princess"
            $ fname = "textfiles/Paper_Bag_Princess.txt"
            $ orientation = "vertical"

        elif persistent.story_choice == "I_Want_My_Hat_Back":
            $ story_name = "I_Want_My_Hat_Back"
            $ fname = "textfiles/I_Want_My_Hat_Back.txt"
            $ orientation = "vertical"

        elif persistent.story_choice == "I_Have_To_Go":
            $ story_name = "I_Have_To_Go"
            $ fname = "textfiles/I_Have_To_Go.txt"
            $ orientation = "vertical"

        elif persistent.story_choice == "The_Giving_Tree":
            $ story_name = "The_Giving_Tree"
            $ fname = "textfiles/The_Giving_Tree.txt"
            $ orientation = "horizontal"



        # ADD MORE STORIES HERE
            # elif persistent.story_choice == "name of story":
                # $ story_name = "name of story"
                # $ fname = "textfiles/name of story.txt"


        # Sets up image formation and display on page
        python:
            story = story_name
            pg_image_number = "1"
        image pg_image = "images/[story]_pg[pg_image_number].png"
        image ky_image = "keyboard.png"

        # Sets up text reading and display on page
        python:

            # reading initial files
            story_text = read_story_file(fname)
            # dict_dolch = read_dolch_file(dname)

            # initial attributes of the story
            length_of_story = len(story_text)
            pg_text_number = 1

            # creating list of page_text and page_words objects
            pages = listing_pages(story_text)

            # defining end punctuation
            text_dividers = [ '.', '?', '!']

            # initializing the variable page_text and page_word objects
            a_page = pages[pg_text_number - 1]

        # Used to determine the highlight words origin and level of difficulty based on either
        # pre-determined or custom inputted word lengths or a word file.
        if persistent.type == "length":
            $ type = "length"
            $ the_dict = None
            $ plus = None
            $ minus = None

        # Used to test whether a custom input was entered in the word origin preference screen
            if persistent.custom_change == True:
                $ persistent.custom_change = False
                # $ narrator("hello I am in custom")
                python:
                    try:
                        int(my_word_length)
                        the_length = int(my_word_length)
                    except ValueError:
                        renpy.call_screen ("invalid_input_error", persistent.type)
                        pass


            elif persistent.difficulty == -1:
                $ the_length = 2
                if persistent.plus == True:
                    $ plus = True
                elif persistent.minus == True:
                    $ minus = True

            elif persistent.difficulty == 0:
                $ the_length = 3
                if persistent.plus == True:
                    $ plus = True
                elif persistent.minus == True:
                    $ minus = True

            elif persistent.difficulty == 1:
                $ the_length = 4
                if persistent.plus == True:
                    $ plus = True
                elif persistent.minus == True:
                    $ minus = True

            elif persistent.difficulty == 2:
                $ the_length = 5
                if persistent.plus == True:
                    $ plus = True
                elif persistent.minus == True:
                    $ minus = True

            # ADD MORE DIFFICULTY LEVELS HERE BASED ON LENGTH
                # elif persistent.difficulty == [number for difficulty]
                    # $ the_length = [length of word]


        elif persistent.type == "word_file":
            $ type = "word_file"
            $ the_length = None

            # Used to test whether a custom input was entered in the word origin preference screen
            if persistent.custom_change == True:
                $ persistent.custom_change = False
                python:
                    try:
                        str(my_word_file)
                        dname = 'textfiles/'+ str(my_word_file) + '.txt'
                        the_dict = read_dolch_file(dname)
                    except IOError:
                        renpy.call_screen ("invalid_input_error", persistent.type)
                        pass

            elif persistent.difficulty == -1:
                $ dname = 'textfiles/dolch_list_pre-k.txt'
                $ the_dict = read_dolch_file(dname)

            elif persistent.difficulty == 0:
                $ dname = 'textfiles/dolch_list_kindergarten.txt'
                $ the_dict = read_dolch_file(dname)

            elif persistent.difficulty == 1:
                $ dname = 'textfiles/dolch_list_1st_grade.txt'
                $ the_dict = read_dolch_file(dname)

            elif persistent.difficulty == 2:
                $ dname = 'textfiles/dolch_list_2nd_grade.txt'
                $ the_dict = read_dolch_file(dname)

            elif persistent.difficulty == 3:
                $ dname = 'textfiles/dolch_list_3rd_grade.txt'
                $ the_dict = read_dolch_file(dname)

            # ADD MORE DIFFICULTY LEVELS HERE BASED ON WORD LIST
                # elif persistent.difficulty == [number for difficulty]
                    # $ dname = 'textfiles/name of txt file'
                    # $ the_dict = read_dolch_file(dname)


        label prepare_page:
            ## IGNORE FOR NOW TESTING MUSIC PLAYING CODE
            # play music "audio/Here Comes The Sun (Remastered 2009).mp3"
            ## IGNORE FOR NOW TESTING MUSIC PLAYING CODE
            if int(pg_image_number) <= length_of_story:

                # This is to update the instance attribute sentences and fill the attribute (which is a list) up with sentences of a page.
                # The number of sentences is also obtained.
                $ a_page.get_sentences(text_dividers)
                $ number_of_sentences = len(a_page.sentences)

                # sets counter to count the number of sentences displayed
                $ i = 0
                # jumps to proceed to display the sentences in the page
                jump display_sentences

            jump while_has_finished

        label display_sentences:

            if i < number_of_sentences:
                # clears the previous input by user
                $ word_change = ""

                # Used to determine orientation of storybook
                if orientation == "vertical":
                    $ show_page_image()

                if orientation == "horizontal":
                    $ show_entire_image()
                    window hide
                    pause
                    define narrator = nvl_narrator


                # sets an empty sentence dictionary to store sentence attributes that will be returned by Page_Class display_sentence() method
                $ sentence_dict ={}
                # sets a counter to count the number of attempts completed
                $ attempts = persistent.attempt_limit
                # selects the words that will be eligible to highlight in a given sentence as well as how these words will be chosen.
                $ a_page.select_words_to_highlight(i, type, the_dict, the_length, plus, minus)

                # filling the sentence dictionary with the returned sentence attributes
                $ sentence_dict = a_page.display_sentence(i, True, None, None, orientation)

                label re_display_sentence:

                    # word spelled by user
                    $ spell_word = sentence_dict["input_word"]
                    # correct spelling of word
                    $ compare_words = sentence_dict["words_to_compare"]
                    # sentence displayed on game screen
                    $ final_sentence = sentence_dict["highlighted_sentence"]

                    if compare_words is not None:
                        # ensures that the word spelled by the user (inputted by user) is actually going to be compared to a word that exists or is highligthed
                        # compares the correct spelling of target word and word spelled by user
                        $ w = 0
                        while w < len(compare_words):

                            if compare_words[w].lower() == word_change.lower():
                                $ i +=1
                                # reward screen for correct spelling
                                # $ narrator("{=correct}Awesome Job!{/font} " + " The correct spelling of the word is: " + "{=correct_word}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page")
                                $ correct_message = "{=correct}Awesome Job!{/font} " + " The correct spelling of the word is: " + "{=correct_word}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page"
                                if orientation == "horizontal":
                                    $ narrator(correct_message)
                                    $ nvl_clear()
                                else:
                                    $ renpy.call_screen("custom_say_screen", correct_message, not None)
                                # jumps to display new sentence

                                jump display_sentences

                            else:
                                # keeps track of the number of attempts made by user
                                if attempts > 0:

                                    # clears the previous input by user
                                    $ word_change = ""
                                    # updates sentence dictionary, displays the same sentence again and increments the attempt counter
                                    $ sentence_dict = a_page.display_sentence(i, True, compare_words, final_sentence, orientation)
                                    # jumps to allow the user to retry again
                                    jump re_display_sentence

                                # performed after attempts by user exceeds specified attempt limit and shows nice try screen.
                                else:
                                    $ i += 1
                                    # $ narrator("{=incorrect}Nice Try!{/font} " + " The correct spelling of the word is: " + "{=correct_word}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page")
                                    $ incorrect_message = "{=incorrect}Nice Try!{/font} " + " The correct spelling of the word is: " + "{=correct_word}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page"
                                    if orientation == "horizontal":
                                        $ narrator(incorrect_message)
                                        $ nvl_clear()

                                    else:
                                        $ renpy.call_screen("custom_say_screen", incorrect_message, not None)

                                    # jumps to display new sentence
                                    jump display_sentences

                            $ w += 1

                    # if no words highlighted for particular sentence, show new sentence
                    else:
                        $ i += 1
                        # jumps to display new sentence
                        jump display_sentences

            elif number_of_sentences == 0:
                # If no text on a page, fill entire screen with image instead
                $ show_entire_image()
                window hide
                pause

            jump turn_page


        label turn_page:
            # Functions used to update page and page image
            $ update_pages()
            $ update_page_image()
            jump prepare_page

            # stop music fadeout 1.0


        return
