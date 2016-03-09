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

class Team(object):
  '''This class will hold a brief team description and the members of the each
  respective team along with their sets.
  '''


  def __init__(self, team_description, team_members, team_sets):
    '''(Team, str, [str], {str:str}) -> None
    Creates a basic team
    '''
    self._team_description = team_description
    self._team_members = team_members
    self._team_sets = team_sets
    self._team_members.sort() # we do this to help with the hashing


  def __hash__(self):
    '''(Team) -> None
    Uses pythons built in hash function to make a hash for the team
    '''
    return hash(str(team_members))


  def __str__(self):
    ''' (Team) -> None
    Returns a string representaiton of everything
    '''
    ret = 'Team Description:\n'
    ret += str(self._team_description) + '\n'
    ret += 'Team Sets:\n'
    for i in range(len(self._team_members)):
        ret += str(self._team_sets[self._team_members[i]]) + '\n'
    return ret

  # getters and setters
  def getTeamDescription(self):
      return self._team_description

  def setTeamDescription(self, team_description):
      self._team_description = team_description

  def getTeamMembers(self):
      return self._team_members

  def setTeamMembers(self, team_members):
      self._team_members = _team_members

  def getTeamSets(self,team_sets):
      self._team_sets = team_sets




# debugging goes on here
if __name__ == '__main__':
   sample_set = 'Azumarill @ Choice Band \n \
                Ability: Huge Power \n \
                EVs: 172 HP / 252 Atk / 84 Spe \n \
                Adamant Nature \n \
                - Play Rough \n \
                - Waterfall \n \
                - Aqua Jet\n \
                - Superpower'
   team_description = 'testing team'
   team_members = ['azumarill','charizard']
   team_sets = {'azumarill':sample_set,'charizard':'dragon claw'}
   myteam = Team(team_description,team_members,team_sets)
   database = {myteam:1}
   print(myteam)