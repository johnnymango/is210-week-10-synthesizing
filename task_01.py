#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterating Through Dictionaries."""


def sum_orders(customers, orders):
    """This function combines customer and order dictionary and sums the total
        number of order and the order total.

        Args:
            customers (dictionary): A dictionary containing customer data.
            orders (dictionary): A dictionary containing order data.

        Returns:
            Dictionary: A combined dictionary containing both customer and order
            data as well as the total number of orders and order total for every
            customer who has placed an order.

        Examples:
        >>> import data
        >>> import pprint
        >>> pprint.pprint(sum_orders(customers=data.CUSTOMERS,
                                        orders=data.ORDERS))
            {1: {'email': 'evorsoisson@komarr.net',
                 'name': 'Ekaterin Vorsoisson',
                 'orders': 3,
                 'total': 1287},
             2: {'email': 'cordelia@beta.com',
                 'name': 'Cordelia Naismith',
                 'orders': 5,
                 'total': 2778},
             3: {'email': 'iv398@barrayar.net',
                 'name': 'Ivan Vorpatril',
                 'orders': 3,
                 'total': 358}}
    """
    customersummary = {}
    for customerid, customerdata in customers.iteritems():
        ordertotal = 0
        ordercount = 0
        for ordervalues in orders.itervalues():
            if customerid in (ordervalues['customer_id'],):
                ordertotal += ordervalues['total']
                ordercount += 1
                customersummary[customerid] = {'name': customerdata['name'],
                                               'email': customerdata['email'],
                                               'orders': ordercount,
                                               'total': ordertotal}
    return customersummary
