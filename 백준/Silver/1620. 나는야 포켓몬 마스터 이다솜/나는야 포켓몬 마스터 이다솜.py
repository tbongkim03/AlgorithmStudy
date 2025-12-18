import sys
input=sys.stdin.readline
n, m = map(int, input().split())
pokedex_name={}
pokedex_num={}
for i in range(n):
    pokemon = input()
    pokemon = pokemon.strip()
    pokedex_name[pokemon]=str(i+1)
    pokedex_num[str(i+1)]=pokemon
for _ in range(m):
    quiz=input().strip()
    if quiz in pokedex_name:
        print(pokedex_name[quiz])
    else:
        print(pokedex_num[quiz])