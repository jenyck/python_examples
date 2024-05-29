#!/usr/bin/env python3
'''ОРФОЭПИЧЕСКИЙ ТРЕНАЖЕР (ЗАДАНИЕ 4 ЕГЭ)'''
import random
import sys

nouns = {'аэропорты': 'аэропОрты', 'банты': 'бАнты', 'бороду': 'бОроду',
         'бухгалтеров': 'бухгАлтеров', 'вероисповедание': 'вероисповЕдание',
         'водопровод': 'водопровОд', 'газопровод': 'газопровОд',
         'гражданство': 'граждАнство', 'дефис': 'дефИс', 'дешевизна': 'дешевИзна',
         'диспансер': 'диспансЕр', 'договоренность': 'договорЁнность',
         'документ': 'докумЕнт', 'досуг': 'досУг', 'еретик': 'еретИк',
         'жалюзи': 'жалюзИ', 'значимость': 'знАчимость', 'иксы': 'Иксы',
         'каталог': 'каталОг', 'квартал': 'квартАл', 'километр': 'киломЕтр',
         'конусов': 'кОнусов', 'корысть': 'корЫсть', 'краны': 'крАны',
         'кремень': 'кремЕнь', 'кремня': 'кремнЯ', 'лекторов': 'лЕкторов',
         'локтя': 'лОктя', 'локтей': 'локтЕй', 'лыжня': 'лыжнЯ',
         'местностей': 'мЕстностей', 'намерение': 'намЕрение',
         'нарост': 'нарОст', 'недруг': 'нЕдруг', 'недуг': 'недУг',
         'некролог': 'некролОг', 'ненависть': 'нЕнависть',
         'нефтепровод': 'нефтепровОд', 'новостей': 'новостЕй',
         'ногтя': 'нОгтя', 'ногтей': 'ногтЕй', 'отрочество': 'Отрочество',
         'партер': 'партЕр', 'портфель': 'портфЕль', 'поручни': 'пОручни',
         'приданое': 'придАное', 'призыв': 'призЫв', 'свекла': 'свЁкла',
         'сироты': 'сирОты', 'созыв': 'созЫв',
         'сосредоточение': 'сосредотОчение', 'средства': 'срЕдства',
         'статуя': 'стАтуя', 'столяр': 'столЯр', 'таможня': 'тамОжня',
         'торты': 'тОрты', 'туфля': 'тУфля', 'цемент': 'цемЕнт',
         'центнер': 'цЕнтнер', 'цепочка': 'цепОчка', 'шарфы': 'шАрфы',
         'шофер': 'шофЁр', 'эксперт': 'экспЕрт'}

adjectives = {'верна': 'вернА', 'значимый': 'знАчимый',
              'красивее': 'красИвее', 'красивейший': 'красИвейший',
              'кухонный': 'кУхонный', 'ловка': 'ловкА',
              'мозаичный': 'мозаИчный', 'оптовый': 'оптОвый',
              'прозорливый': 'прозорлИвый', 'прозорлива': 'прозорлИва',
              'сливовый': 'слИвовый'}

verbs = {'брала': 'бралА', 'бралась': 'бралАсь', 'взяла': 'взялА',
         'взялась': 'взялАсь', 'влилась': 'влилАсь', 'ворвалась': 'ворвалАсь',
         'воспринять': 'воспринЯть', 'восприняла': 'воспринялА',
         'воссоздала': 'воссоздалА', 'вручит': 'вручИт', 'гнала': 'гналА',
         'гналась': 'гналАсь', 'добрала': 'добралА', 'добралась': 'добралАсь',
         'дождалась': 'дождалАсь', 'дозвонится': 'дозвонИтся',
         'дозировать': 'дозИровать', 'ждала': 'ждалА', 'жилось': 'жилОсь',
         'закупорить': 'закУпорить', 'занять': 'занЯть', 'занял': 'зАнял',
         'заняла': 'занялА', 'заняли': 'зАняли', 'заперла': 'заперлА',
         'запломбировать': 'запломбировАть', 'защемит': 'защемИт',
         'звала': 'звалА', 'звонит': 'звонИт', 'кашлянуть': 'кАшлянуть',
         'клала': 'клАла', 'клеить': 'клЕить', 'кралась': 'крАлась',
         'кровоточить': 'кровоточИть', 'лгала': 'лгалА', 'лила': 'лилА',
         'лилась': 'лилАсь', 'наврала': 'навралА', 'наделит': 'наделИт',
         'надорвалась': 'надорвалАсь', 'назвалась': 'назвалАсь',
         'накренится': 'накренИтся', 'налила': 'налилА', 'нарвала': 'нарвалА',
         'начать': 'начАть', 'обзвонит': 'обзвонИт', 'облегчить': 'облегчИть',
         'облегчит': 'облегчИт', 'облилась': 'облилАсь',
         'обнялась': 'обнялАсь', 'обогнала': 'обогналА',
         'ободрала': 'ободралА', 'ободрить': 'ободрИть', 'ободрит': 'ободрИт',
         'ободриться': 'ободрИться', 'ободрится': 'ободрИтся',
         'обострить': 'обострИть', 'одолжить': 'одолжИть',
         'одолжит': 'одолжИт', 'озлобить': 'озлОбить', 'оклеить': 'оклЕить',
         'окружит': 'окружИт', 'опошлить': 'опОшлить',
         'осведомиться': 'освЕдомиться', 'осведомится': 'освЕдомится',
         'отбыла': 'отбылА', 'отдала': 'отдалА', 'откупорить': 'откУпорить',
         'отозвала': 'отозвалА', 'отозвалась': 'отозвалАсь',
         'перезвонит': 'перезвонИт', 'перелила': 'перелилА',
         'плодоносить': 'плодоносИть', 'пломбировать': 'пломбировАть',
         'повторит': 'повторИт', 'позвала': 'позвалА',
         'позвонит': 'позвонИт', 'полила': 'полилА', 'положить': 'положИть',
         'понять': 'понЯть', 'поняла': 'понялА', 'послала': 'послАла',
         'прибыть': 'прибЫть', 'прибыл': 'прИбыл', 'прибыла': 'прибылА',
         'прибыли': 'прИбыли', 'принять': 'принЯть', 'принял': 'прИнял',
         'приняла': 'принялА', 'приняли': 'прИняли', 'рвала': 'рвалА',
         'сверлит': 'сверлИт', 'сняла': 'снялА', 'соврала': 'совралА',
         'создала': 'создалА', 'сорвала': 'сорвалА', 'сорит': 'сорИт',
         'убрала': 'убралА', 'углубить': 'углубИть', 'укрепит': 'укрепИт',
         'черпать': 'чЕрпать', 'щемит': 'щемИт', 'щелкать': 'щЁлкать'}

partipicles = {'довезенный': 'довезЁнный', 'загнутый': 'зАгнутый',
               'занятый': 'зАнятый', 'занята': 'занятА',
               'запертый': 'зАпертый', 'заселенный': 'заселЁнный',
               'заселена': 'заселенА', 'кормящий': 'кормЯщий',
               'кровоточащий': 'кровоточАщий', 'наживший': 'нажИвший',
               'наливший': 'налИвший', 'нанявшийся': 'нанЯвшийся',
               'начавший': 'начАвший', 'начатый': 'нАчатый',
               'низведенный': 'низведЁнный', 'облегченный': 'облегчЁнный',
               'ободренный': 'ободрЁнный', 'обостренный': 'обострЁнный',
               'отключенный': 'отключЁнный', 'повторенный': 'повторЁнный',
               'поделенный': 'поделЁнный', 'понявший': 'понЯвший',
               'принятый': 'прИнятый', 'принята': 'принятА',
               'прирученный': 'приручЁнный', 'проживший': 'прожИвший',
               'снята': 'снятА', 'согнутый': 'сОгнутый',
               'углубленный': 'углублЁнный'}

adverbs = {'закупорив': 'закУпорив', 'начав': 'начАв',
           'начавшись': 'начАвшись', 'отдав': 'отдАв', 'подняв': 'поднЯв',
           'поняв': 'понЯв', 'прибыв': 'прибЫв', 'создав': 'создАв',
           'вовремя': 'вОвремя', 'доверху': 'дОверху', 'донельзя': 'донЕльзя',
           'донизу': 'дОнизу', 'досуха': 'дОсуха', 'засветло': 'зАсветло',
           'затемно': 'зАтемно', 'красивее': 'красИвее', 'надолго': 'надОлго',
           'ненадолго': 'ненадОлго'}

print('ОРФОЭПИЧЕСКИЙ ТРЕНАЖЕР (ЗАДАНИЕ 4 ЕГЭ)')
print('Добро пожаловать в тренажер!')
print('Пользоваться им очень просто: вам будут по очереди выводиться слова,')
print('в ответ это слово нужно переписать, выделив ударение заглавной буквой.')
print('Например, на вывод "привет" ваш правильный ответ будет "привЕт".')
print('Чтобы закончить работу, введите "выйти".')
print('Чтобы посмотреть, в каких словах вы допускали ошибки в течение работы,')
print('введите "статистика"')
print()

word = ''
corr = incorr = 0
mist = []
iteration = 0

# здесь можно изменить словарь, из которого выбираете слова
words = list(verbs.items())
random.shuffle(words)

# не забудьте изменить текст вывода, изменяя часть речи
print('Из доступных частей речи выбраны глаголы,',
      'отредактировав текст программы, можно это изменить.')
print('Вы будете тренировать', len(words), 'слов в этот раз.')
print('Это значит, что через', len(words),
      'слов они повторятся, но в другом порядке.')
print()

while word != 'выйти':
    out, ans = words[iteration]
    word = input(out + '\n')
    # дан верный ответ
    if word == ans:
        corr += 1
        print('ВЕРНО', file=sys.stderr)
    # пользователь запросил статистику
    elif word.lower() == 'статистика':
        print('В текущей сессии вами было дано ' + str(corr) +
              ' правильных и ' + str(incorr) + ' неправильных ответов.')
        if mist:
            print('Следующие слова были неправильно написаны:')
            print(*mist)
        print()
        print('Продолжим тренировать ударения в словах...')
    # дан неверный ответ
    elif word != 'выйти':
        mist.append(ans)
        incorr += 1
        print('НЕВЕРНО, правильный ответ:', ans, file=sys.stderr)

    iteration += 1
    if iteration >= len(words):
        random.shuffle(words)
        iteration = 0
        print('Теперь слова будут повторяться в другом порядке.')