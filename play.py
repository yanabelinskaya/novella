import random

characters_list = ['Яночка', 'Юрочка', 'Сонечка', 'Мишка', 'Боречка', 'Лизочка', 'Марфочка']

characters_info = {
    'Яночка': 'Добрая и веселая девушка.',
    'Юрочка': 'Самый лучший красивый, умный парень. Все его хотят, но ему нравится Яночка.',
    'Сонечка': 'Умная и привлекательная девушка.',
    'Мишка': 'Объездил весь мир, нарцис.',
    'Боречка': 'Спортивный, любит футбол.',
    'Лизочка': 'Красивая девушка, хочет найти daddy.',
    'Марфочка': 'Талантливая художница, всего может добиться сама.',
}

locations_list = ['Школа', 'Макдональдс', 'Дом', 'Кинотеатр', 'Тусовка']

locations_info = {
    'Школа': 'Место, где познакомились персонажи.',
    'Макдональдс': 'Можно поесть и поговорить по душам.',
    'Дом': 'Можно поиграть и отдохнуть.',
    'Кинотеатр': 'Место для досуга.',
    'Тусовка': 'Можно отдохнуть и не думать о каких-либо проблемах.',
}

common_actions = ['Поцелуи', 'Разговоры', 'Прогулки', 'Фотосессия', 'Еда', 'Фильм', 'Отдых', 'Игра', 'Учеба']

def display_intro():
    print("Добро пожаловать в клуб романтики!")
    print("Выберите персонажа и место для свидания.")
    print("\nДоступные персонажи:")
    for character in characters_list:
        print(f"{character}: {characters_info[character]}")
    
    print("\nДоступные места:")
    for location in locations_list:
        print(f"{location}: {locations_info[location]}")

def choose_characters():
    print("Выберите способ выбора персонажей для свидания:")
    print("1. Выбрать вручную")
    print("2. Выбрать случайно")
    
    choice = input("Введите номер способа: ")
    if choice == '1':
        return choose_manual_characters()
    elif choice == '2':
        return choose_random_characters()
    else:
        print("Некорректный выбор. Выбран способ выбора по умолчанию (случайный выбор).")
        return choose_random_characters()

def choose_manual_characters():
    print("Выберите двух персонажей для свидания:")
    for index, character in enumerate(characters_list, start=1):
        print(f"{index}. {character}")

    chosen_characters = set()
    while len(chosen_characters) < 2:
        choice = input(f"Введите номер {len(chosen_characters) + 1} персонажа: ")
        if choice.isdigit() and 1 <= int(choice) <= len(characters_list):
            chosen_characters.add(characters_list[int(choice) - 1])
        else:
            print("Некорректный выбор. Попробуйте снова.")
    return chosen_characters

def choose_random_characters():
    random_characters = random.sample(characters_list, 2)
    print(f"Случайный выбор персонажей: {', '.join(random_characters)}")
    return set(random_characters)

def choose_action():
    print("\nВыберите действие для свидания:")
    for index, action in enumerate(common_actions, start=1):
        print(f"{index}. {action}")
    
    while True:
        choice = input("Введите номер действия для свидания: ")
        if choice.isdigit() and 1 <= int(choice) <= len(common_actions):
            return common_actions[int(choice) - 1]
        else:
            print("Некорректный выбор. Попробуйте снова.")

def choose_location():
    print("\nВыберите место для свидания:")
    for index, location in enumerate(locations_list, start=1):
        print(f"{index}. {location}")
    
    while True:
        choice = input("Введите номер места для свидания: ")
        if choice.isdigit() and 1 <= int(choice) <= len(locations_list):
            return choice
        else:
            print("Некорректный выбор. Попробуйте снова.")

def rate_date():
    while True:
        rating = input("Пожалуйста, оцените свидание от 1 до 10 (10 - отлично, 1 - плохо): ")
        if rating.isdigit() and 1 <= int(rating) <= 10:
            return int(rating)
        else:
            print("Некорректная оценка. Попробуйте снова.")

def display_final_message(characters, location, action):
    print(f"\nСвидание в {locations_list[int(location) - 1]} с {' и '.join(characters)}:")
    print(f"\nДействие во время свидания: {action}")
    chosen_rating = rate_date()
    print(f"\nВы оценили свидание как {chosen_rating} из 10.")

def main():
    display_intro()
    chosen_characters = choose_characters()
    chosen_action = choose_action()
    chosen_location = choose_location()
    display_final_message(chosen_characters, chosen_location, chosen_action)

if __name__ == "__main__":
    main()


       
