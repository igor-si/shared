

# example 1
try:
    parm.expression()
except hou.OperationFailed:
    print('Not expression branch.')
else:
    print('Expression branch.')

# example 2
is_exp=False
raw = parm.unexpandedString()
if any(['`' in raw, '$' in raw, '(' in raw]):
    is_exp = True

