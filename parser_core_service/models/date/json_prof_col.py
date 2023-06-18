import json

gallery_eco = [
"Аудитор",
"Финансовый аналитик",
"Брокер",
"Продавец",
"Кредитный консультант",
"Маркетолог",
"Страховой агент",
"Торговый представитель",
"Экономист",
"Финансист",]

gallery_med = [
"Акушер-гинеколог",
"Аллерголог",
"Венеролог",
"Врач скорой медицинской помощи",
"Гастроэнтеролог",
"Дерматолог",
"Диетолог",
"Кардиолог",
"Косметолог",
"Нарколог",
"Онколог",
"Ортодонт",
"Ортопед",
"Офтальмолог",
"Пластический хирург",
"Проктолог",
"Психиатр",
"Психотерапевт",
"Рентгенолог",
"Терапевт",
"Травматолог",
"Фармацевт",
"Фельдшер",
"Хирург",
"Уролог",
"Эндокринолог",
"Эпидемиолог",]

gallery_it = [
"Администратор базы данных",
"Веб-интеграторT",
"Оператор ПК",
"Веб-мастер",
"Программист",
"Кодер",
"Веб-программист",
"Тестировщик",
"Геймдизайнер",
"Системный администратор",
]
gallery_inge = [
"Автослесарь",
"Автоэлектрик",
"Инженер-конструктор",
"Инженер-механик",
"Инженер по Технике Безопасности",
"Инженер-системотехник",
"Инженер-строитель",
"Кабельщик",
"Кровельщик",
"Маляр",
"Механик",
"Монтажник",
"Плотник",
"Сантехник",
"Сборщик",
"Сварщик",
"Техник",
"Токарь",
"Швея",
"Штукатур",
"Электрик",
]

gallery_sn = [
"Философ",
"Физик",
"Биолог",
"Футуролог",
"Географ",
"Геодезист",
"Зоолог",
"Логик",
"Эколог",
"Математик",
"Социолог",
]

gallery_tvor = [
"Актёр",
"Балерина",
"Визажист",
"Иллюстратор",
"Модель",
"Фотомодель",
"Фотограф",
"Танцор",
"Вокалист",
"Гитарист",
"Композитор",
"Режиссёр",
"Танцор",
"Флорист",
"Художник",
]

gallery_ur = [
"Адвокат",
"Кинолог",
"Государственный исполнитель",
"Нотариус",
"Правовед",
"Прокурор",
"Работник органов ЗАГСа",
"Телохранитель",
"Юрисконсульт",
"Юрист",
"Таможенник",
]

coll = {
    "Экономические профессии": gallery_eco,
    "Медицинские профессии": gallery_med,
    'IT профессии': gallery_it,
    "Технические\Инженерные": gallery_inge,
    "Научные профессии": gallery_sn,
    "Творческие профессии": gallery_tvor,
    "Юридические, правоохранительны": gallery_ur
}

with open('professions.json', 'w') as file:
    t = json.dumps(coll, indent = 4,ensure_ascii = False)
    file.write(t)