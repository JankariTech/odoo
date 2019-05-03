odoo.define('maintenance_schedule.tour', function (require) {
    "use strict";

    /**
     * Simulates a click event of given type on the given element.
     *
     * @param {DOMElement} el
     * @param {string} type - 'click', 'mouseup', ...
     */
    function simulateClickEvent(el, type) {
        var evt = document.createEvent('MouseEvents');
        evt.initMouseEvent(type, true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, el);
        el.dispatchEvent(evt);
    }

    var core = require('web.core');
    var tour = require('web_tour.tour');

    var _t = core._t;

    var options = {
        test: true,
        url: '/web',
    };

    var steps = [tour.STEPS.SHOW_APPS_MENU_ITEM, {
        trigger: '.o_app[data-menu-xmlid="maintenance.menu_maintenance_title"]',
        position: 'right',
    }, {
        trigger: 'a:contains("Scheduled"):first',
        position: 'right',
    }, {
        trigger: 'div.fc-day-grid td.fc-today',
        run: function (actions) {
            // actions.click(this.$anchor);

            var $h1 = this.$anchor;
            console.log();
            simulateClickEvent($h1[0], 'mousedown');
            simulateClickEvent($h1[0], 'mousedown');
        }
    }];

    tour.register('maintenance_schedule_tour', options, steps);
});
