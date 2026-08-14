#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Nathan Mazzaro, Dante Venga

import os 
import gi 
import math

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

pasta = os.path.dirname(os.path.abspath(__file__))
arquivo_interface = os.path.join(pasta, 'suor.glade')

fatores = {
    'Leve': 1.0,
    'Moderado': 1.15,
    'Intenso': 1.3
}

class Aplicacao:
    def __init__(self):
        self.construtor = Gtk.Builder()
        self.construtor.add_from_file(arquivo_interface)
        self.construtor.connect_signals(self)

        self.janela = self.construtor.get_object('jan_principal')

        self.pesos = self.construtor.get_object('spn_peso')
        self.cmb_atividade = self.construtor.get_object('cmb_atividade')
        temp = self.cmb_atividade.get_active()
        self.clima_quente = self.construtor.get_object('chk_clima')

        self.lbl_resposta = self.construtor.get_object('lbl_resultado')

        self.janela.show_all()

    def exit(self, componente=None, dados=None):
        Gtk.main_quit()

    def limpar(self, componente=None, dados=None):
        pass

    def calcular(self, componente=None, dados=None):
        peso = self.pesos.get_value()
        fator = list(fatores.values())[self.cmb_atividade.get_active()]
        clima = self.clima_quente.get_active()
        print(clima)

        if clima:
            meta_beber_ml = peso*fator*35*1.1
        else:
            meta_beber_ml = peso*fator*35

        meta_beber_l = meta_beber_ml / 1000
        copos = self.calcular_copos(meta_beber_ml)

        self.lbl_resposta.set_markup(f"<big><b>{meta_beber_l:.2f} L</b></big>\n cerca de {copos} copos de 200 ml")


    def calcular_copos(self, meta_ml):
        copos = math.ceil(meta_ml / 200)
        return copos



if __name__ == "__main__":
    Aplicacao()
    Gtk.main()
