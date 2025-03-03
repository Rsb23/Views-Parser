# Views-Parser
CLI interface that takes a number of views and formats it for video format, inspired heavily by YouTube's formatting.
# Installation
```bash
python3 -m venv <venv name>
```
Activate Virtual Environment
```bash
pip3 install -r requirements.txt
```
```bash
python3 main.py <number of views>
```
# Usage
```bash
python3 main.py -n 2345859

2M Views
```
```bash
python3 main.py -n 243

243 Views
```
```bash
python3 main.py -n 1

1 View
```
```bash
python3 main.py -n 34903

34K Views
```
```bash
python3 main.py -n 0

No Views
```