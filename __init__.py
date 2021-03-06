# This file is part of the stock_move_box module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .move import *
from .shipment import *

def register():
    Pool.register(
        Move,
        ShipmentIn,
        ShipmentOut,
        ShipmentOutReturn,
        module='stock_move_box', type_='model')
