# Use PYTHON 3.10 - 3.11.5 


## [Settings]

| Settings | Description |
|----------------------------|:-------------------------------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**      | Platform data from which to run the Telegram session (default - android)                                      |       
| **REF_LINK**               | Put your ref link here (default: )                                                                 |
| **AUTO_TASK**              |  Auto do tasks (default: True)                                                                                  |
| **AUTO_UPGRADE_PAINT_REWARD** | AUTO upgrade paint reward if possible (default: True)                                                                      |
| **AUTO_UPGRADE_RECHARGE_SPEED** | AUTO upgrade recharge speed if possible (default: True)                                                                      |
| **AUTO_UPGRADE_RECHARGE_ENERGY** | AUTO upgrade energy limit if possible (default: True)                                                                      |
| **USE_CUSTOM_TEMPLATE** | Use custom template if it's disabled global template will be used (default: True)                                                    |
| **CUSTOM_TEMPLATE_ID** | your custom template id (default: my template id)                                                                      |
| **USE_RANDOM_TEMPLATES** | Option to use random templates on catalog (default: False)                                                                      |
| **RANDOM_TEMPLATES_ID** |List of templates id (default: list of templates on catalog )                                                                      |
| **NIGHT_MODE** | Sleep time for the bot (default: True)                                                                      |
| **SLEEP_TIME** | Sleep in your timezone for the bot (default: [0, 7] 0am to 7am)                                                                     |
| **DELAY_EACH_ACCOUNT** | Sleep time in second between each account(non multi thread) (default: [10, 15])                                                                     |
| **SLEEP_BETWEEN_EACH_ROUND** | Sleep time in second between each round (default: [1000, 1500])                                                                     |
| **ADVANCED_ANTI_DETECTION** | More protection for your account ;-; (default: False)                                                                     |
| **USE_PROXY_FROM_FILE**    | Whether to use a proxy from the bot/config/proxies.txt file (True / False)                                    |


## Quick Start

To install libraries and run bot - open run.bat on Windows

## Installation

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/Notpixel-bot >>> python3 main.py --action (1/2)
# Or
~/Notpixel-bot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```
You can also use arguments for quick start, for example:
```shell
~/Notpixel-bot >>> python3 main.py --action (1/2)
# Or
~/Notpixel-bot >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```
