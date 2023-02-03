# !/usr/bin/env python3


import random

GREETENG = ["Теробора України !!! Стій! Хто Іде? Ану переклади пароль з англійської"]
PASSWORD = ["hedgehog", "heaver", "eagle", "deer", "snake", "goose", "hare", "monkey", "dove", "turtle"]
N_DIALOG = ["Шо мовчиш?, москаль чи шо?", "Ану кажи пароль", "Микола, стрельни йому під ноги", "Ти шо німий?"]
NO_DIALOG = ["Підіймай руки і йди сюди, якщо не німий, то ми тебе розговоримо"]
UA_DIALOG = ["Вітаємо Козаче, Слава Україні!!!"]
PL_DIALOG = ["Powitanie nasz Рolski przyjaciel! Chwała Ukrainie!!!"]
GB_DIALOG = ["Welcome our English friend! Glory to Ukrain!!!"]
RU_DIALOG = ["Ну от і все, гейм овер!. Микола доставай пакет, будемо депортірувати на \"родіну\"."]
F_DIALOG = ["Йо Йо Йой, щось тут не те, ану ще разок",
            "Микола ти це чув? Шукай гиляку. Ану ще раз",
            "А ти часом не москаль? ану спробуй знову",
            "Але ж ти і підозрілий! Давай знов ",
            "Ану ше раз, поки Микола готує мотузку "]
ATTEMPTS = 4
T_PASSWORD = '> '


def dialog():
    """User dialog logic."""
    password = PASSWORD[random.randrange(0, len(PASSWORD))]
    print(f"{GREETENG}:\n{password}")
    entry = input(T_PASSWORD).strip().lower()  # user entry
    attempts = ATTEMPTS
    while attempts > 0:
        if not entry and attempts == 1:
            return print(NO_DIALOG)
        elif not entry:
            print(f"{N_DIALOG[random.randrange(0, len(N_DIALOG))]}")
            print(password)
        else:
            if attempts == 1:
                return print(RU_DIALOG)
            for i in entry:
                if i in "aeuoiy":
                    return print(GB_DIALOG)
            for i in entry:
                if i in "ąćęłńóśźż":
                    return print(PL_DIALOG)
            for i in entry:
                if i in "іїґє'":
                    return print(UA_DIALOG)
            print(F_DIALOG[random.randrange(0, len(F_DIALOG))])
            password = PASSWORD[random.randrange(0, len(PASSWORD))]
            print(password)
        entry = input(T_PASSWORD).strip().lower()
        attempts -= 1



def main(args):
    script, *args = args
    if args:
       exit('Too many arguments. ' )

    else:
        dialog()

if __name__ == '__main__':
   import sys

   main(sys.argv)
