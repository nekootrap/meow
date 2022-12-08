
def word(message):
    w = list('мышка')
    wd = ['_', '_', '_', '_', '_']
    print(f'Загаданное слово {wd}')
    user_number = message.strip('/')
    if user_number in w:
        print(f'Верно ты угадала {w.find(user_number)} букву!')
        ind = wd.index(user_number)
        wd = wd.insert(ind, w[ind])
        wd.remove('_')
        
message = input()
print(word('м'))