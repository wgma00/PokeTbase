# Copyright (c) 2016 William Granados
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
# !/usr/bin/python

import sys
from team_database import Database
from team import Team
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    '''Graphical interface that is show to the user'''

    def __init__(self):
        # members
        self._user_input = ['' for i in range(6)]
        self._database = Database()
        # gui members
        super(Window, self).__init__()
        self.init_UI()
        self.init_dropdown_menu()
        self.init_search_button()
        self.init_editor()
        self.layout.addStretch()
        self.show()

    def init_UI(self):
        '''(Window) -> None
        Sets the dimensions and user interface
        '''
        self.setGeometry(150, 150, 300, 210)
        self.setWindowTitle('PokéTbase - Pokémon Team Database')
        self.setWindowIcon(QtGui.QIcon('../res/icon/pikachu_icon.png'))
        self.layout = QtGui.QHBoxLayout()

    def init_dropdown_menu(self):
        ''' (Window) -> None
        Sets up the input the user can give
        '''
        file = open("../res/pokemon-names/pokemon-names.txt")
        pokemon_names = []
        for name in file:
            pokemon_names.append(name)
        # create 6 combo boxes since there are 6 members on a team
        self._combo_box = [QtGui.QComboBox(self) for x in range(6)]
        for name in pokemon_names:
            for i in range(6):
                self._combo_box[i].addItem(name)

        # set up each user input individually

        # combo box 1
        self._combo_box[0].move(0, 0)
        self._combo_box[0].activated[str].connect(self.user_choice_one)
        self.layout.addWidget(self._combo_box[0])

        # combo box 2
        self._combo_box[1].move(0, 30)
        self._combo_box[1].activated[str].connect(self.user_choice_two)
        self.layout.addWidget(self._combo_box[1])

        # combo box 3
        self._combo_box[2].move(0, 60)
        self._combo_box[2].activated[str].connect(self.user_choice_three)
        self.layout.addWidget(self._combo_box[2])

        # combo box 4
        self._combo_box[3].move(0, 90)
        self._combo_box[3].activated[str].connect(self.user_choice_four)
        self.layout.addWidget(self._combo_box[3])

        # combo box 5
        self._combo_box[4].move(0, 120)
        self._combo_box[4].activated[str].connect(self.user_choice_five)
        self.layout.addWidget(self._combo_box[4])

        # combo box 6
        self._combo_box[5].move(0, 150)
        self._combo_box[5].activated[str].connect(self.user_choice_six)
        self.layout.addWidget(self._combo_box[5])

    def init_search_button(self):
        '''(Window) -> None
        Initalizes the search button
        '''
        self._search_btn = QtGui.QPushButton('Search', self)
        self.layout.addWidget(self._search_btn)
        self._search_btn.clicked.connect(self.user_choice_search)
        self._search_btn.move(0, 180)

    def init_editor(self):
        '''(Window) -> None
        Intializes the editor pane
        '''
        self._open_editor = QtGui.QTextEdit(self)
        self._open_editor.move(100, 0)
        self._open_editor.resize(200, 210)
        self.layout.addWidget(self._open_editor)

    def output_editor(self, output):
        '''(Window, str) -> None
        '''
        self._open_editor.clear()
        self._open_editor.append(output)

    def user_choice_search(self):
        '''(Window) -> None
        check if the team is within the database then update output pane
        '''
        user_input_empty = False
        for user_input in self._user_input:
            if(user_input == ''):
                user_input_empty = True

        if(user_input_empty is False):
            query = self._database.query(self._user_input)
            if(query is not None):
                self.output_editor(str(query))
            else:
                self.output_editor(str(self._user_input) + '\n' + 'sorry')

    def user_choice_one(self, text):
        '''(Window) -> None'''
        self._user_input[0] = text.strip()

    def user_choice_two(self, text):
        '''(Window) -> None'''
        self._user_input[1] = text.strip()

    def user_choice_three(self, text):
        '''(Window) -> None'''
        self._user_input[2] = text.strip()

    def user_choice_four(self, text):
        '''(Window) -> None'''
        self._user_input[3] = text.strip()

    def user_choice_five(self, text):
        '''(Window) -> None'''
        self._user_input[4] = text.strip()

    def user_choice_six(self, text):
        '''(Window) -> None'''
        self._user_input[5] = text.strip()


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
