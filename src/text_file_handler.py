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

from team import team
import glob

def parse_file(file):
  ''' (IO.TextWrapper) -> team
  '''
  team_description = ''
  team_members = []
  team_sets = {}
  # we will not start reading the team's description
  line = file.readline() # at this point it should be equal to \
                         # 'description-start-line'
  while(line != 'team-start-line\n'):
        if(line != '\n' and line != 'description-start-line\n'):
           team_description += line
           #print(line,end='')
        line = file.readline()
  # we will now start reading in the actual team
  line = file.readline()
  while(line != ''):
      pokemon_info = []
      while(line != '\n'):
          pokemon_info.append(line)
          line = file.readline()

      pokemon_name = pokemon_info[0][:pokemon_info[0].index('@')-1]
      team_members.append(pokemon_name)

      set_info = ''
      for i in pokemon_info:
         set_info += str(i)

      team_sets[pokemon_name] = set_info
      #print(team_sets[pokemon_name])
      line = file.readline()
  # now to finalize the current team and return
  ret = team(team_description, team_members, team_sets)
  return ret

def retrieve_teams():
  ''' () -> list of team object
  '''
  file_paths = glob.glob('..//database//overused//*.txt')
  ret = []
  current_path = ''
  try:
      for path in file_paths:
          file = open(path)
          current_path = path
          ret.append(parse_file(file))
  except Exception as e:
     print(current_path)
     print(e)
  return ret


# debugging happens here
if __name__ == '__main__':
   ret = retrieve_teams()
   team = ret[0]
   print(team.getTeamMembers())
   print(team.getTeamMembers())
   #print)
