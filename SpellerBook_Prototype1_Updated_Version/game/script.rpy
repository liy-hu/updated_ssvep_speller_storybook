label initialization:
    # Variables used for the custom input option in word length and word file preferences.
    # Also includes the variables used for the custom input option in the story selection preference.
    init:
        default my_word_file = ""
        default my_word_length = ""
        default my_story_name = ""

    # Variables used to store the number of attempts made and the input entered by the user
        default word_change = ""
        default attempts = 0

    # Functions and styles used for the custom input option in word length, word file and story selection preferences
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

    # These two variables only pertain to the word length preference
    default plus = False
    default minus = False

    # Setting default story
    default persistent.story_choice = "Paper_Bag_Princess"
    default persistent.custom_story = False

    # Setting default song choice
    default persistent.song_choice = "None"

    # Setting the default number of attempts that user is allowed
    default persistent.attempt_limit = 3


label start:
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
        if persistent.custom_story == True:
            $ persistent.custom_story = False
            python:
                story_name = my_story_name
                fname = 'textfiles/'+ str(my_story_name) + '.txt'
                orientation = "vertical"

            $ persistent.story_choice = "Paper_Bag_Princess"


        elif persistent.story_choice == "Paper_Bag_Princess":
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

        # ADD MORE DEFAULT STORIES HERE
            # elif persistent.story_choice == "name of story":
                # $ story_name = "name of story"
                # $ fname = "textfiles/name of story.txt"


        # Sets up image formation and display on page
        python:
            story = story_name
            pg_image_number = "1"
        image pg_image = "images/[story]_pg[pg_image_number].png"
        image title_page = "images/[story]_Title_pg.png"

        # Sets up text reading and display on page
        python:

            # Reading initial story textfile and checking if a name of a custom story exists/makes sense
            try:
                story_text = read_story_file(fname)

            except IOError:
                renpy.call_screen ("invalid_input_error", 'story name')
                pass

            # Setting initial attributes of the story
            length_of_story = len(story_text)
            pg_text_number = 1

            # Creating a list of Page objects
            pages = listing_pages(story_text)

            # Defining end punctuation
            text_dividers = [ '.', '?', '!']

            # Initializing the variable a_page which will store the current Page object
            a_page = pages[pg_text_number - 1]

        # Used to determine the origin of the highlighted words and their difficulty level based on either
        # pre-determined or custom inputted word lengths or word files.
        if persistent.type == "length":
            $ type = "length"
            $ the_dict = None

        # Used to test whether or not a custom input was entered in the word length preference screen
            if persistent.custom_change == True:
                $ persistent.custom_change = False
                # Used to see if entered input is a valid input
                python:
                    try:
                        int(my_word_length)
                        the_length = int(my_word_length)
                    except ValueError:
                        renpy.call_screen ("invalid_input_error", persistent.type)
                        pass


            elif persistent.difficulty == -1:
                $ the_length = 2


            elif persistent.difficulty == 0:
                $ the_length = 3


            elif persistent.difficulty == 1:
                $ the_length = 4


            elif persistent.difficulty == 2:
                $ the_length = 5


            # ADD MORE DIFFICULTY LEVELS HERE BASED ON LENGTH
                # elif persistent.difficulty == [number for difficulty]
                    # $ the_length = [length of word]


        elif persistent.type == "word_file":
            $ type = "word_file"
            $ the_length = None

            # Used to test whether or not a custom input was entered in the word file preference screen
            if persistent.custom_change == True:
                $ persistent.custom_change = False
                # Used to see if entered input is a valid input
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

        # shows title page first
        $ show_title_page()
        window hide
        pause

        label prepare_page:
            ## IGNORE FOR NOW TESTING MUSIC PLAYING CODE
            # play music "audio/Here Comes The Sun (Remastered 2009).mp3"
            ## IGNORE FOR NOW TESTING MUSIC PLAYING CODE

            # Checks to see if the page exists
            if int(pg_image_number) <= length_of_story:
                # This is to update the instance attribute sentences and fill the attribute (which is a list) up with all the collected sentences of a page.
                $ a_page.get_sentences(text_dividers)
                # The number of sentences is obtained.
                $ number_of_sentences = len(a_page.sentences)
                # Sets counter to count the number of sentences displayed
                $ i = 0
                # Jumps to display the sentences in the page
                jump display_sentences

            else:
                jump finished_story

        label display_sentences:

            # Checks to see if there are still sentences from a page that needs to be displayed
            if i < number_of_sentences:
                # Clears the previous input by user
                $ word_change = ""

                # Used to determine orientation of storybook
                if orientation == "vertical":
                    $ show_page_image()

                if orientation == "horizontal":
                    $ show_entire_image()
                    window hide
                    pause
                    define narrator = nvl_narrator


                # Sets an empty dictionary to store sentence attributes that will be returned by Page_Class display_sentence() method
                $ sentence_dict ={}
                # Sets a counter to count the number of attempts completed
                $ attempts = persistent.attempt_limit
                # Selects the words that will be eligible to highlight in a given sentence as well as how these words will be chosen.
                $ a_page.select_words_to_highlight(i, type, the_dict, the_length, plus, minus)
                # Displays the sentence and fills the previously empty dictionary with sentence attributes
                $ sentence_dict = a_page.display_sentence(i, True, None, None, orientation)


                label re_display_sentence:

                    # Word spelled and or inputted by user
                    $ spell_word = sentence_dict["input_word"]
                    # List of words that contain the correct spelling of words
                    $ compare_words = sentence_dict["words_to_compare"]
                    # The updated sentence that will be displayed on game screen
                    $ final_sentence = sentence_dict["highlighted_sentence"]

                    # Ensures that the word spelled by the user (inputted by user) is actually going to be compared to a word that exists or is highligthed

                    if compare_words is not None:
                        # This counter and while loop is for when more than one word is highlighted in a sentence (currently the default is 1)
                        $ w = 0
                        while w < len(compare_words):
                            # Compares the correct spelling of target word and word spelled by user
                            if compare_words[w].lower() == word_change.lower():
                                # Updates the counter that keeps track of how many sentences of a page have been displayed
                                $ i +=1

                                # Reward screen for horizontal books
                                if orientation == "horizontal":
                                    $ correct_message = "{=correct}Awesome Job!{/font} " + " The correct spelling is: " + "{=correct_word_light}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page"
                                    $ narrator(correct_message)
                                    $ nvl_clear()
                                # Reward screen for vertical books
                                else:
                                    $ correct_message = "{=correct}Awesome Job!{/font} " + " The correct spelling is: " + "{=correct_word_dark}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page"
                                    $ renpy.call_screen("custom_say_screen", correct_message, not None)

                                # Jumps to display new sentence
                                jump display_sentences

                            else:
                                # Keeps track of the number of attempts made by user
                                if attempts > 0:

                                    # Clears the previous input by user
                                    $ word_change = ""

                                    # Updates sentence dictionary, displays the same sentence again and increments the attempt counter
                                    $ sentence_dict = a_page.display_sentence(i, True, compare_words, final_sentence, orientation)

                                    # Jumps to allow the user to retry again
                                    jump re_display_sentence

                                # After attempts by user exceeds specified attempt limit
                                else:
                                    # Updates the counter that keeps track of how many sentences of a page have been displayed
                                    $ i += 1

                                    # Encouragement screen for horizontal books
                                    if orientation == "horizontal":
                                        $ incorrect_message = "{=incorrect}Nice Try!{/font} " + " The correct spelling is: " + "{=correct_word_light}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page"
                                        $ narrator(incorrect_message)
                                        $ nvl_clear()

                                    # Encouragement screen for vertical books
                                    else:
                                        $ incorrect_message = "{=incorrect}Nice Try!{/font} " + " The correct spelling is: " + "{=correct_word_dark}" + compare_words[w] + "{/font}" +  "\n\nYou spelled: " + "{=saved_input}" + word_change + "{/font}" + "\nPress enter to advance to the next page"
                                        $ renpy.call_screen("custom_say_screen", incorrect_message, not None)

                                    # Jumps to display new sentence
                                    jump display_sentences

                            # Increments counter that keeps track of how many highlighted words have been checked with user input for spelling in a sentence
                            # (assuming that the number of highlighted words per sentence is more than 1)
                            $ w += 1


                    # If no words highlighted for particular sentence, show new sentence
                    else:
                        # Updates the counter that keeps track of how many sentences of a page have been displayed
                        $ i += 1
                        # Jumps to display new sentence
                        jump display_sentences

            # If no text on a page and just a picture, fill entire screen with image instead
            elif number_of_sentences == 0:
                $ show_entire_image()
                window hide
                pause


        label turn_page:
            # Function called to update Page object a_page
            $ update_pages()

            # Function called to update global variable page_image_number to update Image object pg_image
            $ update_page_image()

            # Jumps to prepare the new page
            jump prepare_page

            # stop music fadeout 1.0

        label finished_story:
            return
        return
