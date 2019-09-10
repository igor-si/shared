

# ======= smooth shaded through python

'''Set geometry display mode for Houdini before version 16.0.'''

import hou
import toolutils

mode = 'shade'
display_set = 'display' # For display geometry inside SOP context.
viewport = '%s.%s.world' % (hou.ui.curDesktop().name(),
                            toolutils.sceneViewer().name())

command = 'viewdispset -s %s %s %s' % (mode, display_set, viewport)
hou.hscript(command)
#  ----------------------------------------


# Keyboard shortcut to toggle template visibility
import hou
import toolutils

# Toggle mechanism using session module.
tgd = hou.session.__dict__.get('templated_geo_display', 'on')
tgd = 'off' if tgd == 'on' else 'on'
hou.session.templated_geo_display = tgd

viewport = '%s.%s.world' % (hou.ui.curDesktop().name(),
                            toolutils.sceneViewer().name())

command = 'viewdisplay -T %s %s' % (tgd, viewport)
hou.hscript(command)
#  ----------------------------------------
