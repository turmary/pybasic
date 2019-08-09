
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOLONleftCOMMAleftANDORleftEQUALSNOT_EQUALGREATER_THANLESS_THANEQUAL_GREATER_THANEQUAL_LESS_THANleftASleftPLUSMINUSleftTIMESDIVIDEMODleftEXPrightUMINUSNOTleftDOTAND AS COLON COMMA CONTINUE DECIMAL DEFUN DIM DIVIDE DO DOT ELSE ELSEIF END EQUALS EQUAL_GREATER_THAN EQUAL_LESS_THAN EXACTDIV EXIT EXP FOR FUNCTION GREATER_THAN ID IF INTEGER LBRACE LESS_THAN LET LOOP LPAREN MINUS MOD NEXT NOT NOT_EQUAL OR PLUS RBRACE RETURN RPAREN STEP STRING SUB THEN TIMES TO UNTIL USE WEND WHILE\n    statement : statement COLON statement\n    \n    statement : assignment\n              | declaration\n              | funcall\n              | control\n              | return\n              | defun_statement\n    \n    statement : expression\n    \n    statement : block_begin\n    \n    statement : block_end\n    \n    statement : if_block_begin\n              | elseif_block_begin\n              | else_statement\n    \n    args_list : args_list COMMA expression\n              | expression\n    \n    params_list : params_list COMMA ID\n                | ID\n    \n    defun_statement : DEFUN ID LPAREN params_list RPAREN EQUALS expression\n    \n    funcall : ID args_list\n    \n    assignment : ID EQUALS expression\n               | LET ID EQUALS expression\n               | ID LPAREN expression RPAREN EQUALS expression\n               | expression DOT ID EQUALS expression\n    \n    declaration : declare_array\n    \n    declare_array : DIM ID LPAREN expression RPAREN AS ID\n    \n    rel_expression : expression GREATER_THAN expression\n                   | expression LESS_THAN expression\n                   | expression EQUAL_GREATER_THAN expression\n                   | expression EQUAL_LESS_THAN expression\n                   | expression EQUALS expression\n                   | expression NOT_EQUAL expression\n                   | rel_expression AND rel_expression\n                   | rel_expression OR rel_expression\n                   | LPAREN rel_expression RPAREN\n                   | NOT rel_expression\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression EXACTDIV expression\n               | expression MOD expression\n               | expression AS expression\n               | expression EXP expression\n               | expression DOT ID\n               | MINUS expression %prec UMINUS\n               | LPAREN expression RPAREN\n    \n    expression : ID LPAREN RPAREN\n               | ID LPAREN args_list RPAREN\n    \n    expression : INTEGER\n               | DECIMAL\n    \n    expression : STRING\n    \n    expression : ID\n    \n    expression : LBRACE args_list RBRACE\n    \n    block_begin : while_block_begin\n                | for_block_begin\n                | do_block_begin\n                | function_block_begin\n    \n    if_block_begin : IF rel_expression THEN\n    \n    else_statement : ELSE\n    \n    elseif_block_begin : ELSEIF rel_expression THEN\n    \n    while_block_begin : WHILE rel_expression\n    \n    do_block_begin : DO\n    \n    for_block_begin : FOR ID EQUALS expression TO expression\n                    | FOR ID EQUALS expression TO expression STEP expression\n    \n    function_block_begin : SUB ID LPAREN params_list RPAREN\n                         | FUNCTION ID LPAREN params_list RPAREN\n                         | SUB ID LPAREN RPAREN\n                         | FUNCTION ID LPAREN RPAREN\n    \n    block_end : END IF\n    \n    block_end : END WHILE\n              | WEND\n    \n    block_end : END FOR\n              | NEXT ID\n    \n    block_end : LOOP\n              | LOOP WHILE rel_expression\n              | LOOP UNTIL rel_expression\n    \n    block_end : END SUB\n              | END FUNCTION\n    \n    return : RETURN\n           | RETURN expression\n    \n    control : EXIT WHILE\n            | EXIT DO\n            | EXIT FOR\n    \n    control : CONTINUE WHILE\n            | CONTINUE DO\n            | CONTINUE FOR\n    \n    statement : USE ID\n    '
    
_lr_action_items = {'USE':([0,45,],[14,14,]),'ID':([0,14,15,16,17,20,22,24,25,26,30,36,38,40,41,42,44,45,46,47,48,49,50,51,52,53,54,57,59,68,69,85,86,101,103,107,108,110,111,112,113,114,115,116,117,121,122,127,128,130,131,155,156,158,164,166,167,],[15,55,56,61,56,56,70,56,75,56,56,56,84,87,88,56,90,15,92,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,132,56,56,56,56,56,56,56,56,56,56,56,147,147,147,56,56,56,56,165,56,169,56,]),'LET':([0,45,],[16,16,]),'EXIT':([0,45,],[19,19,]),'CONTINUE':([0,45,],[23,23,]),'RETURN':([0,45,],[24,24,]),'DEFUN':([0,45,],[25,25,]),'MINUS':([0,8,15,17,20,24,26,27,28,29,30,36,42,45,47,48,49,50,51,52,53,54,56,57,58,59,62,67,68,69,74,76,85,86,92,93,94,95,96,97,98,99,100,101,102,104,105,107,108,109,110,111,112,113,114,115,116,117,119,121,123,130,131,132,133,134,135,136,139,140,141,142,143,144,146,153,154,155,156,162,163,164,167,168,170,],[26,48,26,26,26,26,26,-49,-50,-51,26,26,26,26,26,26,26,26,26,26,26,26,-52,26,48,26,48,48,26,26,48,-45,26,26,-44,-36,-37,-38,-39,48,-41,48,-43,26,48,48,-47,26,26,-46,26,26,26,26,26,26,26,26,48,26,-53,26,26,-44,-46,-48,48,48,48,48,48,48,48,48,48,48,48,26,26,48,48,26,26,48,48,]),'LPAREN':([0,15,17,20,24,26,30,36,42,45,47,48,49,50,51,52,53,54,56,57,59,68,69,75,85,86,87,88,90,101,107,108,110,111,112,113,114,115,116,117,121,130,131,155,156,164,167,],[17,59,17,68,17,17,17,68,68,17,17,17,17,17,17,17,17,17,101,17,17,68,68,122,68,68,127,128,130,17,17,17,68,68,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'INTEGER':([0,15,17,20,24,26,30,36,42,45,47,48,49,50,51,52,53,54,57,59,68,69,85,86,101,107,108,110,111,112,113,114,115,116,117,121,130,131,155,156,164,167,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'DECIMAL':([0,15,17,20,24,26,30,36,42,45,47,48,49,50,51,52,53,54,57,59,68,69,85,86,101,107,108,110,111,112,113,114,115,116,117,121,130,131,155,156,164,167,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'STRING':([0,15,17,20,24,26,30,36,42,45,47,48,49,50,51,52,53,54,57,59,68,69,85,86,101,107,108,110,111,112,113,114,115,116,117,121,130,131,155,156,164,167,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'LBRACE':([0,15,17,20,24,26,30,36,42,45,47,48,49,50,51,52,53,54,57,59,68,69,85,86,101,107,108,110,111,112,113,114,115,116,117,121,130,131,155,156,164,167,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'END':([0,45,],[35,35,]),'WEND':([0,45,],[37,37,]),'NEXT':([0,45,],[38,38,]),'LOOP':([0,45,],[39,39,]),'IF':([0,35,45,],[36,78,36,]),'ELSEIF':([0,45,],[42,42,]),'ELSE':([0,45,],[43,43,]),'DIM':([0,45,],[44,44,]),'WHILE':([0,19,23,35,39,45,],[20,63,71,79,85,20,]),'FOR':([0,19,23,35,45,],[22,65,73,80,22,]),'DO':([0,19,23,45,],[21,64,72,21,]),'SUB':([0,35,45,],[40,81,40,]),'FUNCTION':([0,35,45,],[41,82,41,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,15,18,21,24,27,28,29,31,32,33,34,37,39,43,55,56,58,60,63,64,65,66,71,72,73,74,76,78,79,80,81,82,84,91,92,93,94,95,96,97,98,99,100,102,105,109,120,123,124,125,126,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,152,154,159,160,162,163,168,169,170,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-52,-24,-62,-79,-49,-50,-51,-54,-55,-56,-57,-71,-74,-59,-87,-52,-15,-19,-81,-82,-83,-61,-84,-85,-86,-80,-45,-69,-70,-72,-77,-78,-73,-1,-44,-36,-37,-38,-39,-40,-41,-42,-43,-20,-47,-46,-35,-53,-58,-75,-76,-60,-44,-46,-48,-14,-21,-32,-33,-26,-27,-28,-29,-30,-31,-34,-67,-68,-23,-65,-66,-22,-63,-18,-25,-64,]),'COLON':([1,2,3,4,5,6,7,8,9,10,11,12,13,15,18,21,24,27,28,29,31,32,33,34,37,39,43,55,56,58,60,63,64,65,66,71,72,73,74,76,78,79,80,81,82,84,91,92,93,94,95,96,97,98,99,100,102,105,109,120,123,124,125,126,129,132,133,134,135,136,137,138,139,140,141,142,143,144,145,150,152,154,159,160,162,163,168,169,170,],[45,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-52,-24,-62,-79,-49,-50,-51,-54,-55,-56,-57,-71,-74,-59,-87,-52,-15,-19,-81,-82,-83,-61,-84,-85,-86,-80,-45,-69,-70,-72,-77,-78,-73,-1,-44,-36,-37,-38,-39,-40,-41,-42,-43,-20,-47,-46,-35,-53,-58,-75,-76,-60,-44,-46,-48,-14,-21,-32,-33,-26,-27,-28,-29,-30,-31,-34,-67,-68,-23,-65,-66,-22,-63,-18,-25,-64,]),'DOT':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[46,-52,-49,-50,-51,-52,103,103,103,103,103,-44,103,103,103,103,103,103,103,103,103,103,-47,-46,103,-53,-44,-46,-48,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'PLUS':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[47,-52,-49,-50,-51,-52,47,47,47,47,-45,-44,-36,-37,-38,-39,47,-41,47,-43,47,47,-47,-46,47,-53,-44,-46,-48,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'TIMES':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[49,-52,-49,-50,-51,-52,49,49,49,49,-45,-44,49,49,-38,-39,49,-41,49,-43,49,49,-47,-46,49,-53,-44,-46,-48,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'DIVIDE':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[50,-52,-49,-50,-51,-52,50,50,50,50,-45,-44,50,50,-38,-39,50,-41,50,-43,50,50,-47,-46,50,-53,-44,-46,-48,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'EXACTDIV':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[51,-52,-49,-50,-51,-52,51,51,51,51,-45,-44,-36,-37,-38,-39,51,-41,-42,-43,51,51,-47,-46,51,-53,-44,-46,-48,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'MOD':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[52,-52,-49,-50,-51,-52,52,52,52,52,-45,-44,52,52,-38,-39,52,-41,52,-43,52,52,-47,-46,52,-53,-44,-46,-48,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'AS':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,161,162,163,168,170,],[53,-52,-49,-50,-51,-52,53,53,53,53,-45,-44,-36,-37,-38,-39,53,-41,-42,-43,53,53,-47,-46,53,-53,-44,-46,-48,53,53,53,53,53,53,53,53,53,53,53,166,53,53,53,53,]),'EXP':([8,15,27,28,29,56,58,62,67,74,76,92,93,94,95,96,97,98,99,100,102,104,105,109,119,123,132,133,134,135,136,139,140,141,142,143,144,146,153,154,162,163,168,170,],[54,-52,-49,-50,-51,-52,54,54,54,54,-45,-44,54,54,54,54,54,54,54,-43,54,54,-47,-46,54,-53,-44,-46,-48,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'EQUALS':([15,27,28,29,56,61,67,70,76,92,93,94,95,96,97,98,99,100,105,109,119,123,132,133,134,157,],[57,-49,-50,-51,-52,108,116,121,-45,131,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,116,-53,-44,155,-48,164,]),'NOT':([20,36,42,68,69,85,86,110,111,],[69,69,69,69,69,69,69,69,69,]),'COMMA':([27,28,29,56,58,60,76,77,93,94,95,96,97,98,99,100,104,105,106,109,123,132,133,134,135,147,148,149,151,165,],[-49,-50,-51,-52,-15,107,-45,107,-36,-37,-38,-39,-40,-41,-42,-43,-15,-47,107,-46,-53,-44,-46,-48,-14,-17,158,158,158,-16,]),'RPAREN':([27,28,29,56,58,59,62,76,93,94,95,96,97,98,99,100,101,104,105,106,109,118,119,120,123,127,128,132,134,135,137,138,139,140,141,142,143,144,145,147,148,149,151,153,165,],[-49,-50,-51,-52,-15,105,109,-45,-36,-37,-38,-39,-40,-41,-42,-43,105,133,-47,134,-46,145,109,-35,-53,150,152,-44,-48,-14,-32,-33,-26,-27,-28,-29,-30,-31,-34,-17,157,159,160,161,-16,]),'GREATER_THAN':([27,28,29,56,67,76,93,94,95,96,97,98,99,100,105,109,119,123,132,134,],[-49,-50,-51,-52,112,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,112,-53,-44,-48,]),'LESS_THAN':([27,28,29,56,67,76,93,94,95,96,97,98,99,100,105,109,119,123,132,134,],[-49,-50,-51,-52,113,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,113,-53,-44,-48,]),'EQUAL_GREATER_THAN':([27,28,29,56,67,76,93,94,95,96,97,98,99,100,105,109,119,123,132,134,],[-49,-50,-51,-52,114,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,114,-53,-44,-48,]),'EQUAL_LESS_THAN':([27,28,29,56,67,76,93,94,95,96,97,98,99,100,105,109,119,123,132,134,],[-49,-50,-51,-52,115,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,115,-53,-44,-48,]),'NOT_EQUAL':([27,28,29,56,67,76,93,94,95,96,97,98,99,100,105,109,119,123,132,134,],[-49,-50,-51,-52,117,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,117,-53,-44,-48,]),'RBRACE':([27,28,29,56,58,76,77,93,94,95,96,97,98,99,100,105,109,123,132,134,135,],[-49,-50,-51,-52,-15,-45,123,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,-53,-44,-48,-14,]),'AND':([27,28,29,56,66,76,83,89,93,94,95,96,97,98,99,100,105,109,118,120,123,125,126,132,134,137,138,139,140,141,142,143,144,145,],[-49,-50,-51,-52,110,-45,110,110,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,110,-35,-53,110,110,-44,-48,-32,-33,-26,-27,-28,-29,-30,-31,-34,]),'OR':([27,28,29,56,66,76,83,89,93,94,95,96,97,98,99,100,105,109,118,120,123,125,126,132,134,137,138,139,140,141,142,143,144,145,],[-49,-50,-51,-52,111,-45,111,111,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,111,-35,-53,111,111,-44,-48,-32,-33,-26,-27,-28,-29,-30,-31,-34,]),'THEN':([27,28,29,56,76,83,89,93,94,95,96,97,98,99,100,105,109,120,123,132,134,137,138,139,140,141,142,143,144,145,],[-49,-50,-51,-52,-45,124,129,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,-35,-53,-44,-48,-32,-33,-26,-27,-28,-29,-30,-31,-34,]),'TO':([27,28,29,56,76,93,94,95,96,97,98,99,100,105,109,123,132,134,146,],[-49,-50,-51,-52,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,-53,-44,-48,156,]),'STEP':([27,28,29,56,76,93,94,95,96,97,98,99,100,105,109,123,132,134,163,],[-49,-50,-51,-52,-45,-36,-37,-38,-39,-40,-41,-42,-43,-47,-46,-53,-44,-48,167,]),'UNTIL':([39,],[86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,45,],[1,91,]),'assignment':([0,45,],[2,2,]),'declaration':([0,45,],[3,3,]),'funcall':([0,45,],[4,4,]),'control':([0,45,],[5,5,]),'return':([0,45,],[6,6,]),'defun_statement':([0,45,],[7,7,]),'expression':([0,15,17,20,24,26,30,36,42,45,47,48,49,50,51,52,53,54,57,59,68,69,85,86,101,107,108,110,111,112,113,114,115,116,117,121,130,131,155,156,164,167,],[8,58,62,67,74,76,58,67,67,8,93,94,95,96,97,98,99,100,102,104,119,67,67,67,58,135,136,67,67,139,140,141,142,143,144,146,153,154,162,163,168,170,]),'block_begin':([0,45,],[9,9,]),'block_end':([0,45,],[10,10,]),'if_block_begin':([0,45,],[11,11,]),'elseif_block_begin':([0,45,],[12,12,]),'else_statement':([0,45,],[13,13,]),'declare_array':([0,45,],[18,18,]),'while_block_begin':([0,45,],[31,31,]),'for_block_begin':([0,45,],[32,32,]),'do_block_begin':([0,45,],[33,33,]),'function_block_begin':([0,45,],[34,34,]),'args_list':([15,30,59,101,],[60,77,106,106,]),'rel_expression':([20,36,42,68,69,85,86,110,111,],[66,83,89,118,120,125,126,137,138,]),'params_list':([122,127,128,],[148,149,151,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement COLON statement','statement',3,'p_multi_statement','basic_yacc.py',33),
  ('statement -> assignment','statement',1,'p_singleline_statement','basic_yacc.py',41),
  ('statement -> declaration','statement',1,'p_singleline_statement','basic_yacc.py',42),
  ('statement -> funcall','statement',1,'p_singleline_statement','basic_yacc.py',43),
  ('statement -> control','statement',1,'p_singleline_statement','basic_yacc.py',44),
  ('statement -> return','statement',1,'p_singleline_statement','basic_yacc.py',45),
  ('statement -> defun_statement','statement',1,'p_singleline_statement','basic_yacc.py',46),
  ('statement -> expression','statement',1,'p_expression','basic_yacc.py',54),
  ('statement -> block_begin','statement',1,'p_multiline_begin_statement','basic_yacc.py',62),
  ('statement -> block_end','statement',1,'p_multiline_end_statement','basic_yacc.py',71),
  ('statement -> if_block_begin','statement',1,'p_if_else_elseif','basic_yacc.py',78),
  ('statement -> elseif_block_begin','statement',1,'p_if_else_elseif','basic_yacc.py',79),
  ('statement -> else_statement','statement',1,'p_if_else_elseif','basic_yacc.py',80),
  ('args_list -> args_list COMMA expression','args_list',3,'p_args_list','basic_yacc.py',86),
  ('args_list -> expression','args_list',1,'p_args_list','basic_yacc.py',87),
  ('params_list -> params_list COMMA ID','params_list',3,'p_param_list','basic_yacc.py',97),
  ('params_list -> ID','params_list',1,'p_param_list','basic_yacc.py',98),
  ('defun_statement -> DEFUN ID LPAREN params_list RPAREN EQUALS expression','defun_statement',7,'p_defun','basic_yacc.py',108),
  ('funcall -> ID args_list','funcall',2,'p_funcall','basic_yacc.py',123),
  ('assignment -> ID EQUALS expression','assignment',3,'p_assignment','basic_yacc.py',130),
  ('assignment -> LET ID EQUALS expression','assignment',4,'p_assignment','basic_yacc.py',131),
  ('assignment -> ID LPAREN expression RPAREN EQUALS expression','assignment',6,'p_assignment','basic_yacc.py',132),
  ('assignment -> expression DOT ID EQUALS expression','assignment',5,'p_assignment','basic_yacc.py',133),
  ('declaration -> declare_array','declaration',1,'p_declare','basic_yacc.py',146),
  ('declare_array -> DIM ID LPAREN expression RPAREN AS ID','declare_array',7,'p_declare_array','basic_yacc.py',152),
  ('rel_expression -> expression GREATER_THAN expression','rel_expression',3,'p_rel_expression','basic_yacc.py',158),
  ('rel_expression -> expression LESS_THAN expression','rel_expression',3,'p_rel_expression','basic_yacc.py',159),
  ('rel_expression -> expression EQUAL_GREATER_THAN expression','rel_expression',3,'p_rel_expression','basic_yacc.py',160),
  ('rel_expression -> expression EQUAL_LESS_THAN expression','rel_expression',3,'p_rel_expression','basic_yacc.py',161),
  ('rel_expression -> expression EQUALS expression','rel_expression',3,'p_rel_expression','basic_yacc.py',162),
  ('rel_expression -> expression NOT_EQUAL expression','rel_expression',3,'p_rel_expression','basic_yacc.py',163),
  ('rel_expression -> rel_expression AND rel_expression','rel_expression',3,'p_rel_expression','basic_yacc.py',164),
  ('rel_expression -> rel_expression OR rel_expression','rel_expression',3,'p_rel_expression','basic_yacc.py',165),
  ('rel_expression -> LPAREN rel_expression RPAREN','rel_expression',3,'p_rel_expression','basic_yacc.py',166),
  ('rel_expression -> NOT rel_expression','rel_expression',2,'p_rel_expression','basic_yacc.py',167),
  ('expression -> expression PLUS expression','expression',3,'p_expression_calc','basic_yacc.py',192),
  ('expression -> expression MINUS expression','expression',3,'p_expression_calc','basic_yacc.py',193),
  ('expression -> expression TIMES expression','expression',3,'p_expression_calc','basic_yacc.py',194),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_calc','basic_yacc.py',195),
  ('expression -> expression EXACTDIV expression','expression',3,'p_expression_calc','basic_yacc.py',196),
  ('expression -> expression MOD expression','expression',3,'p_expression_calc','basic_yacc.py',197),
  ('expression -> expression AS expression','expression',3,'p_expression_calc','basic_yacc.py',198),
  ('expression -> expression EXP expression','expression',3,'p_expression_calc','basic_yacc.py',199),
  ('expression -> expression DOT ID','expression',3,'p_expression_calc','basic_yacc.py',200),
  ('expression -> MINUS expression','expression',2,'p_expression_calc','basic_yacc.py',201),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_calc','basic_yacc.py',202),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_inline_funcall','basic_yacc.py',231),
  ('expression -> ID LPAREN args_list RPAREN','expression',4,'p_inline_funcall','basic_yacc.py',232),
  ('expression -> INTEGER','expression',1,'p_expression_number','basic_yacc.py',242),
  ('expression -> DECIMAL','expression',1,'p_expression_number','basic_yacc.py',243),
  ('expression -> STRING','expression',1,'p_expression_string','basic_yacc.py',249),
  ('expression -> ID','expression',1,'p_expression_id','basic_yacc.py',255),
  ('expression -> LBRACE args_list RBRACE','expression',3,'p_expression_array','basic_yacc.py',261),
  ('block_begin -> while_block_begin','block_begin',1,'p_block_begin','basic_yacc.py',268),
  ('block_begin -> for_block_begin','block_begin',1,'p_block_begin','basic_yacc.py',269),
  ('block_begin -> do_block_begin','block_begin',1,'p_block_begin','basic_yacc.py',270),
  ('block_begin -> function_block_begin','block_begin',1,'p_block_begin','basic_yacc.py',271),
  ('if_block_begin -> IF rel_expression THEN','if_block_begin',3,'p_if_block_begin','basic_yacc.py',277),
  ('else_statement -> ELSE','else_statement',1,'p_else','basic_yacc.py',293),
  ('elseif_block_begin -> ELSEIF rel_expression THEN','elseif_block_begin',3,'p_elseif','basic_yacc.py',312),
  ('while_block_begin -> WHILE rel_expression','while_block_begin',2,'p_while_block_begin','basic_yacc.py',331),
  ('do_block_begin -> DO','do_block_begin',1,'p_do_block_begin','basic_yacc.py',342),
  ('for_block_begin -> FOR ID EQUALS expression TO expression','for_block_begin',6,'p_for_block_begin','basic_yacc.py',353),
  ('for_block_begin -> FOR ID EQUALS expression TO expression STEP expression','for_block_begin',8,'p_for_block_begin','basic_yacc.py',354),
  ('function_block_begin -> SUB ID LPAREN params_list RPAREN','function_block_begin',5,'p_function_block_begin','basic_yacc.py',368),
  ('function_block_begin -> FUNCTION ID LPAREN params_list RPAREN','function_block_begin',5,'p_function_block_begin','basic_yacc.py',369),
  ('function_block_begin -> SUB ID LPAREN RPAREN','function_block_begin',4,'p_function_block_begin','basic_yacc.py',370),
  ('function_block_begin -> FUNCTION ID LPAREN RPAREN','function_block_begin',4,'p_function_block_begin','basic_yacc.py',371),
  ('block_end -> END IF','block_end',2,'p_if_block_end','basic_yacc.py',381),
  ('block_end -> END WHILE','block_end',2,'p_while_block_end','basic_yacc.py',389),
  ('block_end -> WEND','block_end',1,'p_while_block_end','basic_yacc.py',390),
  ('block_end -> END FOR','block_end',2,'p_for_block_end','basic_yacc.py',398),
  ('block_end -> NEXT ID','block_end',2,'p_for_block_end','basic_yacc.py',399),
  ('block_end -> LOOP','block_end',1,'p_do_block_end','basic_yacc.py',410),
  ('block_end -> LOOP WHILE rel_expression','block_end',3,'p_do_block_end','basic_yacc.py',411),
  ('block_end -> LOOP UNTIL rel_expression','block_end',3,'p_do_block_end','basic_yacc.py',412),
  ('block_end -> END SUB','block_end',2,'p_function_block_end','basic_yacc.py',427),
  ('block_end -> END FUNCTION','block_end',2,'p_function_block_end','basic_yacc.py',428),
  ('return -> RETURN','return',1,'p_return','basic_yacc.py',437),
  ('return -> RETURN expression','return',2,'p_return','basic_yacc.py',438),
  ('control -> EXIT WHILE','control',2,'p_control_exit','basic_yacc.py',454),
  ('control -> EXIT DO','control',2,'p_control_exit','basic_yacc.py',455),
  ('control -> EXIT FOR','control',2,'p_control_exit','basic_yacc.py',456),
  ('control -> CONTINUE WHILE','control',2,'p_control_continue','basic_yacc.py',466),
  ('control -> CONTINUE DO','control',2,'p_control_continue','basic_yacc.py',467),
  ('control -> CONTINUE FOR','control',2,'p_control_continue','basic_yacc.py',468),
  ('statement -> USE ID','statement',2,'p_use_statement','basic_yacc.py',478),
]
