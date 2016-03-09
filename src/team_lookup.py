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

from team_database import Database

def main():
  d = Database()
  print('Welcome to the team lookup!')
  print('Here we will check if a team is currently within our database')
  print('All you have to do is enter the name of six pokemon and we will check')
  print('If at any moment you want to quit simply type \'qq\' without the \' ')
  user_input = ''
  while(user_input != 'qq'):

    user_query = []
    print('Please enter 6 pokemon, 1 per line')
    consent = input('press qq or y to continue\n')
    if(consent == 'qq'):
       break
    for i in range(6):
       pokemon = input()
       user_query.append(pokemon)
    output = d.query(user_query)
    print()
    if(output != None):
       print(output)
    else:
       print('Sorry, we did\'t find anything.')
    user_input = input()

# do your testing here
if __name__ == '__main__':
    main()