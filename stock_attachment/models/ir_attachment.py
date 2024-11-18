# models/ir_attachment.py
from odoo import models, fields, api

class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    def action_preview_image(self):
        """Відкрити модальне вікно з прев'ю зображення"""
        self.ensure_one()  # Працюємо тільки з одним записом
        return {
            'type': 'ir.actions.act_window',
            'name': 'Image Preview',
            'res_model': 'ir.attachment',
            'res_id': self.id,
            'view_mode': 'form',
            'view_id': self.env.ref('stock_attachment.view_attachment_preview_form').id,
            'target': 'new',  # Модальне вікно
        }
