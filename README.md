# search_engine
Поисковик написан без использования либ, только статистика и горсточка логики.

Это подсказчик для запросов на основе примерных запросов из phrases.txt

В ходе работы программы введенное слово сначала проверяется на опечатки, а потом ищутся возможные концы запроса и возвращаются лучшие из них.

Чуть больше про сортровку запросов: длинные запросы из базы приоретнее коротких запросов из базы. Это приоритетнее коротких запросов не из базы. Худший вариант - длинный запрос не из базы.
В его логике также учтено, что короткое слово в конце запроса (вероятно, предлог) -- это не круто


## How to start
```python
python main.py
```

```
>>> Переводчик

переводчик с английского на русский
переводчик с английского
переводчик онлайн
переводчик
переводчик гугл
```

```
>>> одноклассники

одноклассники ru социальная моя страница
одноклассники ru социальная
одноклассники моя страница
одноклассники ru социальная сеть
одноклассники
```
