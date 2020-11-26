import json

texto = """

[{
    "id": 5677240,
    "name": "Cønjuntø de Pænelæs æntiæderentes ¢øm 05 Peçæs Pæris",
    "quantity": 21,
    "price": "192.84",
    "category": "Panelas"
  },
  {
    "id": 9628920,
    "name": "Lævæ & Se¢æ 10,2 Kg Sæmsung E¢ø ßußßle ßræn¢æ ¢øm 09 Prøgræmæs de Lævægem",
    "quantity": 57,
    "price": 3719.70,
    "category": "Eletrodomésticos"
  },
  {
    "id": 1316334,
    "name": "Refrigerædør ßøttøm Freezer Ele¢trølux de 02 Pørtæs Frøst Free ¢øm 598 Litrøs",
    "quantity": 12,
    "price": 3880.23,
    "category": "Eletrodomésticos"
  },
  {
    "id": 6502394,
    "name": "Føgãø de Pisø Ele¢trølux de 04 ßø¢æs, Mesæ de Vidrø Prætæ",
    "quantity": 37,
    "price": "1419",
    "category": "Eletrodomésticos"
  },
  {
    "id": 9576720,
    "name": "Førnø Mi¢rø-øndæs Pænæsøni¢ ¢øm ¢æpæ¢idæde de 21 Litrøs ßræn¢ø",
    "quantity": 13,
    "price": "358.77",
    "category": "Eletrodomésticos"
  },
  {
    "id": 8875900,
    "name": "Smært TV 4K Søny LED 65” 4K X-Reælity Prø, UpS¢ælling, Møtiønfløw XR 240 e Wi-F",
    "quantity": 0,
    "price": 5799.42,
    "category": "Eletrônicos"
  },
  {
    "id": 9746439,
    "name": "Høme Theæter LG ¢øm ßlu-ræy 3D, 5.1 ¢ænæis e 1000W",
    "quantity": 80,
    "price": 2199,
    "category": "Eletrônicos"
  },
  {
    "id": 2162952,
    "name": "Kit Gæmer æ¢er - Nøteßøøk + Heædset + Møuse",
    "price": "25599.00",
    "category": "Eletrônicos"
  },
  {
    "id": 3500957,
    "name": "Mønitør 29 LG FHD Ultræwide ¢øm 1000:1 de ¢øntræste",
    "quantity": 18,
    "price": 1559.40,
    "category": "Eletrônicos"
  },
  {
    "id": 1911864,
    "name": "Møuse Gæmer Predætør ¢estus 510 Føx Pretø",
    "price": "699",
    "category": "Acessórios"
  }
]
"""


def escrever_json(dados):
    with open('BrokenDatabase.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=5, separators=(',', ':'))


def ler_json(brokendatabase_json):
    with open(brokendatabase_json, 'r', encoding='utf8') as f:
        return json.load(f)


lista_categoria = ["Panelas", "Eletrodomésticos", "Eletrônicos", "Acessórios"]
lista_alfabetica = sorted(lista_categoria)
print(lista_alfabetica)

j = json.loads('{"name": "Møuse Gæmer Predætør ¢estus 510 Føx Pretø", "quantity": 0, "price": 699, "id": 1911864, '
               '"category": '
               '"Acessórios"}')
if 'name': "Møuse Gæmer Predætør ¢estus 510 Føx Pretø"
categoria = ["Acessórios"]
print(categoria)
id = 1911864
print(id)
print("Mouse Gamer Predator cestus 510 Fox Preto")
AC = 699

j = json.loads(
    '{"name": "Refrigerædør ßøttøm Freezer Ele¢trølux de 02 Pørtæs Frøst Free ¢øm 598 Litrøs", "quantity": 12, '
    '"price": 3880.23, '
    '"id": 1316334, "category": "Eletrodomésticos"}')
if 'name': "Refrigerædør ßøttøm Freezer Ele¢trølux de 02 Pørtæs Frøst Free ¢øm 598 Litrøs"
categoria = ["Eletrodomésticos"]
print(categoria)
id = 1316334
print(id)
print("Refrigerador Bottom Freezer Electrolux de 02 Portas Frost Free com 598 Litros")
ELETROD1 = 3880.23

j = json.loads('{"name": "Føgãø de Pisø Ele¢trølux de 04 ßø¢æs, Mesæ de Vidrø Prætæ", "quantity": 37, "price": 1419, '
               '"id": 6502394, '
               '"category": "Eletrodomésticos"}')
if 'name': "Føgãø de Pisø Ele¢trølux de 04 ßø¢æs, Mesæ de Vidrø Prætæ"
categoria = ["Eletrodomésticos"]
print(categoria)
id = 6502394
print(id)
print("Fogão de Piso Electrolux de 04 Bocas, Mesa de Vidro Prata")
ELETROD2 = 1419

j = json.loads('{"name": "Førnø Mi¢rø-øndæs Pænæsøni¢ ¢øm ¢æpæ¢idæde de 21 Litrøs ßræn¢ø", "quantity": 13, '
               '"price": 358.77, '
               '"id": 9576720, "category": "Eletrodomésticos"}')
if 'name': "Førnø Mi¢rø-øndæs Pænæsøni¢ ¢øm ¢æpæ¢idæde de 21 Litrøs ßræn¢ø"
categoria = ["Eletrodomésticos"]
print(categoria)
id = 9576720
print(id)
print("Forno Micro-ondas Panasonic com capacidade de 21 Litros Branco")
ELETROD3 = 358.77

j = json.loads(
    '{"name": "Lævæ & Se¢æ 10,2 Kg Sæmsung E¢ø ßußßle ßræn¢æ ¢øm 09 Prøgræmæs de Lævægem", "quantity": 57, '
    '"price": 3719.70, '
    '"id": 9628920, "category": "Eletrodomésticos"}')
if 'name': "Lævæ & Se¢æ 10,2 Kg Sæmsung E¢ø ßußßle ßræn¢æ ¢øm 09 Prøgræmæs de Lævægem"
categoria = ["Eletrodomésticos"]
print(categoria)
id = 9628920
print(id)
print("Lava & Seca 10,2 Kg Samsung Eco Bubble Branco com 09 Programas de Lavagem")
ELETROD4 = 3719.70

j = json.loads('{"name": "Kit Gæmer æ¢er - Nøteßøøk + Heædset + Møuse", "quantity": 0, "price": 25599.00, '
               '"id": 2162952, '
               '"category": "Eletrônicos"}')
if 'name': "Kit Gæmer æ¢er - Nøteßøøk + Heædset + Møuse"
categoria = ["Eletrônicos"]
print(categoria)
id = 2162952
print(id)
print("Kit Gamer acer - Notebook + Headset + Mouse")
ELETRO1 = 25599.00

j = json.loads('{"name": "Mønitør 29 LG FHD Ultræwide ¢øm 1000:1 de ¢øntræste", "quantity": 18, "price": 1559.40, '
               '"id": 3500957, '
               '"category": "Eletrônicos"}')
if 'name': "Mønitør 29 LG FHD Ultræwide ¢øm 1000:1 de ¢øntræste"
categoria = ["Eletrônicos"]
print(categoria)
id = 3500957
print(id)
print("Monitor 29 LG FHD Ultrawide com 1000:1 de contraste")
ELETRO2 = 1559.40

j = json.loads(
    '{"name": "Smært TV 4K Søny LED 65” 4K X-Reælity Prø, UpS¢ælling, Møtiønfløw XR 240 e Wi-F", "quantity": 0, '
    '"price": 5799.42, '
    '"id": 8875900, "category": "Eletrônicos"}')
if 'name': "Smært TV 4K Søny LED 65” 4K X-Reælity Prø, UpS¢ælling, Møtiønfløw XR 240 e Wi-F"
categoria = ["Eletrônicos"]
print(categoria)
id = 8875900
print(id)
print("Smart TV 4K Sony LED 65” 4K X-Reality Pro, UpScalling, Motionflow XR 240 e Wi-F")
ELETRO3 = 5799.42

j = json.loads('{"name": "Høme Theæter LG ¢øm ßlu-ræy 3D, 5.1 ¢ænæis e 1000W", "quantity": 80, "price": 2199, '
               '"id": 9746439, '
               '"category": "Eletrônicos"}')
if 'name': "Høme Theæter LG ¢øm ßlu-ræy 3D, 5.1 ¢ænæis e 1000W"
categoria = ["Eletrônicos"]
print(categoria)
id = 9746439
print(id)
print("Home Theater LG com Blu-ray 3D, 5.1 canais e 1000W")
ELETRO4 = 2199

j = json.loads('{"name": "Cønjuntø de Pænelæs æntiæderentes ¢øm 05 Peçæs Pæris", "quantity": 21, "price": 192.84, '
               '"id": 5677240, '
               '"category": "Panelas"}')
if 'name': "Cønjuntø de Pænelæs æntiæderentes ¢øm 05 Peçæs Pæris"
categoria = ["Panelas"]
print(categoria)
id = 5677240
print(id)
print("Conjunto de Panelas antiaderentes com 05 Peçs Paris")
PAN = 192.84

def escrever_json(lista):
    with open('saida.json', 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open('saida.json', 'r') as f:
        return json.load(f)

ACESSORIOS = (AC*0)
ELETRODOMESTICOS = (ELETRO1*12)+(ELETROD2*37)+(ELETROD3*13)+(ELETROD4*57)
ELETRONICOS = (ELETRO1*0)+(ELETRO2*18)+(ELETRO3*0)+(ELETRO4*80)
PANELAS = (PAN*21)

ACE = ("O valor total do estoque de acessórios é %d" % ACESSORIOS)
ELETD = ("O valor total do estoque de eletrodomésticos é %d" % ELETRODOMESTICOS)
ELETR = ("O valor total do estoque de eletrônicos é %d" % ELETRONICOS)
PANE = ("O valor total do estoque de panelas é %d" % PANELAS)

TOTAL = (ACE, ELETD, ELETR, PANE)
escrever_json(TOTAL)

print(carregar_json('saida.json'))