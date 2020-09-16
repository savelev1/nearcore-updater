# nearcore-updater

## Описание [RU]

**nearcore-updater** это скрипт, который с заданным интервалом проверяет обновления [nearcore](https://github.com/nearprotocol/nearcore). При наличии обновлений, скачивается новая версия [nearcore](https://github.com/nearprotocol/nearcore) и запускаются тесты. Если тесты завершились успешно, локальный nearcore обновляется на новую версию.

## Установка

### Установка зависимостей

```sudo apt update```

```sudo apt install python3 git curl jq```

У вас должен быть [обновленный](https://discord.com/channels/490367152054992913/708278589031710761/750253047145431110) [nearup](https://github.com/near/nearup/tree/nearup_v2)

### Установка nearcore-updater

```git clone https://github.com/savelev1/nearcore-updater.git /home/near/nearcore-updater```

nearcore-updater установится в директорию */home/near/nearcore-updater*. Вы можете ее изменить на свое усмотрение.

### Настройка запуска nearcore-updater с интервалом 1 час

```crontab -e```

В открывшемся окне редактирования Crontab добавьте в конец новую строку:

```0 */1 * * * /usr/bin/python3 /home/near/nearcore-updater/nearcore-updater.py betanet /home/near/nearcore > /tmp/nearcore-updater-cron.log 2>&1```

**✅Установка завершена**

Вы можете запустить скрипт вручную, чтобы убедится что все работает:

```python3 /home/near/nearcore-updater/nearcore-updater.py betanet /home/near/nearcore```

### Описание параметров запуска nearcore-updater

Скрипт имеет 3 параметра для запуска:

```<NETWORK>``` - название сети блокчейна **(обязательный)**

```<NEARCORE_DIR>``` - директория установки nearcore **(обязательный)**

```<ENABLE_LOG>``` - включить ли запись логов в файл nearcore-updater.log (необязательный, по умолчанию True)

Например, для сети testnet с расположением nearcore в /home/near/nearcore и с выключенными логами:

```0 */1 * * * /usr/bin/python3 /home/near/nearcore-updater/nearcore-updater.py testnet /home/near/nearcore False > /tmp/nearcore-updater-cron.log 2>&1```

### Обновление nearcore-updater

Перейдите в директорию расположения скрипта и вытяните обновления:

```cd /home/near/nearcore-updater && git pull```

## Description [EN]

**nearcore-updater** is a script that checks for updates at a specified interval [nearcore](https://github.com/nearprotocol/nearcore). If there are updates, a new version of [nearcore](https://github.com/nearprotocol/nearcore) is downloaded and tests are performed. If the tests are successful, the local nearcore is updated to the new version.

## Installation

### Installation of Dependency

```sudo apt update```

```sudo apt install python3 git curl jq```

You should also have [updated](https://discord.com/channels/490367152054992913/708278589031710761/750253047145431110) [nearup](https://github.com/near/nearup/tree/nearup_v2)

### Installation of nearcore-updater

```git clone https://github.com/savelev1/nearcore-updater.git /home/near/nearcore-updater```

nearcore-updater will install in the directory */home/near/nearcore-updater*. You can change it at your discretion.

### Setting the start of nearcore-updater at 1 hour intervals

```crontab -e```

In the Crontab edit window that opens add a new line to the end:

```0 */1 * * * /usr/bin/python3 /home/near/nearcore-updater/nearcore-updater.py betanet /home/near/nearcore > /tmp/nearcore-updater-cron.log 2>&1```

**✅Installation completed**

You can run the script manually to make sure that everything works:

```python3 /home/near/nearcore-updater/nearcore-updater.py betanet /home/near/nearcore```

### Description of nearcore-updater launch parameters

The script has 3 parameters to run:

```<NETWORK>``` - network name of the blockchain **(required)**

```<NEARCORE_DIR>``` - nearcore installation directory **(required)**

```<ENABLE_LOG>``` - enable logging in the nearcore-updater.log file (optional, by default True)

For example, for a testnet network with nearcore location in /home/near/nearcore and with logs disabled:

```0 */1 * * * /usr/bin/python3 /home/near/nearcore-updater/nearcore-updater.py testnet /home/near/nearcore False > /tmp/nearcore-updater-cron.log 2>&1```

### Update nearcore-updater

Go to the script directory and pull out the updates:

```cd /home/near/nearcore-updater && git pull```
