init python:
    # updates the page to the next page
    # Parameters: no parameters
    # Returns: no return
    def update_pages():
        global pg_text_number, length_of_story, a_page, pages
        if pg_text_number < length_of_story:
            pg_text_number += 1
            a_page = pages[pg_text_number-1]


    # updates the page image
    # Parameters: no parameters
    # Returns: no return
    def update_page_image():
        global pg_image_number, length_of_story, pg_image
        if int(pg_image_number) <= length_of_story:
            number = int(pg_image_number) + 1
            pg_image_number = str(number)
