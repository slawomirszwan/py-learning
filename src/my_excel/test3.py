"""

praca ze stylami

Styles can be applied to the following aspects:

font to set font size, color, underlining, etc.
fill to set a pattern or color gradient
border to set borders on a cell
cell alignment
protection

"""


"""
wartości domyslne 


>>> from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

>>> font = Font(name='Calibri',
...                 size=11,
...                 bold=False,
...                 italic=False,
...                 vertAlign=None,
...                 underline='none',
...                 strike=False,
...                 color='FF000000')

>>> fill = PatternFill(fill_type=None,
...                 start_color='FFFFFFFF',
...                 end_color='FF000000')

>>> border = Border(left=Side(border_style=None,
...                           color='FF000000'),
...                 right=Side(border_style=None,
...                            color='FF000000'),
...                 top=Side(border_style=None,
...                          color='FF000000'),
...                 bottom=Side(border_style=None,
...                             color='FF000000'),
...                 diagonal=Side(border_style=None,
...                               color='FF000000'),
...                 diagonal_direction=0,
...                 outline=Side(border_style=None,
...                              color='FF000000'),
...                 vertical=Side(border_style=None,
...                               color='FF000000'),
...                 horizontal=Side(border_style=None,
...                                color='FF000000')
...                )

>>> alignment=Alignment(horizontal='general',
...                     vertical='bottom',
...                     text_rotation=0,
...                     wrap_text=False,
...                     shrink_to_fit=False,
...                     indent=0)
>>> number_format = 'General'
>>> protection = Protection(locked=True,
...                         hidden=False)
>>>
"""




"""
cell styles


styl jest współdzielony między kmórkami i obiektami
raz ustawiony nie może byc zmieniany

więc przypisanie stylu do komórek a potem jego zmiana aby zmiany zastosować na innych komórkach się nie uda

trzeba stworzyć nowy styl i przypisac go do komórek


>>> from openpyxl.styles import colors
>>> from openpyxl.styles import Font, Color
>>> from openpyxl import Workbook
>>> wb = Workbook()
>>> ws = wb.active
>>>
>>> a1 = ws['A1']
>>> d4 = ws['D4']
>>> ft = Font(color="FF0000")
>>> a1.font = ft
>>> d4.font = ft
>>>
>>> a1.font.italic = True # is not allowed # doctest: +SKIP
>>>
>>> # If you want to change the color of a Font, you need to reassign it::
>>>
>>> a1.font = Font(color="FF0000", italic=True) # the change only affects A1
"""





"""
kopiowanie stylu 


>> from openpyxl.styles import Font
>>> from copy import copy
>>>
>>> ft1 = Font(name='Arial', size=14)
>>> ft2 = copy(ft1)
>>> ft2.name = "Tahoma"
>>> ft1.name
'Arial'
>>> ft2.name
'Tahoma'
>>> ft2.size # copied from the
14.0

skopiowanie i modyfikacja
"""



"""
kolory

>>> from openpyxl.styles import Font
>>> font = Font(color="FF0000")

>>> font.color.rgb
'0000FF00'
"""


"""
colory wg indeksu kolorów 
>>> from openpyxl.styles.colors import Color
>>> c = Color(indexed=32)
>>> c = Color(theme=6, tint=0.5)
"""



"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!
style sa stosowane bezpośrednio do komórek

>>> from openpyxl.workbook import Workbook
>>> from openpyxl.styles import Font, Fill
>>> wb = Workbook()
>>> ws = wb.active
>>> c = ws['A1']
>>> c.font = Font(size=12)


moga być stosowane do kolumn lub wierszy

>>> col = ws.column_dimensions['A']
>>> col.font = Font(bold=True)
>>> row = ws.row_dimensions[1]
>>> row.font = Font(underline="single")


"""












"""
komórki połączone 

>>> from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
>>> from openpyxl import Workbook
>>>
>>> wb = Workbook()
>>> ws = wb.active
>>> ws.merge_cells('B2:F4')
>>>
>>> top_left_cell = ws['B2']
>>> top_left_cell.value = "My Cell"
>>>
>>> thin = Side(border_style="thin", color="000000")
>>> double = Side(border_style="double", color="ff0000")
>>>
>>> top_left_cell.border = Border(top=double, left=thin, right=thin, bottom=double)
>>> top_left_cell.fill = PatternFill("solid", fgColor="DDDDDD")
>>> top_left_cell.fill = fill = GradientFill(stop=("000000", "FFFFFF"))
>>> top_left_cell.font  = Font(b=True, color="FF0000")
>>> top_left_cell.alignment = Alignment(horizontal="center", vertical="center")
>>>
>>> wb.save("styled.xlsx")












format numeryczny

>>> import datetime
>>> from openpyxl import Workbook

>>> wb = Workbook()
>>> ws = wb.active
>>> # set date using a Python datetime
>>> ws['A1'] = datetime.datetime(2010, 7, 21)
>>>
>>> ws['A1'].number_format
'yyyy-mm-dd h:mm:ss'
>>>
>>> ws["A2"] = 0.123456
>>> ws["A2"].number_format = "0.00" # Display to 2dp
"""




"""
ustawienie strony

>>> from openpyxl.workbook import Workbook
>>>
>>> wb = Workbook()
>>> ws = wb.active
>>>
>>> ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
>>> ws.page_setup.paperSize = ws.PAPERSIZE_TABLOID
>>> ws.page_setup.fitToHeight = 0
>>> ws.page_setup.fitToWidth = 1
"""












"""
style nazwane 

.........................................
........................................
"""


