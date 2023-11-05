python -c "import sys; print('\n'.join('\t'.join(c) for c in zip(*(l.split('\t') for l in sys.stdin.readlines() if l.strip()))))" < pH_gR.txt >PH_GR.txt
