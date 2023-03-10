import re
import heapq
import yaml
import numpy as np
punctuation_ = r''',"'()*+,-:«»;<=>@[\\]^_`{|}~'''

# with open('latest_silero_models.yml', 'r', encoding="utf8") as yaml_file:
#     models = yaml.load(yaml_file, Loader=yaml.SafeLoader)
# model_conf = models.get('te_models').get('latest')
#
# # see avaiable languages
# available_languages = list(model_conf.get('languages'))
# print(f'Available languages {available_languages}')
#
# # and punctuation marks
# available_punct = list(model_conf.get('punct'))
# print(f'Available punctuation marks {available_punct}')

text_first = r"1. Президент Путин: развязал:  Путин Путин несправедливую, агрессивную войну против Украины под нелепыми предлогами. Он отчаянно пытается придать этой войне статус «народной», стремясь сделать своими сообщниками всех граждан России, однако его попытки терпят крах. Добровольцев для этой войны почти нет, поэтому путинская армия опирается на заключенных и принудительно мобилизованных. 2. Реальные причины войны — политические и экономические проблемы внутри России, стремление Путина удержать власть любой ценой, а также его одержимость своим историческим наследием. Он хочет войти в историю как «царь-завоеватель» и «собиратель земель». 3. Убиты десятки тысяч невиновных украинцев, боль и страдания обрушены на миллионы. Совершены военные преступления. Разрушены города и инфраструктура Украины. 4. Россия терпит военное поражение. Именно осознание этого изменило риторику властей от «Киев за три дня» до истерических угроз применить ядерное оружие в случае проигрыша. Бессмысленно загублены жизни десятков тысяч российских солдат. Окончательное военное поражение можно отсрочить ценой жизни еще сотен тысяч мобилизованных, но в целом оно неизбежно. Комбинация «агрессивная война + коррупция + бездарность генералов + слабая экономика + героизм и высокая мотивация обороняющихся» результатом выдает только поражение. Лживые и лицемерные призывы Кремля к переговорам и прекращению огня — не что иное, как реалистичная оценка перспектив военных действий."
text = r"1. Президент Путин: развязал:  Путин Путин несправедливую, агрессивную войну против Украины под нелепыми предлогами. Он отчаянно пытается придать этой войне статус «народной», стремясь сделать своими сообщниками всех граждан России, однако его попытки терпят крах. Добровольцев для этой войны почти нет, поэтому путинская армия опирается на заключенных и принудительно мобилизованных. 2. Реальные причины войны — политические и экономические проблемы внутри России, стремление Путина удержать власть любой ценой, а также его одержимость своим историческим наследием. Он хочет войти в историю как «царь-завоеватель» и «собиратель земель». 3. Убиты десятки тысяч невиновных украинцев, боль и страдания обрушены на миллионы. Совершены военные преступления. Разрушены города и инфраструктура Украины. 4. Россия терпит военное поражение. Именно осознание этого изменило риторику властей от «Киев за три дня» до истерических угроз применить ядерное оружие в случае проигрыша. Бессмысленно загублены жизни десятков тысяч российских солдат. Окончательное военное поражение можно отсрочить ценой жизни еще сотен тысяч мобилизованных, но в целом оно неизбежно. Комбинация «агрессивная война + коррупция + бездарность генералов + слабая экономика + героизм и высокая мотивация обороняющихся» результатом выдает только поражение. Лживые и лицемерные призывы Кремля к переговорам и прекращению огня — не что иное, как реалистичная оценка перспектив военных действий."
for p in text:
    if p in punctuation_:
        text = text.replace(p, '')
print(text)
# sentences_first = re.split(r' *[\.?!][\'"\)\]]* *', text_first)
sentences_first = re.split(r' *[\.?!][\'"\)\]]* *', text_first)
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
# sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
print(sentences)
clean_text = text.lower()
word_tokenize = clean_text.split()
# print(word_tokenize)

# стоп-слова рус яз
stop_words = ["а","е","и","ж","м","о","на","не","ни","об","но","он","мне","мои","мож","она","они","оно","мной","много","многочисленное","многочисленная","многочисленные","многочисленный","мною","мой","мог","могут","можно","может","можхо","мор","моя","моё","мочь","над","нее","оба","нам","нем","нами","ними","мимо","немного","одной","одного","менее","однажды","однако","меня","нему","меньше","ней","наверху","него","ниже","мало","надо","один","одиннадцать","одиннадцатый","назад","наиболее","недавно","миллионов","недалеко","между","низко","меля","нельзя","нибудь","непрерывно","наконец","никогда","никуда","нас","наш","нет","нею","неё","них","мира","наша","наше","наши","ничего","начала","нередко","несколько","обычно","опять","около","мы","ну","нх","от","отовсюду","особенно","нужно","очень","отсюда","в","во","вон","вниз","внизу","вокруг","вот","восемнадцать","восемнадцатый","восемь","восьмой","вверх","вам","вами","важное","важная","важные","важный","вдали","везде","ведь","вас","ваш","ваша","ваше","ваши","впрочем","весь","вдруг","вы","все","второй","всем","всеми","времени","время","всему","всего","всегда","всех","всею","всю","вся","всё","всюду","г","год","говорил","говорит","года","году","где","да","ее","за","из","ли","же","им","до","по","ими","под","иногда","довольно","именно","долго","позже","более","должно","пожалуйста","значит","иметь","больше","пока","ему","имя","пор","пора","потом","потому","после","почему","почти","посреди","ей","два","две","двенадцать","двенадцатый","двадцать","двадцатый","двух","его","дел","или","без","день","занят","занята","занято","заняты","действительно","давно","девятнадцать","девятнадцатый","девять","девятый","даже","алло","жизнь","далеко","близко","здесь","дальше","для","лет","зато","даром","первый","перед","затем","зачем","лишь","десять","десятый","ею","её","их","бы","еще","при","был","про","процентов","против","просто","бывает","бывь","если","люди","была","были","было","будем","будет","будете","будешь","прекрасно","буду","будь","будто","будут","ещё","пятнадцать","пятнадцатый","друго","другое","другой","другие","другая","других","есть","пять","быть","лучше","пятый","к","ком","конечно","кому","кого","когда","которой","которого","которая","которые","который","которых","кем","каждое","каждая","каждые","каждый","кажется","как","какой","какая","кто","кроме","куда","кругом","с","т","у","я","та","те","уж","со","то","том","снова","тому","совсем","того","тогда","тоже","собой","тобой","собою","тобою","сначала","только","уметь","тот","тою","хорошо","хотеть","хочешь","хоть","хотя","свое","свои","твой","своей","своего","своих","свою","твоя","твоё","раз","уже","сам","там","тем","чем","сама","сами","теми","само","рано","самом","самому","самой","самого","семнадцать","семнадцатый","самим","самими","самих","саму","семь","чему","раньше","сейчас","чего","сегодня","себе","тебе","сеаой","человек","разве","теперь","себя","тебя","седьмой","спасибо","слишком","так","такое","такой","такие","также","такая","сих","тех","чаще","четвертый","через","часто","шестой","шестнадцать","шестнадцатый","шесть","четыре","четырнадцать","четырнадцатый","сколько","сказал","сказала","сказать","ту","ты","три","эта","эти","что","это","чтоб","этом","этому","этой","этого","чтобы","этот","стал","туда","этим","этими","рядом","тринадцать","тринадцатый","этих","третий","тут","эту","суть","чуть","тысяч"]
word2count = {}
for word in word_tokenize:
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
print(word2count)

# взвешенная гистограмма
for key in word2count.keys():
    word2count[key] = word2count[key] / max(word2count.values()) # насколько частовстречается данное слово, относительно САМОГ7О частовстречаемого

sent2score = {}
# mapping = {} #хранит индексы, прошедших по длинне предложений
# c = 0 #хранит кол-во индексов, прошедших по длинне предложений
for sentence in sentences:
    # increment = False
    for word in sentence.split():
        if word in word2count.keys():
            if len(sentence.split(' ')) < 28 and len(sentence.split(' ')) > 9:
                # if c not in mapping.keys():
                #     mapping[c] = i
                #     increment = True
                if sentence not in sent2score.keys():
                    sent2score[sentence] = word2count[word]#сумма рейтингов слов в конкретном предложении, получили рейтинг предложения
                else:
                    sent2score[sentence] += word2count[word]
    # if increment:
    #     c += 1

# idx = np.flip(np.argsort(list(sent2score.values())))
# idx_best = idx[:3] #лучшие 3 предложения+их индексы в text_first
# idx_best_orig = [mapping[i] for i in idx_best]
# best_three_sentences = [sentences_first[i] for i in idx_best_orig]
# best_three_sentences = '. '.join(best_three_sentences)

best_three_sentences = heapq.nlargest(3, sent2score, key=sent2score.get)
# print(best_three_sentences)
# a = best_three_sentences[0]
print(*best_three_sentences)
