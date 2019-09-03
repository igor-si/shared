

# =============================================
# https://stackoverflow.com/questions/5150182/loop-over-widgets-in-pyqt-layout
items = (layout.itemAt(i) for i in range(layout.count())) 
for w in items:
   doSomething(w)

# I tried the first answer but I found that it returns 
# a WidgetItem type, so actually I did a revision:
widgets = (layout.itemAt(i).widget() for i in range(layout.count())) 
for widget in widgets:
   if isinstance(widget, QLineEdit):
        print "linedit: %s  - %s" %(widget.objectName(), widget.text())
   if isinstance(widget, QCheckBox):
        print "checkBox: %s  - %s" %(widget.objectName(), widget.checkState())
# ---------------------------------------------