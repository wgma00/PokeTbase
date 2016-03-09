# Copyright (c) 2016 William Granados
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
#!/usr/bin/python

import sys
from team_database import Database
from team import Team
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
    
    def __init__(self):
        # members
        self._user_input = ['' for i in range(6)]
        self._database = Database()
        # gui members
        super(Window, self).__init__()
        self.init_UI()             
        self.init_dropdown_menu() 
        self.init_search_button()
        self.show()
        
        
    def init_UI(self):
        '''(Window) -> None
        Sets the dimensions and user interface
        '''
        self.setGeometry(150, 150, 500, 300)
        self.setWindowTitle('PokéTbase - Pokémon Team Database')
        self.setWindowIcon(QtGui.QIcon('../res/icon/pikachu_icon.png'))
        
    def init_dropdown_menu(self):
        ''' (Window) -> None
        Sets up the input the user can give
        '''
        file = open("../res/pokemon-names/pokemon-names.txt")
        pokemon_names = []
        for name in file:
            pokemon_names.append(name)
        # create 6 combo boxes since there are 6 members on a team
        combo_box = [QtGui.QComboBox(self) for x in range(6)]
        for name in pokemon_names:
            for i in range(6):
                combo_box[i].addItem(name)
                
        # set up each user input individually
        
        # combo box 1
        combo_box[0].move(0, 0)
        combo_box[0].activated[str].connect(self.user_choice_one)
        
        # combo box 2
        combo_box[1].move(0, 30)
        combo_box[1].activated[str].connect(self.user_choice_two)  
        
        # combo box 3
        combo_box[2].move(0, 60)
        combo_box[2].activated[str].connect(self.user_choice_three)  
        
        # combo box 4
        combo_box[3].move(0, 90)
        combo_box[3].activated[str].connect(self.user_choice_four)  
        
        # combo box 5
        combo_box[4].move(0, 120)
        combo_box[4].activated[str].connect(self.user_choice_five) 
        
        # combo box 6
        combo_box[5].move(0, 150)
        combo_box[5].activated[str].connect(self.user_choice_six)    
        
    def init_search_button(self):
        '''(Window) -> None
        initalize the search button
        '''
        btn = QtGui.QPushButton('Search', self)
        btn.clicked.connect(self.user_choice_search)
        btn.move(0, 180)
        
    
        
    def user_choice_search(self):
        '''(Window) -> None
        check if the team is within the database then update output pane
        '''
        user_input_empty = False
        for user_input in self._user_input:
            if(user_input == ''):
                user_input_empty = True
                
        if(user_input_empty == False):
            query = self._database.query(self._user_input)
            if(query != None):
                print(query)
        
        
    def user_choice_one(self, text):
        '''(Window) -> None'''
        self._user_input[0] = text
        
    def user_choice_two(self, text):
        '''(Window) -> None'''
        self._user_input[1] = text
    
    def user_choice_three(self, text):
        '''(Window) -> None'''
        self._user_input[2] = text   
        
    def user_choice_four(self, text):
        '''(Window) -> None'''
        self._user_input[3] = text  
        
    def user_choice_five(self, text):
        '''(Window) -> None'''
        self._user_input[4] = text  
        
    def user_choice_six(self, text):
        '''(Window) -> None'''
        self._user_input[5] = text       


def main():

    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()