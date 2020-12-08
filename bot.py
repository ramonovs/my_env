import telebot
import configure

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(content_types=['text'])
def get_text(message):
    if message.text.lower() == 'привет':
        client.send_message(message.chat.id, 'Привет, я помогу тебе расшифровать аббревиатуры, часто используемые в '
                                             'Почте! Напиши, какое сокращение ты хочешь расшифровать.')
    elif message.text.lower() == 'а/я':
        client.send_message(message.chat.id, 'Абонентский ящик')
    elif message.text.lower() == 'аисуз':
        client.send_message(message.chat.id, 'Автоматизированная информационная система управления закупками')
    elif message.text.lower() == 'ак':
        client.send_message(message.chat.id, 'Арбитражный комитет')
    elif message.text.lower() == 'ао':
        client.send_message(message.chat.id, 'Акционерное общество')
    elif message.text.lower() == 'аопп':
        client.send_message(message.chat.id, 'Авиационное отделение перевозки почты')
    elif message.text.lower() == 'апс':
        client.send_message(message.chat.id, 'Автоматизированная почтовая станция')
    elif message.text.lower() == 'апш':
        client.send_message(message.chat.id, 'Абонирование почтового шкафа. Абонентский почтовый шкаф - специальный '
                                             'шкаф с запирающимися ячейками, устанавливаемый в жилых домах, '
                                             'а также на доставочных участках, предназначенный для получения '
                                             'адресатами почтовых отправлений.')
    elif message.text.lower() == 'арм':
        client.send_message(message.chat.id, 'Автоматизированное рабочее место')
    elif message.text.lower() == 'ас':
        client.send_message(message.chat.id, 'Автоматизированная система')
    elif message.text.lower() == 'асбну':
        client.send_message(message.chat.id, 'Автоматизированная система бухгалтерского и налогового учёта (на базе '
                                             '«1C: Бухгалтерия»)')
    elif message.text.lower() == 'аску':
        client.send_message(message.chat.id, 'Автоматизированная система комплексного учёта (на базе «1C: Бухгалтерия '
                                             '»)')
    elif message.text.lower() == 'асу':
        client.send_message(message.chat.id, 'Автоматизированная система управления, АСУ «Экспресс-3» – '
                                             'автоматизированная система управления пассажирскими перевозками')
    elif message.text.lower() == 'асу рпо':
        client.send_message(message.chat.id, 'Автоматизированная система учета регистрируемых почтовых отправлений')
    elif message.text.lower() == 'асу ип':
        client.send_message(message.chat.id, 'Автоматизированная система управления ИТ-процессами')
    elif message.text.lower() == 'асуп':
        client.send_message(message.chat.id, 'Автоматизированная система управления персоналом')
    elif message.text.lower() == 'асц':
        client.send_message(message.chat.id, 'Автоматизированный сортировочный центр')
    elif message.text.lower() == 'атп':
        client.send_message(message.chat.id, 'Автотранспортные предприятия')
    elif message.text.lower() == 'ауп':
        client.send_message(message.chat.id, 'Аппарат управления Предприятия (совокупность структурных подразделений '
                                             'АО «Почта России», осуществляющих руководство деятельностью всего '
                                             'предприятия)')
    elif message.text.lower() == 'ауф':
        client.send_message(message.chat.id, 'Аппарат управления филиала')
    elif message.text.lower() == 'банк':
        client.send_message(message.chat.id, 'Зона или отдельное помещение в ОПС для оказания финансовых услуг в '
                                             'рамках «Почта Банка»')
    elif message.text.lower() == 'бд':
        client.send_message(message.chat.id, 'База данных')
    elif message.text.lower() == 'бддс':
        client.send_message(message.chat.id, 'Бюджет движения денежных средств')
    elif message.text.lower() == 'бдр':
        client.send_message(message.chat.id, 'Бюджет доходов и расходов')
    elif message.text.lower() == 'бир':
        client.send_message(message.chat.id, 'Бюджет инвестиционных расходов')
    elif message.text.lower() == 'бпб':
        client.send_message(message.chat.id, 'Блок почтового бизнеса')
    elif message.text.lower() == 'бпбиэд':
        client.send_message(message.chat.id, 'Блок посылочного бизнеса и экспресс-доставки')
    elif message.text.lower() == 'бсо':
        client.send_message(message.chat.id, 'Бланки строгой отчетности. Приравниваются к кассовым чекам – бланки '
                                             'квитанций (ф. № 1, ф. № 5, ф. № 47, ф. СП-2), билетов, '
                                             'проездных документов, абонементов и другие документы, предназначенные '
                                             'для осуществления наличных денежных расчетов в случае оказания услуг '
                                             'населению')
    elif message.text.lower() == 'бфб':
        client.send_message(message.chat.id, 'Блок финансового бизнеса')
    elif message.text.lower() == 'вкс':
        client.send_message(message.chat.id, 'Видеоконференция')
    elif message.text.lower() == 'впс':
        client.send_message(message.chat.id, 'Всемирный почтовый союз')
    elif message.text.lower() == 'гжп':
        client.send_message(message.chat.id, 'Газетно-журнальная продукция')
    elif message.text.lower() == 'гзпо':
        client.send_message(message.chat.id, 'Государственные знаки почтовой оплаты')
    elif message.text.lower() == 'гибридный перевод':
        client.send_message(message.chat.id, 'Почтовый перевод ЕСПП, прием и выплата которого осуществляется по «бумажной» технологии')
    elif message.text.lower() == 'гис жкх':
        client.send_message(message.chat.id, 'Государственная информационная система жилищно-коммунального хозяйства')
    elif message.text.lower() == 'гкн':
        client.send_message(message.chat.id, 'Государственный кадастр недвижимости')
    elif message.text.lower() == 'гопс':
        client.send_message(message.chat.id, 'Городское отделение почтовой связи')
    elif message.text.lower() == 'гп':
        client.send_message(message.chat.id, 'Главный пункт; газетная пачка; государственная программа')
    elif message.text.lower() == 'гп еспп':
        client.send_message(message.chat.id, 'Главный пункт Единой системы почтовых переводов')
    elif message.text.lower() == 'гпх':
        client.send_message(message.chat.id, 'Договор гражданско-правового характера')
    elif message.text.lower() == 'гсп':
        client.send_message(message.chat.id, 'Городская служебная почта')
    elif message.text.lower() == 'гтп':
        client.send_message(message.chat.id, 'Группа технической поддержки')
    elif message.text.lower() == 'гцмпп':
        client.send_message(message.chat.id, 'Главный центр магистральных перевозок почты')
    elif message.text.lower() == 'гэпс':
        client.send_message(message.chat.id, 'Государственная электронная почтовая система')
    elif message.text.lower() == 'ди':
        client.send_message(message.chat.id, 'Должностная инструкция')
    elif message.text.lower() == 'дм':
        client.send_message(message.chat.id, 'Директ-мейл - Реклама товаров и услуг посредством прямой адресной '
                                             'рассылки – отправка по почте рекламных материалов конкретным '
                                             'потенциальным покупателям и заказчикам')
    elif message.text.lower() == 'дпоиут':
        client.send_message(message.chat.id, 'Департамент по подбору, оценке и управлению талантами')
    elif message.text.lower() == 'дсч':
        client.send_message(message.chat.id, 'Датчик случайных чисел')
    elif message.text.lower() == 'ду':
        client.send_message(message.chat.id, 'Доставочный участок - территория, обслуживаемая почтальоном')
    elif message.text.lower() == 'дшк':
        client.send_message(message.chat.id, 'Двумерный штриховой код')
    elif message.text.lower() == 'еас опс':
        client.send_message(message.chat.id, 'Единая автоматизированная система отделений почтовой связи')
    elif message.text.lower() == 'егрп':
        client.send_message(message.chat.id, 'Единый государственный реестр прав на недвижимое имущество и сделок с ним')
    elif message.text.lower() == 'едв':
        client.send_message(message.chat.id, 'Единовременная выплата')
    elif message.text.lower() == 'еис ко':
        client.send_message(message.chat.id, 'Единая информационная системы консолидированной отчетности ('
                                             'Бухгалтерская, Налоговая отчетность, Бюджет, Статистика)')
    elif message.text.lower() == 'еиск':
        client.send_message(message.chat.id, 'Единая информационная система казначейства')
    elif message.text.lower() == 'експд':
        client.send_message(message.chat.id, 'Единая корпоративная сеть передачи данных')
    elif message.text.lower() == 'еку':
        client.send_message(message.chat.id, 'Единый классификатор услуг')
    elif message.text.lower() == 'екц':
        client.send_message(message.chat.id, 'Единый кадровый центр')
    elif message.text.lower() == 'епм':
        client.send_message(message.chat.id, 'Единый план мероприятий')
    elif message.text.lower() == 'есиа':
        client.send_message(message.chat.id, 'Единая система идентификации и аутентификации')
    elif message.text.lower() == 'еспп':
        client.send_message(message.chat.id, 'Единая система почтовых переводов Предприятия')
    elif message.text.lower() == 'есэд':
        client.send_message(message.chat.id, 'Единая система электронного документооборота')
    elif message.text.lower() == 'згд':
        client.send_message(message.chat.id, 'Заместитель генерального директора')
    elif message.text.lower() == 'знз':
        client.send_message(message.chat.id, 'Заявка на закупку')
    elif message.text.lower() == 'зпбт':
        client.send_message(message.chat.id, 'Защищенный пункт бумажных технологий процессинговой системы')
    elif message.text.lower() == 'зпо':
        client.send_message(message.chat.id, 'Заказные Почтовые Отправления')
    elif message.text.lower() == 'зпто':
        client.send_message(message.chat.id, 'Защищенный пункт терминальной обработки')
    elif message.text.lower() == 'зуп':
        client.send_message(message.chat.id, 'Зарплата и управление персоналом')
    elif message.text.lower() == 'ивц':
        client.send_message(message.chat.id, 'Информационно-вычислительный центр')
    elif message.text.lower() == 'инн':
        client.send_message(message.chat.id, 'Идентификационный номер налогоплательщика')
    elif message.text.lower() == 'инцидент':
        client.send_message(message.chat.id, 'Любое событие (ошибка, сбой, зависание и т.д.), не являющееся частью '
                                             'нормальной работы услуги, способное  привести к остановке услуги или '
                                             'снижению уровня ее качества (см. NAUMEN)')
    elif message.text.lower() == 'ип':
        client.send_message(message.chat.id, 'Информпункты')
    elif message.text.lower() == 'ипа':
        client.send_message(message.chat.id, 'Иностранная почтовая администрация')
    elif message.text.lower() == 'ис':
        client.send_message(message.chat.id, 'Информационная система')
    elif message.text.lower() == 'ис эпс':
        client.send_message(message.chat.id, 'Информационная система «Электронная почтовая система»')
    elif message.text.lower() == 'исо':
        client.send_message(message.chat.id, 'Информационная система обращений')
    elif message.text.lower() == 'ит':
        client.send_message(message.chat.id, 'Информационные технологии')
    elif message.text.lower() == 'ка':
        client.send_message(message.chat.id, 'Контрагент - юридическое лицо, получающие денежные средства за '
                                             'оказываемые услуги')
    elif message.text.lower() == 'кбк':
        client.send_message(message.chat.id, 'Код бюджетной классификации')
    elif message.text.lower() == 'квл':
        client.send_message(message.chat.id, 'Коэффициент выхода на линию (почтовая логистика)')
    elif message.text.lower() == 'кгп':
        client.send_message(message.chat.id, 'Контрольно-гербовая печать')
    elif message.text.lower() == 'кд':
        client.send_message(message.chat.id, 'Кадровые данные; Конкурсная документация')
    elif message.text.lower() == 'кип':
        client.send_message(message.chat.id, 'Коэффициент использования парка (почтовая логистика); Корпоративный '
                                             'интранет-портал (my.pochta.ru)')
    elif message.text.lower() == 'ккм':
        client.send_message(message.chat.id, 'Контрольно-кассовая машина (фискальный регистратор)')
    elif message.text.lower() == 'кнр':
        client.send_message(message.chat.id, 'Ключевые навыки руководителя')
    elif message.text.lower() == 'комр':
        client.send_message(message.chat.id, 'Контрактный отдел МР Предприятия')
    elif message.text.lower() == 'кб':
        client.send_message(message.chat.id, 'Коробочный продукт - Страховой продукт партнеров Предприятия - '
                                             'страховых компаний с четко определенным перечнем страховых рисков, '
                                             'страховых сумм и страховых премий')
    elif message.text.lower() == 'кп':
        client.send_message(message.chat.id, 'Ключевой пользователь; Коммерческое предложение')
    elif message.text.lower() == 'кпг':
        client.send_message(message.chat.id, 'Компримированный природный газ')
    elif message.text.lower() == 'кпо':
        client.send_message(message.chat.id, 'Крупногабаритные почтовые отправления')
    elif message.text.lower() == 'кпш':
        client.send_message(message.chat.id, 'Календарный почтовый штемпель')
    elif message.text.lower() == 'кпэ':
        client.send_message(message.chat.id, 'Ключевой показатель эффективности')
    elif message.text.lower() == 'кр':
        client.send_message(message.chat.id, 'Кадровый резерв')
    elif message.text.lower() == 'крс':
        client.send_message(message.chat.id, 'Квитанция разных сборов (пр. при возврате ж/д билета')
    elif message.text.lower() == 'кспд':
        client.send_message(message.chat.id, 'Корпоративная сеть передачи данных')
    elif message.text.lower() == 'ксс':
        client.send_message(message.chat.id, 'Контрольно-справочная служба; Корпоративная социальная сеть')
    elif message.text.lower() == 'ктг':
        client.send_message(message.chat.id, 'Коэффициент технической готовности (почтовая логистика)')
    elif message.text.lower() == 'кш':
        client.send_message(message.chat.id, 'Календарный штемпель')
    elif message.text.lower() == 'кшд':
        client.send_message(message.chat.id, 'Корпоративная шина данных')
    elif message.text.lower() == 'кэп':
        client.send_message(message.chat.id, 'Квалифицированная электронная подпись')
    elif message.text.lower() == 'лна':
        client.send_message(message.chat.id, 'Локальные нормативные акты Предприятия (Регламент, Порядок и т.д.).')
    elif message.text.lower() == 'лнд':
        client.send_message(message.chat.id, 'Локальные нормативные документы')
    elif message.text.lower() == 'лпц':
        client.send_message(message.chat.id, 'Логистический почтовый центр')
    elif message.text.lower() == 'лшк':
        client.send_message(message.chat.id, 'Линейный штрих-код')
    elif message.text.lower() == 'мап':
        client.send_message(message.chat.id, 'Межрегиональное агентство подписки')
    elif message.text.lower() == 'миндсп':
        client.send_message(message.chat.id, 'Минимально допустимый срок подписки')
    elif message.text.lower() == 'ммгн':
        client.send_message(message.chat.id, 'Маломобильные группы населения')
    elif message.text.lower() == 'ммп':
        client.send_message(message.chat.id, 'Московский межрайонный почтамт')
    elif message.text.lower() == 'ммпо':
        client.send_message(message.chat.id, 'Место международного почтового обмена')
    elif message.text.lower() == 'ммсп':
        client.send_message(message.chat.id, 'ММСП московский межрайонный сортировочный почтамт')
    elif message.text.lower() == 'мо':
        client.send_message(message.chat.id, 'Международное отправление')
    elif message.text.lower() == 'мозгр':
        client.send_message(message.chat.id, 'Место обмена за границей - место международного почтового обмена, '
                                             'открытое за пределами страны почтового оператора')
    elif message.text.lower() == 'мок':
        client.send_message(message.chat.id, 'Международный ответный купон')
    elif message.text.lower() == 'мокк':
        client.send_message(message.chat.id, 'Модель обслуживания корпоративных клиентов')
    elif message.text.lower() == 'мопс':
        client.send_message(message.chat.id, 'Мобильное отделение почтовой связи')
    elif message.text.lower() == 'мпз':
        client.send_message(message.chat.id, 'Матрица приоритетных задач')
    elif message.text.lower() == 'мкпо':
        client.send_message(message.chat.id, 'Место прямого контейнерного обмена')
    elif message.text.lower() == 'мпкт':
        client.send_message(message.chat.id, 'Мобильный почтово-кассовый терминал, состоящий из мобильного телефона с '
                                             'программным обеспечением для оформления платежей и передачи их на '
                                             'сервер и контрольно-кассовой машины для печати фискальных чеков')
    elif message.text.lower() == 'мпо':
        client.send_message(message.chat.id, 'Международное почтовое отделение')
    elif message.text.lower() == 'мр асц':
        client.send_message(message.chat.id, 'Московский региональный автоматизированный сортировочный центр')
    elif message.text.lower() == 'мр лц':
        client.send_message(message.chat.id, 'Межрегиональный логистический центр')
    elif message.text.lower() == 'мрп':
        client.send_message(message.chat.id, 'Межрайонный почтамт')
    elif message.text.lower() == 'мрц':
        client.send_message(message.chat.id, 'Макрорегиональный центр')
    elif message.text.lower() == 'мсп':
        client.send_message(message.chat.id, 'Малое и среднее предпринимательство')
    elif message.text.lower() == 'мсц':
        client.send_message(message.chat.id, 'Магистральный сортировочный центр')
    elif message.text.lower() == 'Мультиконверт':
        client.send_message(message.chat.id, 'Простое почтовое отправление с товарным вложением (сувенирная '
                                             'продукция, рекламные образцы продукции, пластиковые карты, '
                                             'CD/DVD диски)')
    elif message.text.lower() == 'мфц':
        client.send_message(message.chat.id, 'Многофункциональный центр')
    elif message.text.lower() == 'мэр':
        client.send_message(message.chat.id, 'Министерство экономического развития Российской Федерации')
    elif message.text.lower() == 'нп':
        client.send_message(message.chat.id, 'Не применимо')
    elif message.text.lower() == 'ндс':
        client.send_message(message.chat.id, 'Налог на добавленную стоимость')
    elif message.text.lower() == 'Немех':
        client.send_message(message.chat.id, 'Немеханизированные отделения почтовой связи')
    elif message.text.lower() == 'нко':
        client.send_message(message.chat.id, 'Некоммерческие организации')
    elif message.text.lower() == 'нмц':
        client.send_message(message.chat.id, 'Начальная максимальная цена')
    elif message.text.lower() == 'ночной оператор':
        client.send_message(message.chat.id, 'Оператор, работающий в ночное время, определенное Трудовым кодексом '
                                             'Российской Федерации')
    elif message.text.lower() == 'нп':
        client.send_message(message.chat.id, 'Наложенный платеж; Национальный проект')
    elif message.text.lower() == 'нпо':
        client.send_message(message.chat.id, 'Негосударственное пенсионное обеспечение')
    elif message.text.lower() == 'нси':
        client.send_message(message.chat.id, 'Нормативно-справочная информация')
    elif message.text.lower() == 'нспу':
        client.send_message(message.chat.id, 'Номерное сигнальное пластиковое устройство')
    elif message.text.lower() == 'нфо':
        client.send_message(message.chat.id, 'Новые форматы обслуживания')
    elif message.text.lower() == 'оасу рпо':
        client.send_message(message.chat.id, 'Общероссийская автоматизированная система учета и контроля за '
                                             'прохождением регистрируемых почтовых отправлений')
    elif message.text.lower() == 'овпо':
        client.send_message(message.chat.id, 'Ответное внутреннее почтовое отправление')
    elif message.text.lower() == 'огв':
        client.send_message(message.chat.id, 'Органы государственной власти')
    elif message.text.lower() == 'огрн':
        client.send_message(message.chat.id, 'Основной государственный регистрационный номер')
    elif message.text.lower() == 'октмо':
        client.send_message(message.chat.id, 'Общероссийский классификатор территорий муниципальных образований')
    elif message.text.lower() == 'он':
        client.send_message(message.chat.id, 'Начальник ОПС')
    elif message.text.lower() == 'онз':
        client.send_message(message.chat.id, 'Заместитель начальника ОПС')
    elif message.text.lower() == 'оп':
        client.send_message(message.chat.id, 'Основной пользователь')
    elif message.text.lower() == 'оператор':
        client.send_message(message.chat.id, 'Оператор связи 1-3 классов')
    elif message.text.lower() == 'опп':
        client.send_message(message.chat.id, 'Отделение почтовых перевозок; Отдел подбора персонала')
    elif message.text.lower() == 'опс':
        client.send_message(message.chat.id, 'Отделение почтовой связи. Обособленное структурное подразделение '
                                             'почтамта, предоставляющее населению, организациям, предприятиям и '
                                             'учреждениям услуги почтовой связи и другие услуги')
    elif message.text.lower() == 'орд':
        client.send_message(message.chat.id, 'Организационно-распорядительные документы: приказы, распоряжения')
    elif message.text.lower() == 'ос':
        client.send_message(message.chat.id, 'Операционная система')
    elif message.text.lower() == 'осп':
        client.send_message(message.chat.id, 'Обособленное структурное подразделение')
    elif message.text.lower() == 'оц':
        client.send_message(message.chat.id, 'Объявленная ценность')
    elif message.text.lower() == 'пао':
        client.send_message(message.chat.id, 'Публичное акционерное общество')
    elif message.text.lower() == 'партионная почта':
        client.send_message(message.chat.id, 'Партионными считаются 5 и более РПО одного отправителя в один или '
                                             'несколько адресов')
    elif message.text.lower() == 'пвз':
        client.send_message(message.chat.id, 'Пункт выдачи заказов')
    elif message.text.lower() == 'перечень':
        client.send_message(message.chat.id, 'Перечень организаций и физических лиц, в отношении которых имеются '
                                             'сведения об их причастности к экстремистской деятельности или '
                                             'терроризму')
    elif message.text.lower() == 'пждп':
        client.send_message(message.chat.id, 'Прижелезнодорожный почтамт')
    elif message.text.lower() == 'пк':
        client.send_message(message.chat.id, 'Письменная корреспонденция - простые и регистрируемые почтовые '
                                             'карточки, письма, бандероли, секограммы и мелкие пакеты; Персональный '
                                             'компьютер')
    elif message.text.lower() == 'пкд':
        client.send_message(message.chat.id, 'Пункт коллективного доступа')
    elif message.text.lower() == 'пко':
        client.send_message(message.chat.id, 'Предварительный квалификационный отбор')
    elif message.text.lower() == 'пкт':
        client.send_message(message.chat.id, 'Почтово-кассовый терминал')
    elif message.text.lower() == 'пмпо':
        client.send_message(message.chat.id, 'Пункт межународного почтового обмена')
    elif message.text.lower() == 'по':
        client.send_message(message.chat.id, 'Почтовое отправление; Программное обеспечение')
    elif message.text.lower() == 'попс':
        client.send_message(message.chat.id, 'Передвижное отделение почтовой связи')
    elif message.text.lower() == 'поупс':
        client.send_message(message.chat.id, 'Правила оказания услуг почтовой связи')
    elif message.text.lower() == 'Почтатех':
        client.send_message(message.chat.id, 'Филиал Почты России – «Почтовые технологии»')
    elif message.text.lower() == 'Почтомат':
        client.send_message(message.chat.id, '«Почтовый автомат» (Постамат) – автоматизированный терминал по выдаче '
                                             'товаров, заказанных в интернет-магазинах и каталогах')
    elif message.text.lower() == 'пп':
        client.send_message(message.chat.id, 'Почтовый перевод; Подбор персонала')
    elif message.text.lower() == 'ппз':
        client.send_message(message.chat.id, 'Позиция плана закупки')
    elif message.text.lower() == 'ппи':
        client.send_message(message.chat.id, 'Периодическое печатное издание – газета, журнал, альманах, бюллетень, '
                                             'иное издание, имеющее постоянное название, текущий номер и выходящее в '
                                             'свет не реже одного раза в год')
    elif message.text.lower() == 'ппо':
        client.send_message(message.chat.id, 'Пломба почтовая одноразовая')
    elif message.text.lower() == 'ппп':
        client.send_message(message.chat.id, 'Пакет прикладных программ')
    elif message.text.lower() == 'ппс':
        client.send_message(message.chat.id, 'Пункт почтовой связи; Почтовая платежная система с программным '
                                             'обеспечением, осуществляющая прием платежей в адрес 3-х лиц в режимах '
                                             'online и offline')
    elif message.text.lower() == 'псот':
        client.send_message(message.chat.id, 'Повременная система оплаты труда')
    elif message.text.lower() == 'пу':
        client.send_message(message.chat.id, 'Прибор учета')
    elif message.text.lower() == 'пфо':
        client.send_message(message.chat.id, 'Планово-финансовая отчетность')
    elif message.text.lower() == 'пэп':
        client.send_message(message.chat.id, 'Простая электронная подпись')
    elif message.text.lower() == 'рапида':
        client.send_message(message.chat.id, 'Сервис отправки банковских переводов через "Почта-Финанс"')
    elif message.text.lower() == 'рим':
        client.send_message(message.chat.id, 'Рекламный и/или информационный материал, содержащий информационное, '
                                             'маркетинговое или публичное сообщение')
    elif message.text.lower() == 'ркп':
        client.send_message(message.chat.id, 'Расчетно-контрольный показатель; Регулируемый коммерческий показатель')
    elif message.text.lower() == 'рмопс':
        client.send_message(message.chat.id, 'Рабочее место оператора почтовой связи')
    elif message.text.lower() == 'ро':
        client.send_message(message.chat.id, 'Разрешающий орган')
    elif message.text.lower() == 'рпв':
        client.send_message(message.chat.id, 'Расчет пенсионных взносов')
    elif message.text.lower() == 'рпдл':
        client.send_message(message.chat.id, 'Российское публичное должностное лицо')
    elif message.text.lower() == 'рпк':
        client.send_message(message.chat.id, 'Регистрируемая письменная корреспонденция')
    elif message.text.lower() == 'рпо':
        client.send_message(message.chat.id, 'Регистрируемое почтовое отправление')
    elif message.text.lower() == 'рфпи':
        client.send_message(message.chat.id, 'Российский Фонд Прямых Инвестиций')
    elif message.text.lower() == 'сах':
        client.send_message(message.chat.id, 'Система адресного хранения')
    elif message.text.lower() == 'сбп':
        client.send_message(message.chat.id, 'Срочные безадресные переводы; Система быстрых платежей')
    elif message.text.lower() == 'сдо':
        client.send_message(message.chat.id, 'Система дистанционного обучения')
    elif message.text.lower() == 'секограмма':
        client.send_message(message.chat.id, 'Секограмма')
    elif message.text.lower() == 'сзд':
        client.send_message(message.chat.id, 'Система защиты доходов')
    elif message.text.lower() == 'со':
        client.send_message(message.chat.id, 'Специализированная организация')
    elif message.text.lower() == 'сопс':
        client.send_message(message.chat.id, 'Сельское отделение почтовой связи')
    elif message.text.lower() == 'соут':
        client.send_message(message.chat.id, 'Специальная оценка условий труда')
    elif message.text.lower() == 'сп':
        client.send_message(message.chat.id, 'Структурное подразделение')
    elif message.text.lower() == 'спз':
        client.send_message(message.chat.id, 'Специальные права заимствования – искусственная денежная единица для '
                                             'межгосударственных и межбанковских (центральные банки) расчётов')
    elif message.text.lower() == 'спп':
        client.send_message(message.chat.id, 'Структурное подразделение предприятия')
    elif message.text.lower() == 'ссот':
        client.send_message(message.chat.id, 'Сдельная система оплаты труда')
    elif message.text.lower() == 'ссч':
        client.send_message(message.chat.id, 'Среднесписочная численность')
    elif message.text.lower() == 'стм':
        client.send_message(message.chat.id, 'Собственная торговая марка')
    elif message.text.lower() == 'субд':
        client.send_message(message.chat.id, 'Система управления базой данных')
    elif message.text.lower() == 'суо':
        client.send_message(message.chat.id, 'Система управления очередью')
    elif message.text.lower() == 'сц':
        client.send_message(message.chat.id, 'Сортировочный центр')
    elif message.text.lower() == 'сэд':
        client.send_message(message.chat.id, 'Система электронного документооборота')
    elif message.text.lower() == 'тмц':
        client.send_message(message.chat.id, 'Товарно-материальные ценности')
    elif message.text.lower() == 'тнвэд':
        client.send_message(message.chat.id, 'Товарная номенклатура внешнеэкономической деятельности (таможенный код)')
    elif message.text.lower() == 'тнп':
        client.send_message(message.chat.id, 'Товары народного потребления')
    elif message.text.lower() == 'точ':
        client.send_message(message.chat.id, 'Тарифно-окладная часть')
    elif message.text.lower() == 'тп':
        client.send_message(message.chat.id, 'Технический перерыв – время отдыха сотрудника в соответствии с ТК РФ')
    elif message.text.lower() == 'тру':
        client.send_message(message.chat.id, 'Товары, работы, услуги')
    elif message.text.lower() == 'тс':
        client.send_message(message.chat.id, 'Транспортное средство')
    elif message.text.lower() == 'ттс':
        client.send_message(message.chat.id, 'Транзакционный Терминал Самообслуживания (предназначен для оформления '
                                             'проездных документов на бланках строгой отчетности ОАО «РЖД»)')
    elif message.text.lower() == 'тэд':
        client.send_message(message.chat.id, 'Технология электронного документооборота')
    elif message.text.lower() == 'удз':
        client.send_message(message.chat.id, 'Уполномоченный директором заместитель')
    elif message.text.lower() == 'укд':
        client.send_message(message.chat.id, 'Участок курьерской доставки')
    elif message.text.lower() == 'уо и опо':
        client.send_message(message.chat.id, 'Участок обработки и обмена почтовыми отправлениями')
    elif message.text.lower() == 'уои':
        client.send_message(message.chat.id, 'Участок обработки информации ("Инфопункт")')
    elif message.text.lower() == 'уоопо':
        client.send_message(message.chat.id, 'Участок обработки и обмена почтовыми отправлениями')
    elif message.text.lower() == 'уоп':
        client.send_message(message.chat.id, 'Участки обработки почты')
    elif message.text.lower() == 'уопп':
        client.send_message(message.chat.id, 'Выбрать или отменить выбор элемента')
    elif message.text.lower() == 'уопп гсп':
        client.send_message(message.chat.id, 'Участок обслуживания партионной почты -  городская служебная почта')
    elif message.text.lower() == 'уосп':
        client.send_message(message.chat.id, 'Участок обработки страховой почты')
    elif message.text.lower() == 'уп':
        client.send_message(message.chat.id, 'Управление персоналом')
    elif message.text.lower() == 'упс':
        client.send_message(message.chat.id, 'Услуга почтовой связи')
    elif message.text.lower() == 'урм':
        client.send_message(message.chat.id, 'Удаленное рабочее место')
    elif message.text.lower() == 'урпп':
        client.send_message(message.chat.id, 'Участок розничных продаж периодики')
    elif message.text.lower() == 'усои':
        client.send_message(message.chat.id, 'Участок сбора и обработки информации')
    elif message.text.lower() == 'уус':
        client.send_message(message.chat.id, 'Универсальная услуга связи')
    elif message.text.lower() == 'ууц':
        client.send_message(message.chat.id, 'Участок условных ценностей')
    elif message.text.lower() == 'уфпс':
        client.send_message(message.chat.id, 'Управление федеральной почтовой связи, филиал АО «Почта России». '
                                             'Основной задачей УФПС является управление деятельностью организаций '
                                             'федеральной почтовой службы в регионе')
    elif message.text.lower() == 'уфс':
        client.send_message(message.chat.id, 'Универсальная финансовая система')
    elif message.text.lower() == 'фгуп':
        client.send_message(message.chat.id, 'Федеральное государственное унитарное предприятие')
    elif message.text.lower() == 'фм':
        client.send_message(message.chat.id, 'Франкировальная машина')
    elif message.text.lower() == 'фн':
        client.send_message(message.chat.id, 'Фискальный накопитель')
    elif message.text.lower() == 'фоив':
        client.send_message(message.chat.id, 'Федеральный орган исполнительной власти')
    elif message.text.lower() == 'фсг':
        client.send_message(message.chat.id, 'Федеральная система «Город»')
    elif message.text.lower() == 'фулфилмент':
        client.send_message(message.chat.id, 'Комплекс услуг по логистической обработке заказа (хранение, прием и '
                                             'обработка заказа, комплектация и упаковка товара, организация доставки, '
                                             'получения денежных средств от покупателей, обработка возвратов)')
    elif message.text.lower() == 'ходовик':
        client.send_message(message.chat.id, 'Список подписчиков с указанием адресов и наименований периодических '
                                             'печатных изданий на одном доставочном участке')
    elif message.text.lower() == 'цаитс':
        client.send_message(message.chat.id, 'Центр автоматизированных информационно-технологических систем')
    elif message.text.lower() == 'цвпп':
        client.send_message(message.chat.id, 'Центр выдачи и приёма посылок, структурное подразделение ОПС, которое '
                                             'обслуживает как физических, так и юридических лиц')
    elif message.text.lower() == 'цгп':
        client.send_message(message.chat.id, 'Центры гибридной почты')
    elif message.text.lower() == 'цод':
        client.send_message(message.chat.id, 'Центр обработки данных')
    elif message.text.lower() == 'цоюл':
        client.send_message(message.chat.id, 'Центр обслуживания юридических лиц')
    elif message.text.lower() == 'цпк':
        client.send_message(message.chat.id, 'Целевой показатель качества')
    elif message.text.lower() == 'црт сервис':
        client.send_message(message.chat.id, 'Централизованный региональный технический сервис')
    elif message.text.lower() == 'цфо':
        client.send_message(message.chat.id, 'Центр финансового обслуживания; Центр финансовой ответственности')
    elif message.text.lower() == 'цхдпа':
        client.send_message(message.chat.id, 'Центральное хранилище данных о почтовых адресах')
    elif message.text.lower() == 'цхэд':
        client.send_message(message.chat.id, 'Цифровое хранилище электронных документов (цифровой архив)')
    elif message.text.lower() == 'чнн':
        client.send_message(message.chat.id, 'Час наибольшей нагрузки')
    elif message.text.lower() == 'шбз':
        client.send_message(message.chat.id, 'Школа базовых знаний')
    elif message.text.lower() == 'ши':
        client.send_message(message.chat.id, 'Штриховой идентификатор отправления – штриховой код, соответствующий '
                                             'техническому стандарту Всемирного почтового союза')
    elif message.text.lower() == 'шк':
        client.send_message(message.chat.id, 'Штрих-код')
    elif message.text.lower() == 'шпи':
        client.send_message(message.chat.id, 'Штриховой почтовый идентификатор')
    elif message.text.lower() == 'эдо':
        client.send_message(message.chat.id, 'Электронный документооборот')
    elif message.text.lower() == 'эзп':
        client.send_message(message.chat.id, 'Электронные заказные письма')
    elif message.text.lower() == 'эп':
        client.send_message(message.chat.id, 'Электронная площадка')
    elif message.text.lower() == 'эцп':
        client.send_message(message.chat.id, 'Электронная цифровая подпись')
    elif message.text.lower() == 'юзэдо':
        client.send_message(message.chat.id, 'Юридически значимый электронный документооборот')
    elif message.text.lower() == 'япм':
        client.send_message(message.chat.id, 'Ящики полимерные многоразовые')
    elif message.text.lower() == 'дв':
        client.send_message(message.chat.id, 'До востребования')
    elif message.text.lower() == 'b2b':
        client.send_message(message.chat.id, 'Услуги и товары «бизнес к бизнесу» (Business to Business)')
    elif message.text.lower() == 'b2c':
        client.send_message(message.chat.id, 'Услуги и товары «бизнес к потребителю» (Business to Customer)')
    elif message.text.lower() == 'большие данные':
        client.send_message(message.chat.id, 'Обозначение структурированных и неструктурированных данных огромных '
                                             'объемов и значительного многообразия')
    elif message.text.lower() == 'с2с':
        client.send_message(message.chat.id, 'Услуги «потребитель к потребителю» (Customer to Customer)')
    elif message.text.lower() == 'capex':
        client.send_message(message.chat.id, 'Капитальные затраты (Capital Expenditures)')
    elif message.text.lower() == 'капекс':
        client.send_message(message.chat.id, 'Капитальные затраты (Capital Expenditures)')
    elif message.text.lower() == 'cep':
        client.send_message(message.chat.id, 'Курьерский, экспресс и посылочный сегмент (Courier, Express, Parcels)')
    elif message.text.lower() == 'cms':
        client.send_message(message.chat.id, 'Система управления контентом (Content Management System)')
    elif message.text.lower() == 'crm':
        client.send_message(message.chat.id, 'Customer Relationship Management - cистема управления взаимоотношениями '
                                             'с клиентами, прикладное программное обеспечение')
    elif message.text.lower() == 'cvp':
        client.send_message(message.chat.id, 'Ценностное предложение для клиента( Customer Value Prpposition)')
    elif message.text.lower() == 'data science':
        client.send_message(message.chat.id, '«Наука о данных» - обозначение различных методов по обработке данных в '
                                             'условиях больших объемов')
    elif message.text.lower() == 'ebitda':
        client.send_message(message.chat.id, 'Прибыль до вычета расходов по выплате процентов, налогов, износа и начисленной амортизации')
    elif message.text.lower() == 'ems':
        client.send_message(message.chat.id, 'Express Mail Service - всемирная сеть почтовой связи')
    elif message.text.lower() == 'e2e':
        client.send_message(message.chat.id, 'End-to-end - Модель доставки отправлений «из рук в руки»')
    elif message.text.lower() == 'naumen':
        client.send_message(message.chat.id, 'Программный продукт для автоматизации управления ИТ и бизнес услугами; '
                                             'система обработки претензий')
    elif message.text.lower() == 'pos':
        client.send_message(message.chat.id, 'Аппаратно-программный комплекс, позволяющий осуществлять торговые '
                                             'операции')
    elif message.text.lower() == 'sbms':
        client.send_message(message.chat.id, 'Система управления абонентской базой')
    elif message.text.lower() == 'srm':
        client.send_message(message.chat.id, 'Simplified Registered Mail - международные почтовые отправления')
    elif message.text.lower() == 'swift':
        client.send_message(message.chat.id, 'Часть международной банковской системы платежей')
    elif message.text.lower() == 'winpost':
        client.send_message(message.chat.id, 'Автоматизированная система ОПС')
    elif message.text.lower() == '/start':
        client.send_message(message.chat.id, 'Напиши аббревиатуру или термин, который хочешь расшифровать. Можно '
                                             'маленькими буквами.')

    else: client.send_message(message.chat.id, 'я вас не понимаю')

client.polling(none_stop = True, interval = 0)