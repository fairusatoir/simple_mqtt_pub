# MQTT Python Publisher Simple

MQTT Publisher with Python

## Description

This code provides a minimal use of Eclipse Paho MQTT Python client library as Publisher

## Getting Started

### Dependencies

- Python 3.8.8

### Installing

- Install paho-mqtt 1.5.1

### Executing program

- Open Python command prompt
- Change the variable before executing the code

```python
broker_ip = "broker.emqx.io"
broker_port = 1883
topic = "same/topic"

publishName = "pub1"
```

- Exce code

```console
python3 mqtt_pub_simple.py
```

or

```console
python mqtt_pub_simple.py
```

<!-- ## Help

In Python command prompt launch:

```console
python3 mqtt_sub.py -h
``` -->

## Authors

Contributors names and contact info

[@zuhairatoir](https://twitter.com/zuhairatoir)

## Version History

- 1.0
  - Initial Release

<!-- ## License

This project is licensed under the WTFPL - see the LICENSE.md file for details -->

## Acknowledgments

Inspiration, code snippets, etc.

- [Eclipse paho](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
