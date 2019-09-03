import hou
n = hou.node('/obj/geo1/null1')

print "\n"*10
def check():
    parms = [x for x in n.parms() if x.isVisible() ] # and x.name() in ["parm2_1value","testint"] ]
    for p in parms:
        pname = p.name()
        pTempl = p.parmTemplate().type().name()
        prawVal = p.rawValue()
        val = None
        def checkExpr():
            try: 
                k = p.expression()
                return True
            except: return False
        expr = checkExpr()
        
        def checkUndexpandedString():
            try: 
                k = p.unexpandedString()
                return True
            except: return False
        unexp = checkUndexpandedString()
        #val = p.rawValue()
        if pTempl == "Ramp": 
            ev = p.evalAsRamp()
            val = {"values":ev.values(),
                    "keys":ev.keys(),
                    "isColor":ev.isColor(),
                    "basis":ev.basis()}
        elif(expr or unexp):
            if (expr):val = p.expression()
            if (unexp):val = p.unexpandedString()
        else:
            val = p.eval()
            if isinstance(val, float): val = round(val,4)
        
        data = {pname: 
                    {
                    "templ":pTempl,
                    "val":val,
                    "expr":expr,
                    "unexp":unexp
                    }
                }
        for p in parms:
            print p.name(),p.eval()
        
check() 
