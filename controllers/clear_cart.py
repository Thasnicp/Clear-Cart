from odoo import http
from odoo.http import request


class WebsiteClearCart(http.Controller):
    @http.route(['/clear/cart'], type='http', auth="user", website=True)
    def clear_cart(self):
        order = request.env['sale.order'].search(
            [('id', '=', request.session.sale_order_id)])
        # print(order)
        # print(request.session.sale_order_id,"hii")
        for rec in order:
            if rec.state == 'draft':
                for line in rec.order_line:
                    line.unlink()
        return request.render("clear_cart.clear_cart_button",)

