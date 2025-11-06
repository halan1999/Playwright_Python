import random
from playwright.sync_api import Page, expect



class BaseComponent():
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK ="#logout_sidebar_link"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    def __init__(self, page: Page):
        self.page = page   
    
    