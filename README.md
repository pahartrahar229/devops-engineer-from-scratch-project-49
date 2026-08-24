[![Actions Status](https://github.com)](https://github.com)
# Brain Games

Учебный проект: набор консольных игр на Python. Каждая игра задаёт пользователю
случайные вопросы. Чтобы победить, нужно дать три правильных ответа подряд.
При первом неверном (или некорректном) ответе игра завершается.

## Установка

```bash
uv build
uv tool install --force dist/*.whl
```

## Игры

### brain-games
Приветствие пользователя.

```bash
brain-games
```

### brain-even — Проверка на чётность
Показывается случайное число. Нужно ответить `yes`, если оно чётное, или `no` — если нечётное.

[![asciicast](https://asciinema.org/a/ejTIVVx4aCnQCh5E.svg)](https://asciinema.org/a/ejTIVVx4aCnQCh5E)

```bash
brain-even
```

### brain-calc — Калькулятор
Показывается случайное математическое выражение (`+`, `-`, `*`). Нужно вычислить и ввести правильный ответ.

[![asciicast](https://asciinema.org/a/6A8ykwEE1NK5pW0r.svg)](https://asciinema.org/a/6A8ykwEE1NK5pW0r)

```bash
brain-calc
```

### brain-gcd — Наибольший общий делитель
Показываются два случайных числа. Нужно найти их наибольший общий делитель.

[![asciicast](https://asciinema.org/a/iizEfDbyuoz9dTe2.svg)](https://asciinema.org/a/iizEfDbyuoz9dTe2)

```bash
brain-gcd
```

### brain-progression — Арифметическая прогрессия
Показывается ряд чисел, образующих арифметическую прогрессию, с одним пропущенным
числом (заменено на `..`). Нужно определить пропущенное число.

[![asciicast](https://asciinema.org/a/4x1OLTmxeaBNBEGH.svg)](https://asciinema.org/a/4x1OLTmxeaBNBEGH)

```bash
brain-progression
```

### brain-prime — Простое ли число?
Показывается случайное число. Нужно ответить `yes`, если оно простое, или `no` — если нет.

[![asciicast](https://asciinema.org/a/Ud4M0GvDUvopLr0I.svg)](https://asciinema.org/a/Ud4M0GvDUvopLr0I)

```bash
brain-prime
```

## Разработка

```bash
make lint    # проверка стиля кода (ruff)
make build   # сборка пакета
```

