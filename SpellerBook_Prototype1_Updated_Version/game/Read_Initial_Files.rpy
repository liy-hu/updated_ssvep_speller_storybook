init python:
    # This reads the textfile containing the story and splits it into a list of lines per page
    # Parameters: File name of text file to be read
    # Returns: list of strings, where the strings are the entire text of one page of the story
    def read_story_file(fname):
        file = renpy.file(fname).read().decode("utf-8")
        filelines = file.split("pg:")
        updated_filelines = []
        for line in filelines:
            updated_filelines.append(line.replace("\n", " "))

        # Removes any white space considered as an item in the list, so that the list contains only text
        if updated_filelines[0] == "":
            updated_filelines.remove(updated_filelines[0])

        pages_of_book = []

        for updated_line in updated_filelines:

            if updated_line != '':
                string_list = updated_line.split(' ')
                page_number = string_list[0]

                pn_length = len(page_number)
                pages_of_book.append(updated_line[pn_length:].strip())



        return pages_of_book

    # This reads the textfile containing the dolch lists and splits it into words
    # Parameters: File name of dolch list to be read
    # Returns a list of dolch words
    def read_dolch_file(dname):
        dolch_file = renpy.file(dname).read().decode("utf-8")
        dolch_list = dolch_file.split(",")

        updated_dolch_list = []
        for dolch_line in dolch_list:
                updated_dolch_list.append(dolch_line.replace("\n", " ").strip())

        dolch_dict = dict.fromkeys(updated_dolch_list, 0)
        return dolch_dict


    # This reads the dolch dictionary and the story text and compares the word
