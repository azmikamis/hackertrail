import itertools

class Game(object):
  def __init__(self, sizex, sizey):
    self.sizex = sizex
    self.sizey = sizey
    self.livecells = set()

  def advance(self, livecells=None):
    if livecells is not None:
      self.livecells = livecells
    else:
      newlivecells = set()
      neighbours = [self.neighbours(point) for point in self.livecells]
      uniqueneighbours = set(itertools.chain(*neighbours))
      cellstotransit = self.livecells.union(uniqueneighbours)
      for point in cellstotransit:
        liveneighbours = [(neighbour in self.livecells) \
        for neighbour in self.neighbours(point)]
        count = sum(liveneighbours)
        if count == 3 or (count == 2 and point in self.livecells):
          newlivecells.add(point)
      self.livecells = newlivecells

  def neighbours(self, point):
    col, row = point
    leftcol = (col == 0 and [self.sizex-1] or [col-1])[0]
    rightcol = (col == self.sizex-1 and [0] or [col+1])[0]
    toprow = (row == 0 and [self.sizey-1] or [row-1])[0]
    bottomrow = (row == self.sizey-1 and [0] or [row+1])[0]

    yield rightcol, row
    yield leftcol, row
    yield col, bottomrow
    yield col, toprow
    yield rightcol, bottomrow
    yield rightcol, toprow
    yield leftcol, bottomrow
    yield leftcol, toprow

  def printgame(self):
    for i in range(self.sizey):
      printrow = ''
      for j in range(self.sizex):
        if (i,j) not in self.livecells:
          printrow += '0'
        else:
          printrow += '1'
      print printrow

def main():
  t = int(raw_input())
  startsetlist = []
  for _ in range(t):
    startset = set()
    for j in range(5):
      k = 0
      gamerow = raw_input()
      for c in gamerow:
        if c == '1':
          startset.add((k,j))
    startsetlist.append(startset)
  for start in startsetlist:
    game = Game(5, 5)
    game.advance(start)
  for i in range(100):
    game.advance()
  if len(game.livecells) > 0:
    print 'YES'
  else:
    print 'NO'
