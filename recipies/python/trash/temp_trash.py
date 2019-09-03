
initial_contents = [cache_frange[0],cache_frange[1]]
close_choice = 1
choice,frange = hou.ui.readMultiInput(message="frame_range",buttons=("ok","cancel"),initial_contents=initial_contents,input_label=input_labels,close_choice=close_choice)

if not choice: cache_utils.makeDaily(n,frange)

for i ,(p, v) in enumerate(sorted(self.preferences.items(),key=operator.itemgetter(0) )):

	QtWidgets.QShortcut(QtGui.QKeySequence("Esc"),self,self.onClose)


items = (self,scrollLayout.itemsAt(i) for i in range(self.scrollLayout.count() ) )

85 
self.preferences[i.widget().text()] = int(i.widget().isChecked())

104
self.preferences = {names[x]:0 for x in range(0,len(names))}

25
if len(selNodes)>0 and mode ==1: