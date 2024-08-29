from audioop import reverse


Q, NL, CD = input().split()
Q=int(Q)
Pokedex={}
PokedexAux={}
for c in range(Q):
    Pokemon , Forca = input().split()
    Forca = int(Forca)
    Pokedex[Pokemon]=Forca
    PokedexAux[Forca]=Pokemon
if NL == 'N':
    if CD == 'C':
        for c in sorted(Pokedex.keys()):
            print(c, Pokedex[c])
    if CD == 'D':
         for c in reversed(sorted(Pokedex.keys())):
            print(c, Pokedex[c])
if NL == 'L':
    if CD == 'C':
        for c in sorted(PokedexAux.keys()):
            print(PokedexAux[c], c)
    if CD == 'D':
         for c in reversed(sorted(PokedexAux.keys())):
            print(PokedexAux[c], c)