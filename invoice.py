# Author : Hemanth Reddy K
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
from time import gmtime, strftime

MOM_address = 'Mothers on Mission, Bangalore, India'

class Invoice(invoice_number, template, MOM_address, client_address):
    def __init__(self):
        self.invoice_number = str(invoice_number)

        #check if file exists and not null
        self.invoices_savedir = './invoice' # invoices save directory
        self.name = os.path.join(self.invoices_savedir, self.invoice_number+'.html')
        # check if template exists
        self.template = template
        self.time = strftime("%d %b %Y %H:%M:%S", gmtime())

        self.from_address = str(MOM_address)
        self.to_address = str(client_address)

        self.total_bill = ''
        self.__payment_method = ''
        self.__paid_amount = ''
        self.__items = {}
        self.__all_items_template = ''

    def add_item(self, item, quantity, price):
        item_template = self__item_template().format(item=item,
                                                    quantity=str(quantity),
                                                    price=str(price)
                                                    )
        self.__all_items_template += item_template
        self.__items[item] = (quantity, price)
        return True

    def get_invoice(self):
        template = self.__read_template()
        invoice = template.translate(self.__translate_dict())
        with open(self.name ,'w') as f:
            f.write(invoice)
        #check if file exists and not null
        print('Invoice {name} generated'.format(name=self.name))
        return invoice

    def __translate_dict(self):
        translations = {
            '{{invoice_number}}' : self.invoice_number,
            '{{Created_date/today}}' : self.time,
            '{{company_address}}' : self.from_address,
            '{{client_address}}' : self.to_address,
            '{{payment_method}}' : self.__payment_method,
            '{{amount_paid}}' : self.__paid_amount,
            '{{get_items}}' : self.__all_items_template,
            '{{amount_total}}' : self.total_bill
            }
        return translations

    #can be made static
    def __item_template(self):
        # can be read from a file as well, but should not be required
        item_template = '''
                    <tr class="item">
                        <td>
                            {item}
                        </td>

                        <td>
                            {quantity}
                        </td>

                        <td>
                            {price}
                        </td>
                    </tr>
                    '''
        return item_template

    def __read_template(self):
        with open(self.template,'r') as f:
            template = f.read()
        return template

    def change_invoice_directory(self, path):
        # check if path exists
        self.invoices_savedir = path
        pass

    def get_items(self):
        pass

    def add_tax(self, tax):
        pass

    def add_delivery(self, delivery):
        pass

    def add_discount(self, coupon, discount):
        pass

    def add_payment(self, payment_method, amount_paid):
        self.__payment_method = payment_method
        self.__paid_amount = str(amount_paid)
        pass

    def remove_item(self, item, quantity):
        # Ideally shouldn't be required
        pass
