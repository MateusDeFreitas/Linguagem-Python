times = ('bota fogo','palmeiras','fluminence','atletico','cruzeiro',
         'flamengo','athletico','são paulo','santos','gremio','fortaleza',
         'bragantino','bahia','cuiaba','internacional','goias','vasco da gama'
         ,'corinthians','américa','coritiba')

print("------------------------------------------")
print('lista de times do brasileirâo:',times)
print("------------------------------------------")
print("os 5 primeiros times são:",times[:6])
print("------------------------------------------")
print("os 4 últimos times são:",times[21:15:-1])
print("------------------------------------------")
print("os times em ordem alfabética ficam:",sorted(times))
print("------------------------------------------")
print("o corinthians esta na",times.index('corinthians'),"posição")