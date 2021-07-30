init python:
    # Creates a list of page objects
    # Parameters: list of strings, where the strings are the entire text of one page of the book
    # Returns: list of page objects

    def listing_pages (story_text):
        number_of_pages = len(story_text)
        page_list = []
        page_number = 1
        while page_number <= number_of_pages:
            page_list.append(Page(page_number, story_text, [], [], []))
            page_number += 1

        return page_list
