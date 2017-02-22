#coding: utf8

QUESTIONS = [
    [u'Владелец', u'vladelec',[
        [u'Физическое лицо', u'1'],
        [u'Юридическое лицо', u'2']
    ]],
    [u'Условия', u'usloviya',[
        [u'Стандартные', u'0'],
        [u'Транзит', u'1'],
        [u'Иностранец', u'2'],
        [u'Спецтехника', u'3']
    ]],
    [u'Тип ТС', u'tip_ts',[
        [u'Мотоциклы, мопеды, квадроциклы', u'a'],
        [u'Легковой автомобиль', u'b'],
        [u'Легковое такси', u'b-t'],
        [u'Грузовой автомобиль, max 16 тонн и менее', u'c'],
        [u'Грузовой автомобиль, max 16 тонн и более', u'c-m'],
        [u'Автобусы до 16 пассажиров включительно', u'd'],
        [u'Автобусы более 16 пассажиров', u'd-m'],
        [u'Маршрутные автобусы', u'd-t'],
        [u'Троллейбусы', u'tb'],
        [u'Трамваи', u'tm'],
        [u'Трактора', u'tr'],
    ]],
    [u'Мощность', u'moshnost',[
        [u'до 50 л.с. включительно', u'0'],
        [u'свыше 50 до 70 л.с.', u'1'],
        [u'свыше 70 до 100 л.с.', u'2'],
        [u'свыше 100 до 120 л.с.', u'3'],
        [u'свыше 120 до 150 л.с.', u'4'],
        [u'свыше 150 л.с.', u'5'],
    ]],
    [u'Будет использоваться с прицепом', u'pricep',[
        [u'Нет', u'1'],
        [u'Да', u'2'],
    ]],
    [u'Место регистрации собственника', u'region',[
        [u'Москва', u'78'],
        [u'Московская область', u'53'],
        [u'Санкт-Петербург', u'79'],
        [u'Ленинградская область', u'50'],
        [u'Адыгея', u'1'],
        [u'Алтай (республика)', u'2',
            [u'Уточните город', u'city',[
                [u'Горно-Алтайск', u'2_1'],
                [u'прочие города и населенные пункты', u'2_2'],
            ]],
        ],
        [u'Алтайский край', u'23',
             [u'Уточните город', u'city',[
                [u'Барнаул', u'23_1'],
                [u'Бийск', u'23_2'],
                [u'Заринск, Новоалтайск, Рубцовск', u'23_3'],
                [u'прочие города и населенные пункты', u'23_4'],
            ]],
        ],
        [u'Амурская область', u'32',
            [u'Уточните город', u'city',[
                [u'Белогорск, Свободный', u'32_1'],
                [u'Благовещенск', u'32_2'],
                [u'прочие города и населенные пункты', u'32_3'],
            ]],
        ],
        [u'Архангельская область', u'33',
            [u'Уточните город', u'city',[
                [u'Архангельск', u'33_1'],
                [u'Котлас', u'33_2'],
                [u'Северодвинск', u'33_3'],
                [u'прочие города и населенные пункты', u'33_4'],
            ]],
        ],
        [u'Астраханская область', u'34',
            [u'Уточните город', u'city',[
                [u'Астрахань', u'34_1'],
                [u'прочие города и населенные пункты', u'34_2'],
            ]],
        ],
        [u'Башкортостан', u'3',
            [u'Уточните город', u'city',[
                [u'Благовещенск, Октябрьский', u'3_1'],
                [u'Ишимбай, Кумертау, Салават', u'3_2'],
                [u'Стерлитамак, Туймазы', u'3_3'],
                [u'Уфа', u'3_4'],
                [u'прочие города и населенные пункты', u'3_5'],
            ]],
        ],
        [u'Байконур', u'86' ],
        [u'Белгородская область', u'35',
            [u'Уточните город', u'city',[
                [u'Белгород', u'35_1'],
                [u'Губкин, Старый Оскол', u'35_2'],
                [u'прочие города и населенные пункты', u'35_3'],
            ]],
        ],
        [u'Брянская область', u'36',
            [u'Уточните город', u'city',[
                [u'Брянск', u'36_1'],
                [u'Клинцы', u'36_2'],
                [u'прочие города и населенные пункты', u'36_3'],
            ]],
        ],
        [u'Бурятия', u'4',
            [u'Уточните город', u'city',[
                [u'Улан-Удэ', u'4_1'],
                [u'прочие города и населенные пункты', u'4_2'],
            ]],
        ],
        [u'Владимирская область', u'37',
            [u'Уточните город', u'city',[
                [u'Владимир', u'37_1'],
                [u'Гусь-Хрустальный', u'37_2'],
                [u'Муром', u'37_3'],
                [u'прочие города и населенные пункты', u'37_4'],
            ]],
        ],
        [u'Волгоградская область', u'38',
            [u'Уточните город', u'city',[
                [u'Волгоград', u'38_1'],
                [u'Волжский', u'38_2'],
                [u'Камышин, Михайловка', u'38_3'],
                [u'прочие города и населенные пункты', u'38_4'],
            ]],
        ],
        [u'Вологодская область', u'39',
            [u'Уточните город', u'city',[
                [u'Вологда', u'39_1'],
                [u'Череповец', u'39_2'],
                [u'прочие города и населенные пункты', u'39_3'],
            ]],
        ],
        [u'Воронежская область', u'40',
            [u'Уточните город', u'city',[
                [u'Борисоглебск, Лиски, Россошь', u'40_1'],
                [u'Воронеж', u'40_2'],
                [u'прочие города и населенные пункты', u'40_3'],
            ]],
        ],
        [u'Дагестан', u'5',
            [u'Уточните город', u'city',[
                [u'Буйнакск, Дербент, Каспийск, Махачкала, Хасавюрт', u'5_1'],
                [u'прочие города и населенные пункты', u'5_2'],
            ]],
        ],
        [u'Еврейская автономная область', u'81',
            [u'Уточните город', u'city',[
                [u'Биробиджан', u'81_1'],
                [u'прочие города и населенные пункты', u'81_2'],
            ]],
        ],
        [u'Ивановская область', u'41',
            [u'Уточните город', u'city',[
                [u'Иваново', u'41_1'],
                [u'Кинешма', u'41_2'],
                [u'Шуя', u'41_3'],
                [u'прочие города и населенные пункты', u'41_4'],
            ]],
        ],
        [u'Иркутская область', u'42',
            [u'Уточните город', u'city',[
                [u'Ангарск', u'42_1'],
                [u'Братск, Тулун, Усть-Илимск, Усть-Кут, Черемхово', u'42_2'],
                [u'Иркутск', u'42_3'],
                [u'Усолье-Сибирское', u'42_4'],
                [u'Шелехов', u'42_5'],
                [u'прочие города и населенные пункты', u'42_6'],
            ]],
        ],
        [u'Забайкальский край', u'24',
            [u'Уточните город', u'city',[
                [u'Краснокаменск', u'24_1'],
                [u'Чита', u'24_2'],
                [u'прочие города и населенные пункты', u'24_3'],
            ]],
        ],
        [u'Ингушетия', u'6',
            [u'Уточните город', u'city',[
                [u'Малгобек', u'6_1'],
                [u'Назрань', u'6_2'],
                [u'прочие города и населенные пункты', u'6_3'],
            ]],
        ],
        [u'Кабардино-Балкария', u'7',
            [u'Уточните город', u'city',[
                [u'Нальчик, Прохладный', u'7_1'],
                [u'прочие города и населенные пункты', u'7_2'],
            ]],
        ],
        [u'Калининградская область', u'43',
            [u'Уточните город', u'city',[
                [u'Калининград', u'43_1'],
                [u'прочие города и населенные пункты', u'43_2'],
            ]],
        ],
        [u'Калмыкия', u'8',
            [u'Уточните город', u'city',[
                [u'Элиста', u'8_1'],
                [u'прочие города и населенные пункты', u'8_2'],
            ]],
        ],
        [u'Калужская область', u'44',
            [u'Уточните город', u'city',[
                [u'Калуга', u'44_1'],
                [u'Обнинск', u'44_2'],
                [u'прочие города и населенные пункты', u'44_3'],
            ]],
        ],
        [u'Камчатский край', u'25',
            [u'Уточните город', u'city',[
                [u'Петропавловск-Камчатский', u'25_1'],
                [u'прочие города и населенные пункты', u'25_2'],
            ]],
        ],
        [u'Кемеровская область', u'45',
            [u'Уточните город', u'city',[
                [u'Анжеро-Судженск, Киселевск, Юрга', u'45_1'],
                [u'Белово, Березовский, Междуреченск, Осинники, Прокопьевск', u'45_2'],
                [u'Кемерово', u'45_3'],
                [u'Новокузнецк', u'45_4'],
                [u'прочие города и населенные пункты', u'45_5'],
            ]],
        ],
        [u'Кировская область', u'46',
            [u'Уточните город', u'city',[
                [u'Киров', u'46_1'],
                [u'Кирово-Чепецк', u'46_2'],
                [u'прочие города и населенные пункты', u'46_3'],
            ]],
        ],
        [u'Костромская область', u'47',
            [u'Уточните город', u'city',[
                [u'Кострома', u'47_1'],
                [u'прочие города и населенные пункты', u'47_2'],
            ]],
        ],
        [u'Краснодарский край', u'26',
            [u'Уточните город', u'city',[
                [u'Анапа, Геленджик', u'26_1'],
                [u'Армавир, Сочи, Туапсе', u'26_2'],
                [u'Белореченск, Ейск, Кропоткин, Крымск, Курганинск, Лабинск, Славянск-на-Кубани, Тимашевск, Тихорецк', u'26_3'],
                [u'Краснодар, Новороссийск', u'26_4'],
                [u'прочие города и населенные пункты', u'26_5'],
            ]],
        ],
        [u'Красноярский край', u'27',
            [u'Уточните город', u'city',[
                [u'Ачинск, Зеленогорск', u'27_1'],
                [u'Железногорск, Норильск', u'27_2'],
                [u'Канск, Лесосибирск, Минусинск, Назарово', u'27_3'],
                [u'Красноярск', u'27_4'],
                [u'прочие города и населенные пункты', u'27_5'],
            ]],
        ],
        [u'Карачаево-Черкесия', u'9' ],
        [u'Карелия', u'10',
            [u'Уточните город', u'city',[
                [u'Петрозаводск', u'10_1'],
                [u'прочие города и населенные пункты', u'10_2'],
            ]],
        ],
        [u'Коми', u'11',
            [u'Уточните город', u'city',[
                [u'Сыктывкар', u'11_1'],
                [u'Ухта', u'11_2'],
                [u'прочие города и населенные пункты', u'11_3'],
            ]],
        ],
        [u'Крым', u'12',
            [u'Уточните город', u'city',[
                [u'Симферополь', u'12_1'],
                [u'прочие города и населенные пункты', u'12_2'],
            ]],
        ],
        [u'Курганская область', u'48',
            [u'Уточните город', u'city',[
                [u'Курган', u'48_1'],
                [u'Шадринск', u'48_2'],
                [u'прочие города и населенные пункты', u'48_3'],
            ]],
        ],
        [u'Курская область', u'49',
            [u'Уточните город', u'city',[
                [u'Железногорск', u'49_1'],
                [u'Курск', u'49_2'],
                [u'прочие города и населенные пункты', u'49_3'],
            ]],
        ],
        [u'Липецкая область', u'51',
            [u'Уточните город', u'city',[
                [u'Елец', u'51_1'],
                [u'Липецк', u'51_2'],
                [u'прочие города и населенные пункты', u'51_3'],
            ]],
        ],
        [u'Магаданская область', u'52',
            [u'Уточните город', u'city',[
                [u'Магадан', u'52_1'],
                [u'прочие города и населенные пункты', u'52_2'],
            ]],
        ],
        [u'Марий Эл', u'13',
            [u'Уточните город', u'city',[
                [u'Волжск', u'13_1'],
                [u'Йошкар-Ола', u'13_2'],
                [u'прочие города и населенные пункты', u'13_3'],
            ]],
        ],
        [u'Мордовия', u'14',
            [u'Уточните город', u'city',[
                [u'Рузаевка', u'14_1'],
                [u'Саранск', u'14_2'],
                [u'прочие города и населенные пункты', u'14_3'],
            ]],
        ],
        [u'Мурманская область', u'54',
            [u'Уточните город', u'city',[
                [u'Апатиты, Мончегорск', u'54_1'],
                [u'Мурманск', u'54_2'],
                [u'Североморск', u'54_3'],
                [u'прочие города и населенные пункты', u'54_4'],
            ]],
        ],
        [u'Нижегородская область', u'55',
            [u'Уточните город', u'city',[
                [u'Арзамас, Выкса, Саров', u'55_1'],
                [u'Балахна, Бор, Дзержинск', u'55_2'],
                [u'Кстово', u'55_3'],
                [u'Нижний Новгород', u'55_4'],
                [u'прочие города и населенные пункты', u'55_5'],
            ]],
        ],
        [u'Ненецкий автономный округ', u'82' ],
        [u'Новгородская область', u'56',
            [u'Уточните город', u'city',[
                [u'Боровичи', u'56_1'],
                [u'Великий Новгород', u'56_2'],
                [u'прочие города и населенные пункты', u'56_3'],
            ]],
        ],
        [u'Новосибирская область', u'57',
            [u'Уточните город', u'city',[
                [u'Бердск', u'57_1'],
                [u'Искитим', u'57_2'],
                [u'Куйбышев', u'57_3'],
                [u'Новосибирск', u'57_4'],
                [u'прочие города и населенные пункты', u'57_5'],
            ]],
        ],
        [u'Омская область', u'58',
            [u'Уточните город', u'city',[
                [u'Омск', u'58_1'],
                [u'прочие города и населенные пункты', u'58_2'],
            ]],
        ],
        [u'Оренбургская область', u'59',
            [u'Уточните город', u'city',[
                [u'Бугуруслан, Бузулук, Новотроицк', u'59_1'],
                [u'Оренбург', u'59_2'],
                [u'Орск', u'59_3'],
                [u'прочие города и населенные пункты', u'59_4'],
            ]],
        ],
        [u'Орловская область', u'60',
            [u'Уточните город', u'city',[
                [u'Ливны, Мценск', u'60_1'],
                [u'Орел', u'60_2'],
                [u'прочие города и населенные пункты', u'60_3'],
            ]],
        ],
        [u'Пензенская область', u'61',
            [u'Уточните город', u'city',[
                [u'Заречный', u'61_1'],
                [u'Кузнецк', u'61_2'],
                [u'Пенза', u'61_3'],
                [u'прочие города и населенные пункты', u'61_4'],
            ]],
        ],
        [u'Пермский край', u'28',
            [u'Уточните город', u'city',[
                [u'Березники, Краснокамск', u'28_1'],
                [u'Лысьва, Чайковский', u'28_2'],
                [u'Пермь', u'28_3'],
                [u'Соликамск', u'28_4'],
                [u'прочие города и населенные пункты', u'28_5'],
            ]],
        ],
        [u'Приморский край', u'29',
            [u'Уточните город', u'city',[
                [u'Владивосток', u'29_1'],
                [u'прочие города и населенные пункты', u'29_2'],
            ]],
        ],
        [u'Псковская область', u'62',
            [u'Уточните город', u'city',[
                [u'Великие Луки', u'62_1'],
                [u'Псков', u'62_2'],
                [u'прочие города и населенные пункты', u'62_3'],
            ]],
        ],
        [u'Ростовская область', u'63',
            [u'Уточните город', u'city',[
                [u'Азов', u'63_1'],
                [u'Батайск', u'63_2'],
                [u'Волгодонск, Гуково, Каменск-Шахтинский, Новочеркасск, Новошахтинск, Сальск, Таганрог', u'63_3'],
                [u'Ростов-на-Дону', u'63_4'],
                [u'Шахты', u'63_5'],
                [u'прочие города и населенные пункты', u'63_6'],
            ]],
        ],
        [u'Рязанская область', u'64',
            [u'Уточните город', u'city',[
                [u'Рязань', u'64_1'],
                [u'прочие города и населенные пункты', u'64_2'],
            ]],
        ],
        [u'Самарская область', u'65',
            [u'Уточните город', u'city',[
                [u'Новокуйбышевск, Сызрань', u'65_1'],
                [u'Самара', u'65_2'],
                [u'Тольятти', u'65_3'],
                [u'Чапаевск', u'65_4'],
                [u'прочие города и населенные пункты', u'65_5'],
            ]],
        ],
        [u'Саратовская область', u'66',
            [u'Уточните город', u'city',[
                [u'Балаково, Балашов, Вольск', u'66_1'],
                [u'Саратов', u'66_2'],
                [u'Энгельс', u'66_3'],
                [u'прочие города и населенные пункты', u'66_4'],
            ]],
        ],
        [u'Саха (Якутия)', u'15',
            [u'Уточните город', u'city',[
                [u'Нерюнгри', u'15_1'],
                [u'Якутск', u'15_2'],
                [u'прочие города и населенные пункты', u'15_3'],
            ]],
        ],
        [u'Сахалинская область', u'67',
            [u'Уточните город', u'city',[
                [u'Южно-Сахалинск', u'67_1'],
                [u'прочие города и населенные пункты', u'67_2'],
            ]],
        ],
        [u'Свердловская область', u'68',
            [u'Уточните город', u'city',[
                [u'Асбест, Ревда', u'68_1'],
                [u'Березовский, Верхняя Пышма, Новоуральск, Первоуральск', u'68_2'],
                [u'Верхняя Салда, Полевской', u'68_3'],
                [u'Екатеринбург', u'68_4'],
                [u'прочие города и населенные пункты', u'68_5'],
            ]],
        ],
        [u'Северная Осетия–Алания', u'16',
            [u'Уточните город', u'city',[
                [u'Владикавказ', u'16_1'],
                [u'прочие города и населенные пункты', u'16_2'],
            ]],
        ],
        [u'Севастополь', u'80' ],
        [u'Смоленская область', u'69',
            [u'Уточните город', u'city',[
                [u'Вязьма, Рославль, Сафоново, Ярцево', u'69_1'],
                [u'Смоленск', u'69_2'],
                [u'прочие города и населенные пункты', u'69_3'],
            ]],
        ],
        [u'Ставропольский край', u'30',
            [u'Уточните город', u'city',[
                [u'Буденновск, Георгиевск, Ессентуки, Минеральные воды, Невинномысск, Пятигорск', u'30_1'],
                [u'Кисловодск, Михайловск, Ставрополь', u'30_2'],
                [u'прочие города и населенные пункты', u'30_3'],
            ]],
        ],
        [u'Тамбовская область', u'70',
            [u'Уточните город', u'city',[
                [u'Мичуринск', u'70_1'],
                [u'Тамбов', u'70_2'],
                [u'прочие города и населенные пункты', u'70_3'],
            ]],
        ],
        [u'Татарстан', u'17',
            [u'Уточните город', u'city',[
                [u'Альметьевск, Зеленодольск, Нижнекамск', u'17_1'],
                [u'Бугульма, Лениногорск, Чистополь', u'17_2'],
                [u'Елабуга', u'17_3'],
                [u'Казань', u'17_4'],
                [u'Набережные Челны', u'17_5'],
                [u'прочие города и населенные пункты', u'17_6'],
            ]],
        ],
        [u'Тверская область', u'71',
             [u'Уточните город', u'city',[
                [u'Вышний Волочек, Кимры, Ржев', u'71_1'],
                [u'Тверь', u'71_2'],
                [u'прочие города и населенные пункты', u'71_3'],
             ]],
        ],
        [u'Томская область', u'72',
            [u'Уточните город', u'city',[
                [u'Северск', u'72_1'],
                [u'Томск', u'72_2'],
                [u'прочие города и населенные пункты', u'72_3'],
            ]],
        ],
        [u'Тульская область', u'73',
            [u'Уточните город', u'city',[
                [u'Алексин, Ефремов, Новомосковск', u'73_1'],
                [u'Тула', u'73_2'],
                [u'Узловая, Щекино', u'73_3'],
                [u'прочие города и населенные пункты', u'73_4'],
            ]],
        ],
        [u'Тюменская область', u'74',
            [u'Уточните город', u'city',[
                [u'Тобольск', u'74_1'],
                [u'Тюмень', u'74_2'],
                [u'прочие города и населенные пункты', u'74_3'],
            ]],
        ],
        [u'Тыва', u'18',
            [u'Уточните город', u'city',[
                [u'Кызыл', u'18_1'],
                [u'прочие города и населенные пункты', u'18_2'],
            ]],
        ],
        [u'Удмуртия', u'19',
            [u'Уточните город', u'city',[
                [u'Воткинск', u'19_1'],
                [u'Глазов, Сарапул', u'19_2'],
                [u'Ижевск', u'19_3'],
                [u'прочие города и населенные пункты', u'19_4'],
            ]],
        ],
        [u'Ульяновская область', u'75',
            [u'Уточните город', u'city',[
                [u'Димитровград', u'75_1'],
                [u'Ульяновск', u'75_2'],
                [u'прочие города и населенные пункты', u'75_3'],
            ]],
        ],
        [u'Хабаровский край', u'31',
            [u'Уточните город', u'city',[
                [u'Амурск', u'31_1'],
                [u'Комсомольск-на-Амуре', u'31_2'],
                [u'Хабаровск', u'31_3'],
                [u'прочие города и населенные пункты', u'31_4'],
            ]],
        ],
        [u'Хакасия', u'20',
            [u'Уточните город', u'city',[
                [u'Абакан, Саяногорск, Черногорск', u'20_1'],
                [u'прочие города и населенные пункты', u'20_2'],
            ]],
        ],
        [u'Ханты-Мансийск – Югра', u'83',
            [u'Уточните город', u'city',[
                [u'Когалым', u'83_1'],
                [u'Нефтеюганск, Нягань', u'83_2'],
                [u'Сургут', u'83_3'],
                [u'Нижневартовск', u'83_4'],
                [u'Ханты-Мансийск', u'83_5'],
                [u'прочие города и населенные пункты', u'83_6'],
            ]],
        ],
        [u'Челябинская область', u'76',
            [u'Уточните город', u'city',[
                [u'Златоуст, Миасс', u'76_1'],
                [u'Копейск', u'76_2'],
                [u'Магнитогорск', u'76_3'],
                [u'Сатка, Чебаркуль', u'76_4'],
                [u'Челябинск', u'76_5'],
                [u'прочие города и населенные пункты', u'76_6'],
            ]],
        ],
        [u'Чечня', u'21' ],
        [u'Чувашия', u'22',
            [u'Уточните город', u'city',[
                [u'Канаш', u'22_1'],
                [u'Новочебоксарск', u'22_2'],
                [u'Чебоксары', u'22_3'],
                [u'прочие города и населенные пункты', u'22_4'],
            ]],
        ],
        [u'Чукотский автономный округ', u'84' ],
        [u'Ямало-Ненецкий автономный округ', u'85',
            [u'Уточните город', u'city',[
                [u'Новый Уренгой', u'85_1'],
                [u'Ноябрьск', u'85_2'],
                [u'прочие города и населенные пункты', u'85_3'],
            ]],
        ],
        [u'Ярославская область', u'77',
            [u'Уточните город', u'city',[
                [u'Ярославль', u'77_1'],
                [u'прочие города и населенные пункты', u'77_2'],
            ]],
         ],
    ]],
    [u'Период использования', u'period_fl',[
        [u'1 год', u'10'],
        [u'9 месяцев', u'9'],
        [u'8 месяцев', u'8'],
        [u'7 месяцев', u'7'],
        [u'6 месяцев', u'6'],
        [u'5 месяцев', u'5'],
        [u'4 месяца', u'4'],
        [u'3 месяца', u'3'],
    ]],
    [u'Период использования', u'period_ul',[
        [u'1 год', u'10'],
        [u'9 месяцев', u'9'],
        [u'8 месяцев', u'8'],
        [u'7 месяцев', u'7'],
        [u'6 месяцев', u'6'],
    ]],
    [u'Срок страхования', u'period_in',[
        [u'1 год', u'10'],
        [u'9 месяцев', u'9'],
        [u'8 месяцев', u'8'],
        [u'7 месяцев', u'7'],
        [u'6 месяцев', u'6'],
        [u'5 месяцев', u'5'],
        [u'4 месяца', u'4'],
        [u'3 месяца', u'3'],
        [u'2 месяца', u'2'],
        [u'от 16 дней до 1 месяца', u'1'],
        [u'от 5 до 15 дней', u'0'],
    ]],
    [u'Допущены к управлению', u'spisok',[
        [u'ограниченный список водителей', u'1',],
        [u'без ограничения', u'2'],
    ]],
    [u'Минимальный возраст и стаж', u'voditeli',[
        [u'возраст больше 22 лет, стаж свыше 3 лет', u'0'],
        [u'возраст больше 22 лет, стаж до 3 лет', u'1'],
        [u'возраст до 22 лет, стаж свыше 3 лет', u'2'],
        [u'возраст до 22 лет, стаж до 3 лет', u'3'],
    ]],
    [u'Класс', u'kbm',[
        [u'не страховался ранее', u'def'],
        [u'М', u'm'],
        [u'0', u'0'],
        [u'1', u'1'],
        [u'2', u'2'],
        [u'3', u'3'],
        [u'4', u'4'],
        [u'5', u'5'],
        [u'6', u'6'],
        [u'7', u'7'],
        [u'8', u'8'],
        [u'9', u'9'],
        [u'10', u'10'],
        [u'11', u'11'],
        [u'12', u'12'],
        [u'13', u'13'],
    ]],
    [u'Нарушение условий страхования', u'narusheniya',[
        [u'Нет', u'1'],
        [u'Да', u'2'],
    ]]
]

DESCRIPTIONS = {
    'first_name': u'Имя',
    'last_name': u'Фамилия',
    'username': u'Имя пользователя',
    'phone_number': u'Телефонный номер',
    'price': u'Цена'
}

def get_text_question(question_id):
    if question_id is not None:
        try:
            result = DESCRIPTIONS[question_id]
        except KeyError:
            if question_id == 'city':
                return u'Город'
            else:
                for question in QUESTIONS:
                    if question[1] == question_id:
                        return u'%s' % question[0]
        else:
            return result
    else:
        return u''

def get_text_answer(question_id, answer_id):
    if question_id is not None and answer_id is not None:
        for question in QUESTIONS:
            if question_id=='city' and question[1]=='region':
                region_id = answer_id.split('_')[0]
                for region in question[2]:
                    if region[1] == region_id:
                        for city in region[2][2]:
                            if city[1] == answer_id:
                                return u'%s' % city[0]
            if question[1] == question_id:
                for answer in question[2]:
                    if answer[1] == answer_id:
                        return u'%s' % answer[0]
        return u'%s' % answer_id
    else:
        return u''

# if __name__ == "__main__":
#     print get_text_answer('city', '3_4')