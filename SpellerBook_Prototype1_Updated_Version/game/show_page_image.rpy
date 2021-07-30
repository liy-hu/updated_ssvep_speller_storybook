init python:

    # shows image on screen with proper size and scale
    # Parameters: no parameters
    # Returns: no return
    def show_page_image():
        global pg_image
        xsize_image = config.screen_width / 2
        ysize_image = config.screen_height
        fit_style = 'fill'
        renpy.show ('pg_image', at_list=[Transform(child = 'pg_image', function = None, xsize = xsize_image , ysize = ysize_image,
        fit = fit_style), Position(xpos = 0.5, ypos = 0.0, anchor = (0.0,0.0))], what=None, zorder=0, tag=None, behind=[])

    def show_entire_image():
        global pg_image
        xsize_image = config.screen_width
        ysize_image = config.screen_height
        fit_style = 'fill'
        renpy.show ('pg_image', at_list=[Transform(child = 'pg_image', function = None, xsize = xsize_image , ysize = ysize_image,
        fit = fit_style), Position(xalign = 0.5, yalign = 0.5)], what=None, zorder=0, tag=None, behind=[])

    ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)
    # def show_horizontal_page_image():
    #     global pg_image
    #     xsize_image = config.screen_width
    #     ysize_image = config.screen_height*(0.80)
    #     fit_style = 'fill'
    #     renpy.show ('pg_image', at_list=[Transform(child = 'pg_image', function = None, xsize = xsize_image , ysize = ysize_image,
    #     fit = fit_style), Position(xalign = 0.5, yalign =0.0)], what=None, zorder=0, tag=None, behind=[])
    ## IGNORE FOR NOW (TESTING CODE FOR DISPLAYING DIFFERENT TYPES OF PICTURE BOOKS)
