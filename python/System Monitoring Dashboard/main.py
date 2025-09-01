import psutil
from flask import Flask

app = Flask(__name__)

@app.route('/')
def stuff():
    info = []
    task = psutil.sensors_temperatures(fahrenheit=False)

    for name, entries in task.items():
        for entry in entries:
            info.append("Temperature: {} °C ".format(entry.current))
        break

    battery = psutil.sensors_battery()

    info.append("CPU Usage: {}%".format(psutil.cpu_percent()))
    memory = psutil.virtual_memory()
    info.append("Memory Usage: {}%".format(memory.percent))
    disk = psutil.disk_usage('/')
    info.append("Available Space: {} GB".format(round(disk.free / (1024 * 1024 * 1024), 2)))

    return '<br>'.join(info)

if __name__ == "__main__":
    app.run(debug=True, host="192.168.1.120", port=6969)
    