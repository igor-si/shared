"""
    riggingToolsUI.py: Allows the use of the createController and
    createCoordinatesSwitch functions from the CGCircuit tutorial's
    cgc_bipedRigTutorial script through a handy GUI.

    Requires the cgc_bipedRigTutorial file along with the
    Comet Cartoons scripts (http://comet-cartoons.com/maya.html).
    Pyside is also a requirement (you can download it to your Python 2.7
    installation through pip by running the command "python -m pip install
    pyside"). Pymel should already be installed with the most recent
    versions of Autodesk Maya.
"""
__author__ = "http://carlosmontesr.com"

from PySide.QtGui import *
from PySide import QtCore
import maya.OpenMayaUI as OpenMayaUI
import shiboken
import cgc_bipedRigTutorial as biped

try:
    import pymel.core as pmc

except ImportError:
    import maya.cmds as pmc

# Tuple containing the Comet controllers available
CTRLS = ("circleX", "circleY", "circleZ", "square", "cube", "sphere",
         "arrow", "cross", "orient", "bulb", "null", "locator",
         "plus", "joint")

# Override Colors (Hexadecimal values)
COLORS = ("000000", "404040", "808080", "9B0028", "000460", "0000FF",
          "004619", "260043", "C800C8", "8A4833", "3F231F", "992600",
          "FF0000", "00FF00", "004199", "FFFFFF", "FFFF00", "64DCFF",
          "43FFA3", "FFB0B0", "E4AC79", "FFFF63", "009954", "A16930",
          "9FA130", "68A130", "30A1A1", "3067A1", "6F30A1", "A13069")

# Stylesheet strings for the buttons at the left side
button_on = "background:#CCCCCC; color:#555555;"
button_off = "background:#555555; color:#CCCCCC;"

class RiggingToolsWindow(QMainWindow):

    def __init__(self, parent=None):
        """
        Interface constructor
        :param parent: Window that will parent this QWidget instance
        :return: None
        """

        super(RiggingToolsWindow, self).__init__(parent)

        # Create and set the container's central widget on the window
        main_container = QWidget(self)
        self.setCentralWidget(main_container)

        # Main Horizontal layout
        main_layout = QHBoxLayout()

        # =============== LEFT SIDE OF THE WINDOW ===============

        # Left side layout and its widgets
        left_side_layout = QVBoxLayout()

        self.create_control_button = new_button("Create Controller", 10)
        self.multiple_ctrls_button = new_button("Multiple Controllers", 10)
        self.space_switch_button = new_button("Space Switch", 10)

        options_layout = QHBoxLayout()
        options_layout.addWidget(new_label("Options:", 10))
        options_layout.setAlignment(QtCore.Qt.AlignHCenter)
        left_side_layout.addLayout(options_layout)
        add_space(left_side_layout, 0, 10)
        left_side_layout.addWidget(self.create_control_button)
        add_space(left_side_layout, 0, 10)
        left_side_layout.addWidget(self.multiple_ctrls_button)
        add_space(left_side_layout, 0, 10)
        left_side_layout.addWidget(self.space_switch_button)
        left_side_layout.addStretch(1)

        main_layout.addLayout(left_side_layout)
        add_space(main_layout, 20, 0)

        # =============== RIGHT SIDE OF THE WINDOW ================

        # Container layout for the right side
        self.right_side_layout = QVBoxLayout()

        # Frames that will hold the respective widgets, turn them off
        # CONTROLLER FRAME
        self.controller_frame = new_frame(main_container, (400, 300),
                                          "create_ctrl", True, True)
        self.controller_frame.setVisible(False)

        # MULTIPLE CONTROLLERS FRAME
        self.mult_ctrls_frame = new_frame(main_container, (400, 200),
                                          "create_ctrls", True, True)
        self.mult_ctrls_frame.setVisible(False)

        # SPACE SWITCH FRAME
        self.space_switch_frame = new_frame(main_container, (400, 500),
                                            "space_switch", True, True)
        self.space_switch_frame.setVisible(False)

        # Number of drivers (and attr names) in the QListWidgets
        self.no_drivers = 0

        # Instance widgets for the Create Controllers widget
        self.name_lineedit = new_line_edit(200, focus=True)
        self.opt_combo = new_combobox(c for c in CTRLS)
        self.side_combo = new_combobox(("None", "Left", "Right"))
        self.overr_color = new_combobox_color_choice(main_container, COLORS)
        self.con_checkbox = new_checkbox("Create CON node", True)
        self.sdk_checkbox = new_checkbox("Create SDK node", True)
        self.parent_checkbox = new_checkbox("Align to selection")
        self.create_button = new_button("Create Controller", 10)

        # Instance widgets for the Create Multiple Controllers widget
        self.m_opt_combo = new_combobox(c for c in CTRLS)
        self.m_overr_color = new_combobox_color_choice(main_container, COLORS)
        self.m_con_checkbox = new_checkbox("Create CON node", True)
        self.m_sdk_checkbox = new_checkbox("Create SDK node", True)
        self.m_parent_checkbox = new_checkbox("Align to selection")
        self.m_create_button = new_button("Create Controllers", 10)

        # Instance widgets for the Space Switch Coordinates
        self.driven_line = new_line_edit(150, focus=True)
        self.space_line = new_line_edit(150)
        self.driver_list = new_listwidget()
        self.attr_list = new_listwidget()
        self.const_combo = new_combobox(("Parent", "Orient", "Point"))
        self.ssside_combo = new_combobox(("None", "Left", "Right"))

        # Create the layouts for all frames
        self.create_controller_layout(self.right_side_layout)
        self.create_mult_ctrls_layout(self.right_side_layout)
        self.space_switch_layout(self.right_side_layout)
        self.right_side_layout.setAlignment(QtCore.Qt.AlignTop)

        # Fill the right side layout with Create Controller widgets by default
        self.create_controller_mode()
        main_layout.addLayout(self.right_side_layout)

        # ============ BUTTON CONNECTIONS ============

        self.connect(self.create_control_button,
                     QtCore.SIGNAL("clicked()"), self.create_controller_mode)
        self.connect(self.multiple_ctrls_button,
                     QtCore.SIGNAL("clicked()"), self.create_mult_ctrl_mode)
        self.connect(self.space_switch_button,
                     QtCore.SIGNAL("clicked()"), self.space_switch_mode)

        main_container.setLayout(main_layout)
        self.setWindowTitle("CGCircuit's Rigging Tools")
        self.setObjectName("riggingToolsUI")

    def add_driven(self):
        """
        Callback function to add the selected objects to the driven_line.
        :return: None
        """
        # Retrieve the last selected object
        try:
            selected = pmc.ls(sl=1)[-1:]
            self.driven_line.setText(selected[0].name())

        except IndexError:
            pass

    def add_driver_selection(self):
        """
        Callback function that adds the name of the selected objects in the
        scene to the driver and attr lists.
        :return: None
        """
        # Retrieve the current selection
        selected = pmc.ls(sl=1)

        if not selected:
            pass

        for item in selected:
            self.add_driver(item.name())

    def add_driver(self, text=""):
        """
        Adds an empty Widget list item to the driver list and Attr Names list.
        :return: None
        """
        # Raise the total no_drivers, just a visual aid for the user
        self.no_drivers += 1

        # Prepare a new widgetlistitem for the Driver list
        list_item = QListWidgetItem()
        list_item.setSizeHint(QtCore.QSize(0, 40))
        custom_widget = CustomListWidgetItem(self.driver_list,
                                             str(self.no_drivers),
                                             text)
        self.driver_list.addItem(list_item)
        self.driver_list.setItemWidget(list_item, custom_widget)

        # Prepare a new widgetlistitem for the Attr Names list
        list_item2 = QListWidgetItem()
        list_item2.setSizeHint(QtCore.QSize(0, 40))

        # Just as a minor convenience, take the name and remove the part
        # after the last underscore in the name of the object
        last_underscore = text.rfind("_")
        if text and last_underscore:
            text = text[:last_underscore]

        custom_widget2 = CustomListWidgetItem(self.attr_list,
                                              str(self.no_drivers),
                                              text.capitalize())
        self.attr_list.addItem(list_item2)
        self.attr_list.setItemWidget(list_item2, custom_widget2)

    def add_space_node(self):
        """
        Callback function to add the selected object to the space_line.
        :return: None
        """
        # Retrieve the last selected object
        try:
            selected = pmc.ls(sl=1)[-1:]
            self.space_line.setText(selected[0].name())

        except IndexError:
            pass

    def change_colorcombo_bg(self, index):
        """
        Callback that changes the Color combo when its index change.
        :return: None
        """
        # If index is 0, return to the normal color by making index 1
        color = COLORS[index - 1] if index > 0 else "555555"

        self.overr_color.setStyleSheet("background:#{0}".format(color))

    def multi_change_colorcombo_bg(self, index):
        """
        Callback that changes the Multi Color combo when its index changes.
        :return: None
        """
        # If index is 0, return to the normal color by making index 1
        color = COLORS[index - 1] if index > 0 else "555555"

        self.m_overr_color.setStyleSheet("background:#{0}".format(color))

    def create_controller_layout(self, target_layout):
        """
        Fills the right side layout (self.right_side_layout) with
        the Create Controller widgets.
        :param target_layout: Layout to contain the Create Controller widgets
        :return: None
        """

        ccmain_layout = QVBoxLayout()

        cctitle_layout = QHBoxLayout()
        cctitle_layout.addWidget(new_label("Create Controller", 10, True))
        cctitle_layout.setAlignment(QtCore.Qt.AlignHCenter)
        ccmain_layout.addLayout(cctitle_layout)
        add_space(ccmain_layout, 0, 20)

        ccmiddle_layout = QHBoxLayout()

        cclabels_layout = QVBoxLayout()
        cclabels_layout.addWidget(new_label("Name:", 10))
        add_space(cclabels_layout, 0, 8)
        cclabels_layout.addWidget(new_label("Type:", 10))
        add_space(cclabels_layout, 0, 8)
        cclabels_layout.addWidget(new_label("Side:", 10))
        add_space(cclabels_layout, 0, 10)
        cclabels_layout.addWidget(new_label("Color:", 10))
        cclabels_layout.setAlignment(QtCore.Qt.AlignTop)
        ccmiddle_layout.addLayout(cclabels_layout)
        add_space(ccmiddle_layout, 15, 0)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.name_lineedit)
        input_layout.addWidget(self.opt_combo)
        input_layout.addWidget(self.side_combo)
        input_layout.addWidget(self.overr_color)
        ccmiddle_layout.addLayout(input_layout)
        ccmiddle_layout.setAlignment(QtCore.Qt.AlignTop)
        ccmain_layout.addLayout(ccmiddle_layout)
        add_space(ccmain_layout, 0, 15)

        checkbox_main_layout = QHBoxLayout()

        checkbox_layout = QVBoxLayout()
        checkbox_layout.addWidget(self.con_checkbox)
        checkbox_layout.addWidget(self.sdk_checkbox)
        checkbox_layout.addWidget(self.parent_checkbox)
        checkbox_main_layout.addLayout(checkbox_layout)
        ccmain_layout.addLayout(checkbox_main_layout)
        checkbox_main_layout.setAlignment(QtCore.Qt.AlignHCenter)
        add_space(ccmain_layout, 0, 20)

        create_layout = QHBoxLayout()
        create_layout.addWidget(self.create_button)
        create_layout.setAlignment(QtCore.Qt.AlignHCenter)
        ccmain_layout.addLayout(create_layout)
        add_space(ccmain_layout, 0, 20)

        self.controller_frame.setLayout(ccmain_layout)
        target_layout.addWidget(self.controller_frame)
        target_layout.addStretch(1)

        # Connect the color combo to a callback that changes its bg-color
        self.connect(self.overr_color,
                     QtCore.SIGNAL("currentIndexChanged(int)"),
                     self.change_colorcombo_bg)

        # Connect the Create Button to the create_controller method
        self.connect(self.create_button, QtCore.SIGNAL("clicked()"),
                     self.create_controller)

    def create_controller_mode(self, on=True):
        """
        Turns the window into Create Controller mode. Disables the button
        at the left side and fills the right side widget.
        :return: None
        """
        if on:
            self.space_switch_mode(on=False)
            self.create_mult_ctrl_mode(on=False)

        self.create_control_button.setDisabled(on)
        self.create_control_button.setStyleSheet(button_on if on else button_off)
        self.controller_frame.setVisible(on)

    def create_controller(self):
        """
        Calls Carlo's cgc_bipedRigTutorial's createControl.
        Also aligns the resulting controller to the selected object in the
        scene through a parent constrain (and deletes it), if so desired.
        :return: None
        """
        # Retrieve last element in the selection if parent_checkbox is checked
        align = self.parent_checkbox.isChecked()
        parents = pmc.ls(sl=1) if align else None

        # The controller will have the name of its type if no name is present
        name = self.name_lineedit.text()
        name_str = CTRLS[self.opt_combo.currentIndex()] if not name else name
        side_str = {
            0: "",
            1: "left",
            2: "right"
        }[self.side_combo.currentIndex()]

        with undo_chunk():
            result = biped.createControl(side_str,
                                         name_str,
                                         CTRLS[self.opt_combo.currentIndex()],
                                         sdk=self.sdk_checkbox.isChecked(),
                                         con=self.con_checkbox.isChecked())

            # Parent the new controller's POS node to the first element in the
            # selection before the button was clicked
            if align and parents:
                # Append the name of the result[0] to the tuple of parents
                parents.append(result[0])
                pmc.delete(pmc.parentConstraint(parents))

            color = self.overr_color.currentIndex()

            # Due to some mismatch between pymel and my installation of maya,
            # color is only synced when index is under 26
            color = color + 1 if color > 25 else color

            if color:
                pmc.setAttr("{0}.overrideEnabled".format(result[3]), True)
                pmc.setAttr("{0}.overrideColor".format(result[3]), color)

    def create_mult_ctrls_layout(self, target_layout):
        """
        Fills the right side layout (self.right_side_layout) with
        the Create Multiple Controllers widgets.
        :param target_layout: Layout to contain the Mult Controller widgets
        :return: None
        """

        mcmain_layout = QVBoxLayout()

        mctitle_layout = QHBoxLayout()
        mctitle_layout.addWidget(new_label("Create Multiple Controllers", 10, True))
        mctitle_layout.setAlignment(QtCore.Qt.AlignHCenter)
        mcmain_layout.addLayout(mctitle_layout)
        add_space(mcmain_layout, 0, 20)

        mcmiddle_layout = QHBoxLayout()

        mclabels_layout = QVBoxLayout()
        mclabels_layout.addWidget(new_label("Type:", 10))
        add_space(mclabels_layout, 0, 10)
        mclabels_layout.addWidget(new_label("Color:", 10))
        mclabels_layout.setAlignment(QtCore.Qt.AlignTop)
        mcmiddle_layout.addLayout(mclabels_layout)
        add_space(mcmiddle_layout, 15, 0)

        m_input_layout = QVBoxLayout()
        m_input_layout.addWidget(self.m_opt_combo)
        m_input_layout.addWidget(self.m_overr_color)
        mcmiddle_layout.addLayout(m_input_layout)
        mcmiddle_layout.setAlignment(QtCore.Qt.AlignTop)
        mcmain_layout.addLayout(mcmiddle_layout)
        add_space(mcmain_layout, 0, 15)

        m_checkbox_main_layout = QHBoxLayout()

        m_checkbox_layout = QVBoxLayout()
        m_checkbox_layout.addWidget(self.m_con_checkbox)
        m_checkbox_layout.addWidget(self.m_sdk_checkbox)
        m_checkbox_layout.addWidget(self.m_parent_checkbox)
        m_checkbox_main_layout.addLayout(m_checkbox_layout)
        mcmain_layout.addLayout(m_checkbox_main_layout)
        m_checkbox_main_layout.setAlignment(QtCore.Qt.AlignHCenter)
        add_space(mcmain_layout, 0, 20)

        m_create_layout = QHBoxLayout()
        m_create_layout.addWidget(self.m_create_button)
        m_create_layout.setAlignment(QtCore.Qt.AlignHCenter)
        mcmain_layout.addLayout(m_create_layout)
        add_space(mcmain_layout, 0, 20)

        self.mult_ctrls_frame.setLayout(mcmain_layout)
        target_layout.addWidget(self.mult_ctrls_frame)
        target_layout.addStretch(1)

        # Connect the color combo to a callback that changes its bg-color
        self.connect(self.m_overr_color,
                     QtCore.SIGNAL("currentIndexChanged(int)"),
                     self.multi_change_colorcombo_bg)
        self.connect(self.m_create_button, QtCore.SIGNAL("clicked()"),
                     self.create_multiple_ctrls)

    def create_mult_ctrl_mode(self, on=True):
        """
        Turns the window into Create Mult Controller mode. Disables the button
        at the left side and fills the right side widget.
        :return: None
        """
        if on:
            self.space_switch_mode(on=False)
            self.create_controller_mode(on=False)

        self.multiple_ctrls_button.setDisabled(on)
        self.multiple_ctrls_button.setStyleSheet(button_on if on else button_off)
        self.mult_ctrls_frame.setVisible(on)

    def create_multiple_ctrls(self):
        """
        Calls createControl for as many times as selected objects
        :return: None
        """

        align = self.m_parent_checkbox.isChecked()
        parents = pmc.ls(sl=1)

        if not parents:
            print "There is nothing selected!"
            return

        with undo_chunk():
            for obj in parents:
                # The controllers will have the name as their object, sans the
                # latest underscore
                name = obj.name()
                underscore = name.rfind("_")
                name_str = name if not underscore else name[:underscore]

                result = biped.createControl("",
                                             name_str,
                                             CTRLS[self.m_opt_combo.currentIndex()],
                                             sdk=self.m_sdk_checkbox.isChecked(),
                                             con=self.m_con_checkbox.isChecked())

                # Parent the new controller's POS node to its element
                if align:
                    pmc.delete(pmc.parentConstraint(obj, result[0]))

                color = self.m_overr_color.currentIndex()

                # Due to some mismatch between pymel and my installation of maya,
                # color is only synced when index is under 26
                color = color + 1 if color > 25 else color

                if color:
                    pmc.setAttr("{0}.overrideEnabled".format(result[3]), True)
                    pmc.setAttr("{0}.overrideColor".format(result[3]), color)

    def delete_driver_item(self):
        """
        Deletes the selected driver nodes and their corresponding attr names.
        :return: None
        """
        selected = self.driver_list.selectedItems()

        for item in selected:
            index = self.driver_list.row(item)
            self.driver_list.takeItem(index)
            self.attr_list.takeItem(index)

    def space_switch_layout(self, target_layout):
        """
        Fills the right side layout (self.right_side_layout) with
        the Space Switch widgets.
        :param target_layout: Layout to contain the Space Switch widgets
        :return: None
        """
        main_layout = QVBoxLayout()

        title_layout = QHBoxLayout()
        title_layout.addWidget(new_label("Create Coordinates Switch", 10, True))
        title_layout.setAlignment(QtCore.Qt.AlignHCenter)
        main_layout.addLayout(title_layout)
        add_space(main_layout, 0, 20)

        middle_layout = QHBoxLayout()

        labels_layout = QVBoxLayout()
        labels_layout.addWidget(new_label("Driven Node:", 10))
        add_space(labels_layout, 0, 10)
        labels_layout.addWidget(new_label("Space Node:", 10))
        add_space(labels_layout, 0, 10)
        labels_layout.addWidget(new_label("Driver Nodes:", 10))
        add_space(labels_layout, 0, 90)
        labels_layout.addWidget(new_label("Attr Names:", 10))
        add_space(labels_layout, 0, 90)
        labels_layout.addWidget(new_label("Constraint:", 10))
        add_space(labels_layout, 0, 15)
        labels_layout.addWidget(new_label("Side:", 10))
        labels_layout.setAlignment(QtCore.Qt.AlignTop)
        middle_layout.addLayout(labels_layout)
        add_space(middle_layout, 15, 0)

        input_layout = QVBoxLayout()
        input_layout.addWidget(self.driven_line)
        add_space(input_layout, 0, 5)
        input_layout.addWidget(self.space_line)
        add_space(input_layout, 0, 5)
        input_layout.addWidget(self.driver_list)
        add_space(input_layout, 0, 5)
        input_layout.addWidget(self.attr_list)
        add_space(input_layout, 0, 5)
        input_layout.addWidget(self.const_combo)
        add_space(input_layout, 0, 5)
        input_layout.addWidget(self.ssside_combo)
        input_layout.setAlignment(QtCore.Qt.AlignTop)
        middle_layout.addLayout(input_layout)
        add_space(middle_layout, 15, 0)

        button_layout = QVBoxLayout()
        driven_button = new_button("Add Scene Selection", 8, 110)
        space_button = new_button("Add Scene Selection", 8, 110)
        add_driver_button = new_button("Add Empty Driver", 8, 110)
        sel_driver_button = new_button("Add Scene Selection", 8, 110)
        rm_driver_button = new_button("Remove Selected Items", 7, 110)
        button_layout.addWidget(driven_button)
        button_layout.addWidget(space_button)
        add_space(button_layout, 0, 20)
        button_layout.addWidget(add_driver_button)
        button_layout.addWidget(sel_driver_button)
        button_layout.addWidget(rm_driver_button)
        button_layout.setAlignment(QtCore.Qt.AlignTop)
        middle_layout.addLayout(button_layout)
        middle_layout.setAlignment(QtCore.Qt.AlignTop)
        main_layout.addLayout(middle_layout)
        add_space(main_layout, 0, 30)

        bottom_layout = QHBoxLayout()
        space_switch_button = new_button("Create Space Switch", 10)
        bottom_layout.addWidget(space_switch_button)
        bottom_layout.setAlignment(QtCore.Qt.AlignHCenter)
        main_layout.addLayout(bottom_layout)
        add_space(main_layout, 0, 20)

        self.space_switch_frame.setLayout(main_layout)
        target_layout.addWidget(self.space_switch_frame)
        target_layout.addStretch(1)

        # Connect the buttons to their corresponding callbacks
        self.connect(driven_button, QtCore.SIGNAL("clicked()"),
                     self.add_driven)
        self.connect(space_button, QtCore.SIGNAL("clicked()"),
                     self.add_space_node)
        self.connect(add_driver_button, QtCore.SIGNAL("clicked()"),
                     self.add_driver)
        self.connect(rm_driver_button, QtCore.SIGNAL("clicked()"),
                     self.delete_driver_item)
        self.connect(sel_driver_button, QtCore.SIGNAL("clicked()"),
                     self.add_driver_selection)
        self.connect(space_switch_button, QtCore.SIGNAL("clicked()"),
                     self.space_switch)

    def space_switch_mode(self, on=True):
        """
        Turns the window into Create Controller mode. Disables the button
        at the left side and fills the right side widget.
        :return: None
        """
        if on:
            self.create_controller_mode(on=False)
            self.create_mult_ctrl_mode(on=False)

        # Reset the widget lists by removing the current items
        else:
            if self.no_drivers > 0:
                self.no_drivers = 0

                while self.driver_list.count():
                    self.driver_list.takeItem(0)

                while self.attr_list.count():
                    self.attr_list.takeItem(0)

        self.space_switch_button.setDisabled(on)
        self.space_switch_button.setStyleSheet(button_on if on else button_off)
        self.space_switch_frame.setVisible(on)

    def space_switch(self):
        """
        Calls Carlo's cgc_bipedRigTutorial's createCoordinatesSwitch.
        :return: None
        """
        # Retrieve the Driver list, ignore blank line edits
        drivers = []

        for i in range(self.driver_list.count()):
            w = self.driver_list.itemWidget(self.driver_list.item(i))
            text = w.children()[2].text()
            if text:
                drivers.append(text)

        # In a similar way, retrieve the attr name list items
        attr_names = []

        for i in range(self.attr_list.count()):
            w = self.attr_list.itemWidget(self.attr_list.item(i))
            text = w.children()[2].text()
            if text:
                attr_names.append(text)
            # If there is no text, add the name of the driver just in case
            else:
                attr_names.append(drivers[i])

        # Encode the type of constraint
        const_str = {
            0: "parent",
            1: "orient",
            2: "point"
        }[self.const_combo.currentIndex()]

        # Encode the side, if any
        side_str = {
            0: "",
            1: "left",
            2: "right"
        }[self.ssside_combo.currentIndex()]

        with undo_chunk():
            biped.createCoordinatesSwitch(driversList=drivers,
                                          attrsList=attr_names,
                                          drivenNode=self.driven_line.text(),
                                          spaceNode=self.space_line.text(),
                                          constraintType=const_str,
                                          side=side_str)

class CustomListWidgetItem(QWidget):
    """
    Widget that contains an index number and a QLineEdit for the attr name.
    """
    def __init__(self, parent, index, default=""):
        super(CustomListWidgetItem, self).__init__(parent)
        main_layout = QHBoxLayout()
        self.setFixedHeight(40)

        # Insert a label that helps the user correlate both lists
        main_layout.addWidget(new_label("{}.".format(index), 10))

        # Line edit that will contain the name of the driver or attr
        lineedit = new_line_edit(80)
        lineedit.setText(default)
        lineedit.setStyleSheet("background:#FFFFFF; color:#000000")
        main_layout.addWidget(lineedit)
        main_layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        self.setLayout(main_layout)


class undo_chunk():
    """
    Allows the UI to undo the functions with a single Undo command.
    """
    def __enter__(self):
        pmc.undoInfo(openChunk=True)
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        pmc.undoInfo(closeChunk=True)
        # Undo in case of an exception being raised
        if exc_val is not None:
            pmc.undo()


# ===== UTILITY FUNCTIONS ====

def add_space(layout, x, y):
    """
    Add a spacer in the window's layouts
    :param layout: Layout where the spacer will be added
    :param x: Width of spacer
    :param y: Height of spacer
    :return: None
    """
    spacer = QSpacerItem(x, y)
    layout.addSpacerItem(spacer)

def new_button(text, font_size=None, size=200):
    """
    Returns a new button
    :param text: Text that the button will contain
    :param font_size: Optional Font size of the button's text
    :return: QPushButton instance
    """
    button = QPushButton('   ' + text + '   ')
    button.setStyleSheet(button_off)
    button.setFixedSize(size, 25)

    if font_size is not None:
        font = QFont()
        font.setPointSize(font_size)
        button.setFont(font)
    return button

def new_checkbox(text, checked=False):
    """
    Return a new Checkbox
    :param text: Text that will accompany the checkbox
    :return: QCheckbox instance
    """
    checkbox = QCheckBox(text)
    checkbox.setStyleSheet("color:#EEEEEE;")
    checkbox.setChecked(checked)

    cb_palette = checkbox.palette()
    cb_palette.setColor(QPalette.Base, QtCore.Qt.gray)
    checkbox.setPalette(cb_palette)

    return checkbox

def new_combobox(options):
    """
    Return a new Combobox instance.
    :param text: Text that will accompany the checkbox
    :return: QCheckbox instance
    """
    combobox = QComboBox()
    combobox.setStyleSheet("background:#555555; color:#CCCCCC;")
    combobox.setMinimumHeight(25)
    combobox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    for option in options:
        combobox.addItem(option)

    return combobox

def new_combobox_color_choice(parent, color_list):
    """
    Return a Combobox instance with colored items.
    :param color_list: Tuple containing hexadecimal notations of colors
    :return: QCombobox instance
    """
    combobox = QComboBox(parent)
    combobox.setStyleSheet("background:#555555; color:#CCCCCC;")
    combobox.setMinimumSize(50, 25)
    combobox.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    # Add a field for "None"
    combobox.addItem("None")

    model = combobox.model()

    for color in color_list:
        item = QStandardItem(" ")
        item.setBackground(QColor("#" + color))
        model.appendRow(item)

    return combobox

def new_frame(parent, size, name, raised=False, fixed_size=True):
    """
    Create a QFrame instance.
    :param parent: Parent QWidget instance
    :param size: Tuple containing width and height of the frame
    :param name: Name of the QFrame instance
    :param raised: Style the frame as a raised box
    :param fixed_size: Keep the same width and height?
    :return: QFrame instance
    """
    frame = QFrame(parent)
    frame.setMinimumSize(*size)
    frame.setObjectName(name)
    frame.setStyleSheet("#{0} {{ border: 2px solid #666666; }}".format(name))

    if raised:
        frame.setFrameStyle(QFrame.Box | QFrame.Raised)
    if fixed_size:
        frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    return frame

def new_label(text, size=10, bold=False, bg_color=""):
    """
    Return a new QLabel
    :param text: Text that will be contained by the label
    :param size: Size of the label's text
    :param bold: Boolean that tells whether to bold the label or not
    :param bg_color: An hexadecimal notation of a color
    :return: QLabel instance
    """
    label = QLabel(text)
    label.setAlignment(QtCore.Qt.AlignLeft)
    label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    font = QFont()
    font.setPointSize(size)
    if bold:
        font.setBold(bold)
    label.setFont(font)

    style = ["color:#EEEEEE;"]
    if bg_color:
        style.append("background:#{};".format(bg_color))

    label.setStyleSheet(" ".join(style))

    return label

def new_line_edit(size, readonly=False, focus=False):
    """
    Return a new QLineEdit with standard styling
    :param size: Width of the textbox
    :param readonly: Boolean to make the field read-only
    :return: QLineEdit instance
    """
    textbox = QLineEdit()
    textbox.setFixedSize(size, 20)
    textbox.setStyleSheet("background:#6E6E6E; border:none; color:#FFFFFF")
    textbox.setReadOnly(readonly)
    textbox.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
    if focus:
        textbox.setFocusPolicy(QtCore.Qt.StrongFocus)

    return textbox

def new_listwidget():
    listwidget = QListWidget()
    listwidget.setMinimumSize(150, 100)
    listwidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
    listwidget.setStyleSheet("background:#6E6E6E;")

    return listwidget

def get_maya_window():
    """
    Gets the Main Maya window as the parent
    :return: Returns a wrapped instance of the main Maya window
    """
    pointer = OpenMayaUI.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer), QWidget)

def show():
    """
    Creates the window with all of its widgets.
    :return: None
    """
    if pmc.window('riggingToolsUI', exists=True):
        pmc.deleteUI('riggingToolsUI', wnd=True)

    parent_window = get_maya_window()
    _window = RiggingToolsWindow(parent_window)

    background_palette = _window.palette()
    background_palette.setColor(_window.backgroundRole(), QColor(46, 46, 46))
    _window.setPalette(background_palette)

    _window.show()

def test():
    """
    Test layout function for PySide only. No Maya needed.
    :return: None
    """
    import sys

    app = QApplication(sys.argv)

    ex = RiggingToolsWindow()

    # Change the window's background color
    background_palette = ex.palette()
    background_palette.setColor(ex.backgroundRole(), QColor(46, 46, 46))
    ex.setPalette(background_palette)

    ex.show()

    app.exec_()

if __name__ == '__main__':
    test()
