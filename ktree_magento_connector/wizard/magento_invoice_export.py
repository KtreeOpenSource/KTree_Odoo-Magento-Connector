#This python file is used to call Invoice export wizard

import openerp.pooler
import os
from openerp.osv import osv, fields

class wizard_magneto_invoice_export(osv.osv_memory):
    _name = 'magneto.invoice.export'
    _description = 'Export Invoice'

    def do_invoice_export(self, cr, uid, ids, context=None):

        """ this function will call during synchronization of Invoices from Odoo to Magento """

        result=self.pool.get('magento.configuration').export_invoice(cr, uid)
        if (result < 0):
            raise osv.except_osv(('Warning'), ('Export failed, please refer to configure file for failure details.'))
        data_obj = self.pool.get('ir.model.data')
        if result >-1:
            text="%s Invoice Exported !" %result
            cust_text_ids=self.pool.get('number.record.import.export').search(cr, uid, [])
            for ids in cust_text_ids:
               self.pool.get('number.record.import.export').unlink(cr, uid, ids, context=None)
            
            self.pool.get('number.record.import.export').create(cr,uid,{'name':text,})
            xml_id='number_record_import_export_tree'
            res = data_obj.get_object_reference(cr, uid, 'ktree_magento_connector', xml_id)
            context.update({'view_id': res and res[1] or False})
            return {
                'name': 'No Of Records Export',
                'view_type':'form',
                'view_mode':'tree',
                'res_model':'number.record.import.export',
                'type':'ir.actions.act_window',
                'context':context,
            }
        

wizard_magneto_invoice_export()


