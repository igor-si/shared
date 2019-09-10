==========callback resimulate this network============================
hou.parm(kwargs["node"].parent().path()+"/resimulate").pressButton()
=============================================================

==========callback to run code from string multiparm============================
n=hou.pwd();exec(n.evalParm("codeMain"));linkVersion(kwargs["[parm"])
=============================================================

	