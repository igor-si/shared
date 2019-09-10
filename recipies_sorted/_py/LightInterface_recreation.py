from PySide.QtGui import *
from PySide import QtCore

class LightInterfaceWindow(QMainWindow):

    def __init__(self, parent=None):

        super(LightInterfaceWindow, self).__init__(parent)

        # ============ UTILITY CLOSURES ===============
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

        def add_line(length):
            """
            Return a thick line to add in the layouts
            :param length: Length of the line
            :return: QFrame in the form of a line
            """
            line = QFrame()
            line.setFixedWidth(length)
            line.setGeometry(QtCore.QRect(0, 0, length, 0))
            line.setStyleSheet('background-color:#FFFFFF')
            line.setFrameShape(QFrame.HLine)
            return line

        def new_button(text, font_size=None):
            """
            Returns a new button
            :param text: Text that the button will contain
            :param font_size: Optional Font size of the button's text
            :return: QPushButton
            """
            button = QPushButton('  ' + text + '  ')
            button.setStyleSheet("background-color:#555555; color:#CCCCCC;")
            button.setFixedHeight(25)
            if font_size is not None:
                font = QFont()
                font.setPointSize(font_size)
                button.setFont(font)
            return button

        def new_checkbox(text):
            """
            Return a new Checkbox
            :param text: Text that will accompany the checkbox
            :return: QCheckbox
            """
            checkbox = QCheckBox(text)
            checkbox.setStyleSheet('color:#EEEEEE;')

            cb_palette = checkbox.palette()
            cb_palette.setColor(QPalette.Base, QtCore.Qt.gray)
            checkbox.setPalette(cb_palette)

            return checkbox

        def new_label(text, size, bold=False):
            """
            Return a new QLabel
            :param text: Text that will be contained by the label
            :param size: Size of the label's text
            :param bold: Boolean that tells whether to bold the label or not
            :return: QLabel
            """
            label = QLabel(text)
            label.setStyleSheet('color:#EEEEEE;')
            label.setAlignment(QtCore.Qt.AlignCenter)

            font = QFont()
            font.setPointSize(size)
            if bold:
                font.setBold(bold)
            label.setFont(font)
            return label

        def new_line_edit(size, readonly=False):
            """
            Return a new QLineEdit with standard styling
            :param size: Width of the textbox
            :param readonly: Boolean that tells whether to make it non-modifiable
            :return:
            """
            textbox = QLineEdit()
            textbox.setFixedSize(size, 20)
            textbox.setReadOnly(readonly)
            textbox.setStyleSheet('background-color:#6E6E6E; border:none; color:#FFFFFF')
            textbox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            return textbox

        # ============ WIDGETS ============

        # Create and set the container's central widget on the window
        main_container = QWidget(self)
        self.setCentralWidget(main_container)

        # =============== LEFT SIDE OF THE WINDOW ===============

        # Search Textbox (and its Focus Policy) and its label, along with its container layout
        search_layout = QHBoxLayout()
        search_label = new_label('Search Lights:', 8)
        self.searchlight_tbox = new_line_edit(110)
        self.searchlight_tbox.setFocusPolicy(QtCore.Qt.StrongFocus)

        # Widget List that will hold the light names in the scene, and its container layout
        widgetlist_layout = QHBoxLayout()
        self.widgetlist = QListWidget()
        self.widgetlist.setMinimumHeight(400)
        self.widgetlist.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Render Layer Only and Update List buttons
        left_buttons_layout = QHBoxLayout()

        self.renderlayer_button = new_button('Show Current Render Layer Only', 7)
        self.updatebutton = new_button('Update List', 8)

        # Bottom checkbox
        bottomleft_layout = QHBoxLayout()
        self.timeline_listener = new_checkbox('Listen to Timeline Changes')

        # ================ RIGHT SIDE OF THE WINDOW =================

        # QFrame container of the modifier widgets
        modifiers_frame = QFrame(main_container)
        modifiers_frame.setFrameStyle(QFrame.Box | QFrame.Raised)
        modifiers_frame.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        modifiers_frame.setLineWidth(1)

        # Intensity Top Label
        intensitylabel_layout = QHBoxLayout()
        intensitylabel = new_label('Intensity', 10, True)
        intensitylabel_rightline = add_line(100)

        # Main Intensity layout, Current Intensity label, modifying textbox and Operator combo box
        intensity_layout = QVBoxLayout()

        currentintensity_layout = QHBoxLayout()
        intensitycurrent_label = new_label('Current:', 8)
        self.currentintensity_label = new_label('N/A', 11, True)

        setintensity_layout = QHBoxLayout()
        intensityquantity_label = new_label('Set:', 8)
        self.intensityquantity_textbox = new_line_edit(60)

        self.intensityoperator_combo = QComboBox()
        self.intensityoperator_combo.addItem("fixed quantity")
        self.intensityoperator_combo.addItem("+/- increase")
        self.intensityoperator_combo.addItem("* multiply")
        self.intensityoperator_combo.addItem("+/- percentage")
        self.intensityoperator_combo.setStyleSheet("background-color:#555555; color:#CCCCCC;")
        self.intensityoperator_combo.setFixedHeight(25)

        # Intensity Bottom Widgets
        intensity_bottomlayout = QHBoxLayout()

        self.keyframeintensity_checkbox = new_checkbox('Set Keyframe')
        self.applyintensity_button = new_button('Apply Intensity')

        # Light Color Top Label
        colorlabel_layout = QHBoxLayout()
        colorlabel = new_label('Color', 10, True)
        colorlabel_rightline = add_line(100)

        # Light Color Dialog Prompter, RGB/HSV boxes and Frame
        color_layout = QHBoxLayout()
        colorTextboxes_layout = QVBoxLayout()
        rh_layout = QHBoxLayout()
        gs_layout = QHBoxLayout()
        bv_layout = QHBoxLayout()

        self.color_frame = colorFrame(main_container, 1, 255, 255, 255)

        r_label = new_label('R:', 9)
        g_label = new_label('G:', 9)
        b_label = new_label('B:', 9)
        h_label = new_label('H:', 9)
        s_label = new_label('S:', 9)
        v_label = new_label('V:', 9)

        self.r_textbox = new_line_edit(40, True)
        self.g_textbox = new_line_edit(40, True)
        self.b_textbox = new_line_edit(40, True)
        self.h_textbox = new_line_edit(40, True)
        self.s_textbox = new_line_edit(40, True)
        self.v_textbox = new_line_edit(40, True)

        # Light Color Bottom
        lightcolor_bottomlayout = QHBoxLayout()

        self.keyframecolor_checkbox = new_checkbox('Set Keyframe')
        self.applycolor_button = new_button('Apply Color')

        # Shadow Color Top Label
        colorshadowlabel_layout = QHBoxLayout()
        colorshadowlabel = new_label('Shadow Color', 10, True)
        colorshadowlabel_rightline = add_line(100)

        # Shadow Color Dialog Prompter, RGB/HSV boxes and Frame
        colorshadow_layout = QHBoxLayout()
        colorshadowTextboxes_layout = QVBoxLayout()
        rhshadow_layout = QHBoxLayout()
        gsshadow_layout = QHBoxLayout()
        bvshadow_layout = QHBoxLayout()

        self.colorshadow_frame = colorFrame(main_container, 2, 0, 0, 0)

        rshadow_label = new_label('R:', 9)
        gshadow_label = new_label('G:', 9)
        bshadow_label = new_label('B:', 9)
        hshadow_label = new_label('H:', 9)
        sshadow_label = new_label('S:', 9)
        vshadow_label = new_label('V:', 9)

        self.rshadow_textbox = new_line_edit(40, True)
        self.gshadow_textbox = new_line_edit(40, True)
        self.bshadow_textbox = new_line_edit(40, True)
        self.hshadow_textbox = new_line_edit(40, True)
        self.sshadow_textbox = new_line_edit(40, True)
        self.vshadow_textbox = new_line_edit(40, True)

        # Shadow Color Bottom
        shadowcolor_bottomlayout = QHBoxLayout()

        self.keyframeshadow_checkbox = new_checkbox('Set Keyframe')
        self.applyshadow_button = new_button('Apply Shadow')

        # Render Layer Buttons
        renderlayer_layout = QHBoxLayout()

        self.renderlayer_add = new_button('Add to Render Layer', 7)
        self.renderlayer_remove = new_button('Remove from Render Layer', 7)

        # ============ LAYOUTS ============

        # ------ Vertical box layout for the left side ------
        vertical_layout_left = QVBoxLayout()

        # ------ Vertical box layout for the right side ------
        vertical_layout_right = QVBoxLayout()

        # ------ Modifiers Layout and Widgets ------
        modifiers_layout = QVBoxLayout()

        # Search box Layout
        search_layout.addStretch(1)
        search_layout.addWidget(search_label)
        add_space(search_layout, 5, 0)
        search_layout.addWidget(self.searchlight_tbox)

        add_space(vertical_layout_left, 0, 10)
        vertical_layout_left.addLayout(search_layout)
        add_space(vertical_layout_left, 0, 5)

        # Widget list Layout
        widgetlist_layout.addWidget(self.widgetlist)
        vertical_layout_left.addLayout(widgetlist_layout)
        add_space(vertical_layout_left, 0, 5)

        # Render Layer Only and Update buttons at the left side
        left_buttons_layout.addWidget(self.renderlayer_button)
        left_buttons_layout.addStretch(1)
        left_buttons_layout.addWidget(self.updatebutton)

        vertical_layout_left.addLayout(left_buttons_layout)
        add_space(vertical_layout_left, 0, 5)

        # Timeline Listener Checkbox
        bottomleft_layout.addWidget(self.timeline_listener)
        add_space(vertical_layout_left, 0, 15)
        vertical_layout_left.addLayout(bottomleft_layout)
        add_space(vertical_layout_left, 0, 5)

        # Intensity label
        add_space(intensitylabel_layout, 20, 0)
        intensitylabel_layout.addWidget(intensitylabel)
        intensitylabel_layout.addStretch(1)
        intensitylabel_layout.addWidget(intensitylabel_rightline)
        add_space(intensitylabel_layout, 20, 0)
        intensitylabel_layout.setAlignment(QtCore.Qt.AlignLeft)

        modifiers_layout.addLayout(intensitylabel_layout)
        add_space(modifiers_layout, 0, 5)

        # Intensity modifiers
        add_space(currentintensity_layout, 20, 0)
        currentintensity_layout.addWidget(intensitycurrent_label)
        currentintensity_layout.addStretch(1)
        currentintensity_layout.addWidget(self.currentintensity_label)
        add_space(currentintensity_layout, 20, 0)
        currentintensity_layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        add_space(setintensity_layout, 20, 0)
        setintensity_layout.addWidget(intensityquantity_label)
        add_space(setintensity_layout, 6, 0)
        setintensity_layout.addWidget(self.intensityquantity_textbox)
        setintensity_layout.addStretch(1)
        setintensity_layout.addWidget(self.intensityoperator_combo)
        add_space(setintensity_layout, 20, 0)
        setintensity_layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        intensity_layout.addLayout(currentintensity_layout)
        add_space(intensity_layout, 0, 10)
        intensity_layout.addLayout(setintensity_layout)
        add_space(intensity_layout, 0, 10)

        modifiers_layout.addLayout(intensity_layout)
        add_space(modifiers_layout, 0, 6)

        # Bottom elements of intensity
        add_space(intensity_bottomlayout, 20, 0)
        intensity_bottomlayout.addWidget(self.keyframeintensity_checkbox)
        intensity_bottomlayout.addStretch(1)
        intensity_bottomlayout.addWidget(self.applyintensity_button)
        add_space(intensity_bottomlayout, 20, 0)

        modifiers_layout.addLayout(intensity_bottomlayout)
        add_space(modifiers_layout, 0, 10)

        # Color label
        add_space(colorlabel_layout, 20, 0)
        colorlabel_layout.addWidget(colorlabel)
        colorlabel_layout.addStretch(1)
        colorlabel_layout.addWidget(colorlabel_rightline)
        add_space(colorlabel_layout, 20, 0)
        colorlabel_layout.setAlignment(QtCore.Qt.AlignCenter)

        modifiers_layout.addLayout(colorlabel_layout)
        add_space(modifiers_layout, 0, 5)

        # Color Canvas, Buttons and Textboxes
        add_space(color_layout, 20, 0)
        color_layout.addWidget(self.color_frame)

        rh_layout.addWidget(r_label)
        add_space(rh_layout, 2, 0)
        rh_layout.addWidget(self.r_textbox)
        rh_layout.addStretch(1)
        rh_layout.addWidget(h_label)
        add_space(rh_layout, 2, 0)
        rh_layout.addWidget(self.h_textbox)
        add_space(rh_layout, 20, 0)
        colorTextboxes_layout.addLayout(rh_layout)

        gs_layout.addWidget(g_label)
        add_space(gs_layout, 2, 0)
        gs_layout.addWidget(self.g_textbox)
        gs_layout.addStretch(1)
        gs_layout.addWidget(s_label)
        add_space(gs_layout, 2, 0)
        gs_layout.addWidget(self.s_textbox)
        add_space(gs_layout, 20, 0)
        colorTextboxes_layout.addLayout(gs_layout)

        bv_layout.addWidget(b_label)
        add_space(bv_layout, 2, 0)
        bv_layout.addWidget(self.b_textbox)
        bv_layout.addStretch(1)
        bv_layout.addWidget(v_label)
        add_space(bv_layout, 2, 0)
        bv_layout.addWidget(self.v_textbox)
        add_space(bv_layout, 20, 0)
        colorTextboxes_layout.addLayout(bv_layout)

        color_layout.addLayout(colorTextboxes_layout)

        add_space(modifiers_layout, 0, 5)
        modifiers_layout.addLayout(color_layout)
        add_space(modifiers_layout, 0, 5)

        # Bottom elements of light color
        add_space(lightcolor_bottomlayout, 20, 0)
        lightcolor_bottomlayout.addWidget(self.keyframecolor_checkbox)
        lightcolor_bottomlayout.addStretch(1)
        lightcolor_bottomlayout.addWidget(self.applycolor_button)
        add_space(lightcolor_bottomlayout, 20, 0)
        lightcolor_bottomlayout.setAlignment(QtCore.Qt.AlignLeft)

        modifiers_layout.addLayout(lightcolor_bottomlayout)
        add_space(modifiers_layout, 0, 10)

        # Shadow Color label
        add_space(colorshadowlabel_layout, 20, 0)
        colorshadowlabel_layout.addWidget(colorshadowlabel)
        colorshadowlabel_layout.addStretch(1)
        colorshadowlabel_layout.addWidget(colorshadowlabel_rightline)
        add_space(colorshadowlabel_layout, 20, 0)
        colorshadowlabel_layout.setAlignment(QtCore.Qt.AlignCenter)

        modifiers_layout.addLayout(colorshadowlabel_layout)
        add_space(modifiers_layout, 0, 5)

        # Shadow Color Canvas, Buttons and Textboxes
        add_space(colorshadow_layout, 20, 0)
        colorshadow_layout.addWidget(self.colorshadow_frame)

        rhshadow_layout.addWidget(rshadow_label)
        add_space(rhshadow_layout, 2, 0)
        rhshadow_layout.addWidget(self.rshadow_textbox)
        rhshadow_layout.addStretch(1)
        rhshadow_layout.addWidget(hshadow_label)
        add_space(rhshadow_layout, 2, 0)
        rhshadow_layout.addWidget(self.hshadow_textbox)
        add_space(rhshadow_layout, 20, 0)
        colorshadowTextboxes_layout.addLayout(rhshadow_layout)

        gsshadow_layout.addWidget(gshadow_label)
        add_space(gsshadow_layout, 2, 0)
        gsshadow_layout.addWidget(self.gshadow_textbox)
        gsshadow_layout.addStretch(1)
        gsshadow_layout.addWidget(sshadow_label)
        add_space(gsshadow_layout, 2, 0)
        gsshadow_layout.addWidget(self.sshadow_textbox)
        add_space(gsshadow_layout, 20, 0)
        colorshadowTextboxes_layout.addLayout(gsshadow_layout)

        bvshadow_layout.addWidget(bshadow_label)
        add_space(bvshadow_layout, 2, 0)
        bvshadow_layout.addWidget(self.bshadow_textbox)
        bvshadow_layout.addStretch(1)
        bvshadow_layout.addWidget(vshadow_label)
        add_space(bvshadow_layout, 2, 0)
        bvshadow_layout.addWidget(self.vshadow_textbox)
        add_space(bvshadow_layout, 20, 0)
        colorshadowTextboxes_layout.addLayout(bvshadow_layout)

        colorshadow_layout.addLayout(colorshadowTextboxes_layout)
        colorshadow_layout.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        add_space(modifiers_layout, 0, 5)
        modifiers_layout.addLayout(colorshadow_layout)

        # Bottom elements of shadow color
        add_space(shadowcolor_bottomlayout, 20, 0)
        shadowcolor_bottomlayout.addWidget(self.keyframeshadow_checkbox)
        shadowcolor_bottomlayout.addStretch(1)
        shadowcolor_bottomlayout.addWidget(self.applyshadow_button)
        add_space(shadowcolor_bottomlayout, 20, 0)
        shadowcolor_bottomlayout.setAlignment(QtCore.Qt.AlignLeft)

        add_space(modifiers_layout, 0, 5)
        modifiers_layout.addLayout(shadowcolor_bottomlayout)
        add_space(modifiers_layout, 0, 10)

        # Finish modifiers' layout by setting a Center Alignment and adding it to the modifier frame
        modifiers_frame.setLayout(modifiers_layout)
        modifiers_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Add the QFrame to the right side's vertical layout
        vertical_layout_right.addWidget(modifiers_frame)

        # Render Layer Buttons
        renderlayer_layout.addWidget(self.renderlayer_add)
        add_space(renderlayer_layout, 20, 0)
        renderlayer_layout.addWidget(self.renderlayer_remove)
        renderlayer_layout.setAlignment(QtCore.Qt.AlignCenter)

        add_space(vertical_layout_right, 0, 15)
        vertical_layout_right.addLayout(renderlayer_layout)

        # Set Alignments for containers
        vertical_layout_right.setAlignment(QtCore.Qt.AlignTop)

        # Main layout (Horizontal) for the whole window
        main_layout = QHBoxLayout()
        add_space(main_layout, 10, 0)
        main_layout.addLayout(vertical_layout_left)
        add_space(main_layout, 20, 0)
        main_layout.addLayout(vertical_layout_right)
        add_space(main_layout, 10, 0)

        main_container.setLayout(main_layout)
        self.setWindowTitle('Light Interface')


class colorFrame(QFrame):
    def __init__(self, parent, number, red, green, blue):
        """
        Create a customizable QFrame that reacts to a click by opening a QColorDialog
        :param parent: Widget parent of this frame
        :param number: 1 if it's Color Light, 2 if it's Shadow Color
        :param red: Red value to set on a new QColor
        :param green: Green value to set on a new QColor
        :param blue: Blue value to set on a new QColor
        :return: None
        """
        super(colorFrame, self).__init__(parent)

        self.kind = number
        self.hexadecimal = QLabel('', self)
        self.color = QColor(red, green, blue)
        self.update_color(self.color)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.hexadecimal)
        vertical_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.setLineWidth(1)
        self.setFixedSize(80, 80)
        self.setLayout(vertical_layout)

    def update_color(self, color):
        """
        Updates the current frame's QColor's value
        :param color: QColor
        :return: None
        """
        self.color = color
        self.setStyleSheet("background-color: %s" % self.color.name())

        if self.color.black() < 128:
            self.hexadecimal.setStyleSheet('color:#000000')
        else:
            self.hexadecimal.setStyleSheet('color:#FFFFFF')
        self.hexadecimal.setText(self.color.name())


def main():
    app = QApplication([])
    ex = LightInterfaceWindow()

    # Change the window's background color
    background_palette = ex.palette()
    background_palette.setColor(ex.backgroundRole(), QColor(46, 46, 46))
    ex.setPalette(background_palette)

    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()