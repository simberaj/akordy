import sys, os, locale, re, collections
locale.setlocale(locale.LC_ALL, '')

class Index:
  NUMERIC_KEY = '1-9'
  NAME_PATTERN = re.compile(r'(?<=\\beginsong\{).*?(?=\})')
  ARTIST_PATTERN = re.compile(r'(?<=\[by\=\{).*?(?=\}\])')

  def __init__(self, directory, extension='tex'):
    self.index = self.groupByStarts(self.extractNames(self.loadFiles(directory, restrict=('.' + extension))))
  
  @staticmethod
  def loadFiles(directory, restrict=None):
    for fn in sorted(os.listdir(directory), key=locale.strxfrm):
      if restrict and restrict not in fn: continue # exclude all non-tex files
      with open(os.path.join(sys.argv[1], fn), encoding='utf8') as fin:
        yield fin.readline() # first line is where the title and artist is written
  
  def extractNames(self, lines):
    names = []
    for firstline in lines:
      nameMatch = self.NAME_PATTERN.search(firstline)
      artistMatch = self.ARTIST_PATTERN.search(firstline)
      if nameMatch is None:
        continue
      else:
        names.append((nameMatch.group(0), None if artistMatch is None else artistMatch.group(0)))
    return names
  
  def groupByStarts(self, names):
    index = collections.defaultdict(list)
    # input: list of 2-tuples (title, artist)
    for i in range(len(names)):
      title = names[i][0]
      key = title[0:2] if title.upper().startswith('CH') else title[0]
      index[key].append([title, None])
      if i != 0 and title == names[i-1][0]:
        index[key][-1][1] = names[i][1] # add artist discrimination
        index[key][-2][1] = names[i-1][1]
    for key in list(index.keys()):
      if not key.isalpha(): # group all titles starting with digits to one
        index[self.NUMERIC_KEY].extend(index[key])
        del index[key]
    if self.NUMERIC_KEY in index:
      index[self.NUMERIC_KEY].sort()
    return index
  
  def outTex(self):
    lines = []
    orders = [title for letteritem in self.index.values() for title, artist in letteritem]
    orders.sort(key=locale.strxfrm)
    for key in sorted(self.index, key=locale.strxfrm):
      lines.append('\\begin{idxblock}{' + key + '}')
      for title, artist in self.index[key]:
        lines.append(self.entryTex(title, artist, orders.index(title) + 1))
      lines.append('\\end{idxblock}')
    return '\n'.join(lines)
  
  def entryTex(self, title, artist, i):
    if artist is None:
      name = title
    else:
      name = title + ' \\emph{(' + artist + ')}'
    return '\\idxentry{%s}{\\hyperlink{song-%i}{\\pageref*{song-%i}}}' % (name, i, i)
    
  def writeTex(self, outfn):
    with open(outfn, 'w', encoding='utf8') as fileout:
      fileout.write(self.outTex())

  
if __name__ == '__main__':
  Index(sys.argv[1]).writeTex(sys.argv[2])
    