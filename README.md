# ⚡ Checker
> A simple and lightweight discord token checker

Join the [server](https://discord.gg/pop) or dm me on discord (x5n9) for support/questions.

> [!CAUTION]
> Pasting/selling this script might cause you to develop extreme autism and will have long-term consequences, use responsibly.




### Features
- Proxy support
- Lightweight
- No token locks
- Threading
- Very easy to use




### Installation

Open any terminal and type the following command
```bash
git clone https://github.com/vividsex/discord-token-checker
cd discord-token-checker/checker
```
> [!NOTE]
> Git is required! If not available; download this repository manually by clicking the green dropdown and selecting the Download Zip button

After cloning the repo, run the given command to install the requirements for the checker
```bash
python3 -m pip install -r requirements.txt
; OR
pip install -r requirements.txt
```
After this, you can run main.py with python and the checker should start, after it finishes - the output will be dumped in the ./output/ dir.


> [!NOTE]
> Please make sure you have filled the config and the tokens file before running the script!


### Config
> ./data/config.toml
```toml
[main]
threads = 50         # Number of threads to use, recommended - 100-200
proxyless = false    # Proxies are recommended but not neccesary
```
> ./data/settings.json
```json
{
    "nitro": true,    // Filter tokens based on nitro?
    "age": true,      // Filter tokens based on age?
    "type": true,     // Filter tokens based on type? (Ev, fv)
    "flagged": true   // Filter tokens if they are flagged?
}
```



### Proxies
> ./dats/proxies.txt

Supported formats are:
```
user:pass@ip:port
ip:port
```
Please do NOT use free proxies.




### Tokens
> ./data/tokens.txt


Supported formats are:
```
email:pass:token
token
```

### Screenshots
![screenshot](https://media.discordapp.net/attachments/1222528933522837609/1224327780867510362/image.png?ex=661d1719&is=660aa219&hm=aadbbf337251bbec55473f512e699faafb1c6dc63f243aa24824f7892e8ff58d&=&format=webp&quality=lossless&width=1151&height=626)


# <3
> __Pull requests are welcome.__

> __Made with ❤ by vv__



