from datetime import date, time, datetime


def trabalhando_com_datetime():
    data_atual = datetime.now()

    print(data_atual)

    print(data_atual.strftime("%d/%m/%Y"))
    print(data_atual.strftime("%d/%m/%Y %H:%M:%S"))
    print(data_atual.strftime("%c"))
    print(data_atual.day)
    print(data_atual.month)
    print(data_atual.year)
    print(data_atual.weekday())
    print(data_atual.date())


def dia_da_semana_em_ptbr():
    tupla = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
    data_atual = datetime.now()

    print(tupla[data_atual.weekday()])


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime("%d/%m/%Y"))
    print(data_atual.strftime("%A %B %Y"))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime("%H:%M:%S"))


if __name__ == '__main__':

    # Exemplo 1:
    # trabalhando_com_date()

    # Exemplo 2:
    # trabalhando_com_time()

    # Exemplo 3:
    # trabalhando_com_datetime()

    # Exemplo 4:
    dia_da_semana_em_ptbr()
