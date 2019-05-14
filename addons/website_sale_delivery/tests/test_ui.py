import odoo.tests
# Part of Odoo. See LICENSE file for full copyright and licensing details.


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_free_delivery_when_exceed_threshold(self):
        self.phantom_js("/web", "odoo.__DEBUG__.services['web_tour.tour'].run('check_free_delivery')", "odoo.__DEBUG__.services['web_tour.tour'].tours.check_free_delivery.ready", login="admin")
