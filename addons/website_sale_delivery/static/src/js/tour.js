odoo.define('website_sale_delivery.tour', function (require) {
    'use strict';

    var tour = require("web_tour.tour");
    var rpc = require("web.rpc");

    tour.register('check_free_delivery', {
            test: true,
            url: '/shop',
        },
        [
            {
                content: "Set fixed price for delivery charges",
                trigger: '#oe_main_menu_navbar',
                run: function () {
                    return rpc.query({
                        'model': 'delivery.carrier',
                        'method': 'write',
                        'args': [[1], {
                            'fixed_price': 2,
                            'free_over': true,
                            'amount': 10
                        }],
                    })
                }
            },
            {
                content: "search conference chair",
                trigger: 'form input[name="search"]',
                run: "text conference chair",
            },
            {
                content: "search conference chair",
                trigger: 'form:has(input[name="search"]) .oe_search_button',
            },
            {
                content: "select conference chair",
                trigger: '.oe_product_cart:first a:contains("Conference Chair")',
            },
            {
                content: "select Conference Chair Aluminium",
                extra_trigger: '#product_detail',
                trigger: 'label:contains(Aluminium) input',
            },
            {
                content: "select Conference Chair Steel",
                extra_trigger: '#product_detail',
                trigger: 'label:contains(Steel) input',
            },
            {
                content: "click on add to cart",
                extra_trigger: 'label:contains(Steel) input:propChecked',
                trigger: '#product_detail form[action^="/shop/cart/update"] .btn-primary',
            },
            {
                content: "click in modal on 'Proceed to checkout' button",
                trigger: 'button:contains("Proceed to Checkout")',
            },
            {
                content: "add hundred more",
                trigger: 'input.js_quantity.form-control.quantity',
                run: "text 100",
            },
            {
                content: "go to checkout",
                extra_trigger: '#cart_products input.js_quantity:propValue(100)',
                trigger: 'a[href*="/shop/checkout"]',
            },
            {
                content: "Check Free Delivery value to be zero",
                trigger: "#delivery_carrier span:contains('0.0')"
            },
        ]
    );
});
