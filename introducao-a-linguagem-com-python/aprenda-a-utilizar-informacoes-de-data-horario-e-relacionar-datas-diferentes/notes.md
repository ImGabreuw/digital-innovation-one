# Aprenda a utilizar informações de data, horário e relacionar datas diferentes

### Data

* **Obter a data atual**

  * **Sintaxe**

    ```python
    from datetime import date

    date.today()
    ```

  * **Exemplo**

    ```python
    from datetime import date

    data_atual = date.today()
    print(data_atual) # 2021-07-09
    ```

* **Formatar a data no padrão brasileiro**

  * **Sintaxe**

    ```python
    data.strftime("%d/%m/%y")
    ```

  * **Exemplo**

    ```python
    from datetime import date

    data_atual = date.today()
    print(data_atual.strftime("%d/%m/%Y")) # 09/07/2021
    ```

### Time

* **Criar um horário**

  * **Sintaxe**

    ```python
    from datetime import time

    time(hour=<horas>, minute=<minutos>, second=<segundos>)
    ```

  * **Exemplo**

    ```python
    from datetime import time

    horario = time(hour=15, minute=18, second=30)
    print(horario) # 15:18:30
    ```

* **Formatar um horário**

  * **Sintaxe**

    ```python
    horario.strftime("formato")
    ```


  * **Exemplo**

    ```python
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime("%H:%M:%S")) # 15:18:30
    ```

### Datetime

* **Obter data e hora atual**

  * **Sintaxe**

    ```python
    from datetime import datetime

    datetime.now()
    ```

  * **Exemplo**

    ```python
    from datetime import datetime

    data_atual = datetime.now()
    print(data_atual) # 2021-07-09 16:31:23.313105 
    ```

* **Formatação um datetime**

  * **Sintaxe**

    ```python
    datahora.strftime("formato")
    ```

  * **Exemplo**

    ```python
    from datetime import datetime

    data_atual = datetime.now()

    print(data_atual.strftime("%d/%m/%Y")) # 09/07/2021
    print(data_atual.strftime("%d/%m/%Y %H:%M:%S")) # 09/07/2021 16:34:20
    print(data_atual.strftime("%c")) # Fri Jul  9 16:35:09 2021
    ```
