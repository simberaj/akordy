import sys, os, locale
locale.setlocale(locale.LC_ALL, '')

init = os.path.join(os.path.dirname(sys.argv[0]), 'init.tex')

if __name__ == '__main__':
  with open(sys.argv[2], 'w', encoding='utf8') as fout:
    fout.write(open(init, encoding='utf8').read())
    for fn in sorted(os.listdir(sys.argv[1]), key=locale.strxfrm):
      if '.tex' not in fn: continue
      with open(os.path.join(sys.argv[1], fn), encoding='utf8') as fin:
        fout.write(fin.read() + '\n')
    fout.write('\n\\end{songs}\n\\end{document}\n')
