from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    
    self.label_direktor.text = anvil.server.call('get_direktor') 
    self.label_freie_zellen.text = anvil.server.call('get_zelle') 
    zellennummeranzahl = anvil.server.call('get_zellennummer')
    print(zellennummeranzahl)
    for x in range(len(zellennummeranzahl)):
      print(zellennummeranzahl[x][0])
      self.repeating_zellen.items = [{'zellennummer': zellennummeranzahl[x][0], 'anzahl_häftlinge': 'TODO'}]

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
   
    self.label_direktor.text = anvil.server.call('get_dirketor_chance', self.gefaengnisse_drop_down.selected_value) 
    self.label_freie_zellen.text = anvil.server.call('get_zelle_chance', self.gefaengnisse_drop_down.selected_value) 


    

 



  
 
