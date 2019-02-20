# service-monitor
A github repo containing code to monitor different types of services using python

## Pre-requisites
* Python 2.7
* `virtualenv` must be installed
* Any service which needs to be monitored should be installed and running e.g. `redis`

## Installation

* **Clone the git repository**

    ```
    git clone git@github.com:nitinpandey-154/service-monitor.git
    ```
    
* **Go to the `service-monitor` folder and install requirements inside virtualenv**
    ```
    cd service-monitor
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    
* **Create the `logs` folder**
    ```
    mkdir service-monitor/log
    ```
* **Configuration File**

    A sample configuration file is provided. The structure should be as follows:
    
    ```
    {
      "services": {
        "monitor-rest": {
          "type": "rest",
          "end-point": "https://httpbin.org/ip",
          "return-code": 200,
          "method": "get"
        },
        "local-redis": {
          "type": "redis",
          "host": "localhost",
          "port": 6379,
          "db": 0
        }
      }
    }

    ```
    
    Add the respective blocks inside `services` to monitor more.
    
 ## Executing
 
 * Run using the below command:
 
    ```
    python run.py -c monitoring/config/config.json
    ```