import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Name, GID FROM Gefaengnisse"))
  conn.close()
  return res

@anvil.server.callable
def get_gefaengnisseid():
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Name, GID FROM Gefaengnisse"))
  conn.close()
  return res


@anvil.server.callable
def get_direktor():
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Direktor, VID FROM Verwaltungen"))
  conn.close()
  return res[0][0]

@anvil.server.callable
def get_dirketor_chance(gid):
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Direktor, VID FROM Verwaltungen"))
  conn.close()
  print(gid)
  return res[gid-1][0]

@anvil.server.callable
def get_zelle():
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Freie_Zellen, VID FROM Verwaltungen"))
  conn.close()
  return res[0][0]

@anvil.server.callable
def get_zelle_chance(gid):
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Freie_Zellen, VID FROM Verwaltungen"))
  conn.close()
  print(gid)
  return res[gid-1][0]

@anvil.server.callable
def get_zellennummer():
  conn = sqlite3.connect(data_files["gefangnis.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("SELECT Zellennummer, ZID FROM Zellen"))
  conn.close()
  print(res)
  return res


