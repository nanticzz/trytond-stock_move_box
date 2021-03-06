# This file is part of the stock_move_box module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Move']


class Move:
    __metaclass__ = PoolMeta
    __name__ = 'stock.move'
    box = fields.Char('Box')

    @classmethod
    def __setup__(cls):
        super(Move, cls).__setup__()
        cls._order.insert(1, ('box', 'ASC'))
