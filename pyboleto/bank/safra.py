# -*- coding: utf-8 -*-
"""
    pyboleto.bank.bradesco
    ~~~~~~~~~~~~~~~~~~~~~~

    Lógica para boletos do banco Safra.

    :copyright: © 2022 by Patrick Freitas
    :license: BSD, see LICENSE for more details.
"""
from pyboleto.data import BoletoData, CustomProperty


class BoletoSafra(BoletoData):
    """Estrutura de dados para criação de boleto para o banco Safra"""

    nosso_numero = CustomProperty('nosso_numero', 9)
    agencia_cedente = CustomProperty('agencia_cedente', 4)
    agencia_cedente_d = CustomProperty('agencia_cedente_dv', 1)
    conta_cedente = CustomProperty('conta_cedente', 9)

    def __init__(self, **kwargs):
        super(BoletoSafra, self).__init__(**kwargs)
        self.codigo_banco = '422'
        self.logo_image = 'logo_safra.png'
        self.carteira = '1'
        self.local_pagamento = 'Pagável em qualquer banco até o vencimento'

    def format_nosso_numero(self):
        return f'{self.nosso_numero[:-1]}-{self.nosso_numero[-1]}'

    @property
    def agencia_conta_cedente(self):
        return "%s-%s/%s-%s" % (
            self.agencia_cedente,
            self.agencia_cedente_d,
            self.conta_cedente.lstrip('0'),
            self.conta_cedente_dv,
        )

    @property
    def campo_livre(self):
        content = '{0:.1}{1:.5}{2:.9}{3:.9}{4:.1}'.format(
            '7',
            f'{self.agencia_cedente:0<5}',  # increase 0 at right complete 5 digits
            f'{self.conta_cedente}{self.conta_cedente_dv}'.zfill(9)[-9:],
            self.nosso_numero.zfill(9),
            '2',
        )
        return content
