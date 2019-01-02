from pypom import page

class AppsPage(page.Page):
    _main_content_locator = ("css", ".o_kanban_ungrouped")
    _username_locator = ("css", ".oe_topbar_name")

    @property
    def loaded(self):
        return self.find_element(*self._main_content_locator).visible or False

    @property
    def username(self):
        return self.find_element(*self._username_locator).value
