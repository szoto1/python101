import webbrowser

def open_web(tab=0, website="https://www.google.pl"):
    """
    Open new tab (0) or new browser (1) and open url, if possible
    """
    if tab == 0:
        open_browser_tab(website)
    else:
        open_browser(website)

def open_browser(website):
    """
    Open url in a new window of the default browser, if possible
    """

    webbrowser.open_new(website)


def open_browser_tab(website):
    """
    Open url in a new page (“tab”) of the default browser, if possible
    """

    webbrowser.open_new_tab(website)

