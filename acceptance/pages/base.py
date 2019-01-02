from pypom import page

import os


class BasePage(page.Page):
    def __init__(self, *args, **kwargs):
        base_url = os.environ.get('TEST_SERVER_URL', 'http://localhost:1234')
        super().__init__(*args, **kwargs, baseurl=base_url)
