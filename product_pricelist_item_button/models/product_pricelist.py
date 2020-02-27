from odoo import fields, models


class Pricelist(models.Model):
    _inherit = 'product.pricelist'

    items_count = fields.Integer(
        compute='_compute_items_count',
        string='Pricelist Items Count')

    def _compute_items_count(self):
        for pricelist in self:
            pricelist.items_count = len(pricelist.item_ids)

    def action_product_pricelist_item(self):
        self.ensure_one()
        action = self.env.ref(
            'product_pricelist_item_button.act_product_pricelist_item') \
            .read()[0]
        action['domain'] = [('pricelist_id', '=', self.id)]
        action['context'] = {
            'default_pricelist_id': self.id,
            'pricelist_id_invisible': True
        }
        return action
