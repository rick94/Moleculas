
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'F7D76AE963ECB2D9C334C8706BCF563A'
    
_lr_action_items = {'NUMBER':([8,],[10,]),'RCURL':([5,6,7,10,12,],[-3,-4,9,-5,-6,]),'LCURL':([1,3,],[4,-2,]),'BOND':([10,],[11,]),'MODEL':([0,],[3,]),'ELEMENT':([4,6,11,],[6,8,6,]),'$end':([2,9,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'A':([0,],[1,]),'S':([0,],[2,]),'B':([4,11,],[5,12,]),'L':([4,],[7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> A LCURL L RCURL','S',4,'p_model','MoleculeParser.py',65),
  ('A -> MODEL','A',1,'p_modeltype','MoleculeParser.py',71),
  ('L -> B','L',1,'p_list','MoleculeParser.py',75),
  ('B -> ELEMENT','B',1,'p_lone','MoleculeParser.py',80),
  ('B -> ELEMENT ELEMENT NUMBER','B',3,'p_central','MoleculeParser.py',89),
  ('B -> ELEMENT ELEMENT NUMBER BOND B','B',5,'p_centralBonded','MoleculeParser.py',113),
]
