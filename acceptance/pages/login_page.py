from . import base

import os

class LoginPage(base.BasePage):
    URL_TEMPLATE = "{baseurl}/web/login"
    _username_field_locator = ("name", "login")
    _password_field_locator = ("name", "password")
    _form_locator = ("css", ".oe_login_form")
    _form_submit_locator = ("css", ".btn-block")

    @property
    def loaded(self):
        form = self.find_element(*self._form_locator)
        return form.visible if form else False

    def login(self, username, password):
        self.find_element(*self._username_field_locator).fill(username)
        self.find_element(*self._password_field_locator).fill(password)
        self.find_element(*self._form_submit_locator).click()
