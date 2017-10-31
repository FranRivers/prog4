import asyncio
import random

def letras():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    yield 'E'
    yield 'F'
    yield 'G'
    yield 'H'
    yield 'I'
    yield 'J'
    yield 'K'
    yield 'L'
    yield 'M'

def num():

    numa = 1

    while True:
        yield numa
        numa = numa + 2

# @asyncio.coroutine
# def num_impares():
#     numero_final = 100
#     numero = 0
#     while True:
#         numero = numero + 1
#
#         if numero%2 == 0:
#             yield numero
#             if (numero_final == 100):
#                 break
#         yield from asyncio.sleep(random.randint(0, 5))


if __name__=='__main__':
    generador = letras()
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))
    print(next(generador))

    nume = num()

    for n in nume:
        if n > 100:
            break
        else:
            print(n)


    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(num_impares())
    # # asyncio.ensure_future(num_impares())
    # # asyncio.ensure_future(num_impares())
    # # loop.run_forever()
    #
    # # for n in num_impares():
    # #
    # #     if n > 100:
    # #         break
    # #     else :
    # #         print(n)