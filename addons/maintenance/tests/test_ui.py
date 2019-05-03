from odoo.tests.common import HttpCase


class RandomTestCase(HttpCase):
    def test_13_hello_world(self):
        expected = "123"
        actual = "324"

        self.phantom_js("/web", "console.log('ok');")

    # def test_01_mail_sent(self):
    #     code = """
    #         setTimeout(function () {
    #             $(".mail_sent").click();
    #             setTimeout(function() { console.log('ok'); }, 30000);
    #
    #         }, 1000);
    #     """
    #     ref = self.ref('mail.mail_channel_action_client_chat')
    #     link = f"/web#action={ref}"
    #     ready = "odoo.__DEBUG__.services['mail_sent.sent'].is_ready"
    #     self.phantom_js(link, code, ready=ready, login="demo")
