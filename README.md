# nearcore-updater

## Описание

**nearcore-updater** это скрипт, который раз в час проверяет обновления [nearcore](https://github.com/nearprotocol/nearcore). При наличии обновлений, скачивается новая версия [nearcore](https://github.com/nearprotocol/nearcore) и запускаются тесты. Если тесты завершились успешно, локальный nearcore обновляется на новую версию.

## Установка

**Установка зависимостей**

```sudo apt update```

```sudo apt install python3 git curl jq```

**Установка nearcore-updater**

```git clone https://github.com/savelev1/nearcore-updater.git /home/near/nearcore-updater```

nearcore-updater установится в директорию */home/near/nearcore-updater*. Вы можете ее изменить на свое усмотрение.

**Установка запуска скрипта с интервалом 1 час**

```crontab -e```

В открывшемся окне редактирования Crontab добавьте новую строку в конце:

```0 */1 * * * export NODE_ENV=betanet && /usr/bin/python3 /home/near/nearcore-updater/nearcore-updater.py betanet /home/near/nearcore > /tmp/nearcore-updater-cron.log 2>&1```

**На этом этапе установка завершена**

Вы можете запустить скрипт вручную, чтобы убедится что все работает:

```python3 /home/near/nearcore-updater/nearcore-updater.py betanet /home/near/nearcore```

**Описание параметров запуска nearcore-updater**

Скрипт имеет 3 параметра для запуска

```<NETWORK>``` - название сети блокчейна **(обязательный)**

```<NEARCORE_DIR>``` - директория установки nearcore **(обязательный)**

```<ENABLE_LOG>``` - включить ли запись логов в файл nearcore-updater.log (необязательный, по умолчанию True)

Например, для сети testnet с расположением nearcore в /home/near/nearcore и с выключенными логами:

```0 */1 * * * export NODE_ENV=betanet && /usr/bin/python3 /home/near/nearcore-updater/nearcore-updater.py testnet /home/near/nearcore False > /tmp/nearcore-updater-cron.log 2>&1```
