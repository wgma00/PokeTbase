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
# SOFTWARE.

import text_file_handler

class Database(object):
  ''' This class will hold all available teams currently in the forum
  '''
  def __init__(self):
    ''' default constructor
        we will just have a list of
    '''
    self._teams = text_file_handler.retrieve_teams()
    self._database = {}
    for team in self._teams:
        self._database[str(team.getTeamMembers())] = team

  def query(self, team):
    ''' ([str]) -> team
        checks if the team is in the database
    '''
    # sort team to make hash compliant with the database's hashses
    team.sort()
    team = str(team)
    if team in self._database:
        return self._database[team]
    else:
        return None


if __name__ == '__main__':
  d = Database()
  q = ['Excadrill', 'Heatran', 'Latios-Mega (M)', 'Manaphy', 'Tangrowth', \
  'Tyranitar']
  q = ['Azumarill', 'Garchomp', 'Heatran', 'Latias', 'Reuniclus', 'Venusaur']
  print(d.query(q))
  # Yay, I'm finally done (It was almost 7am when I finished this, please
  # understand my joy)

