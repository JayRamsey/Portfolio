from rich.console import Console
from rich.markdown import Markdown
from rich.align import Align
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from rich.live import Live
import psutil
from time import sleep
import numpy


import cpuinfo

console = Console()

cpuInfoDict = cpuinfo.get_cpu_info()
coreCount = cpuInfoDict["count"]
cpuArch = cpuInfoDict["arch"]
cpuProduct = cpuInfoDict["brand_raw"]
cpuHz = cpuInfoDict["hz_actual_friendly"]


with Live(console=console, screen=True) as live:

    while True:
        currentUsage = psutil.cpu_percent() * 10
        cpuUsageColour = "green"
        
        if 0 < currentUsage <= 35:
            pass
        elif 35 < currentUsage <= 60:
            cpuUsageColour = "yellow"
        elif 60 < currentUsage <= 80:
            cpuUsageColour = "rgb(255,102,0)"
        else:
            cpuUsageColour = "red"
        
        cpuValues = Table()
        cpuValues.add_column("Field", style="green")
        cpuValues.add_column("Value", style="purple")
        cpuValues.add_row("CPU", cpuProduct, style="purple")
        cpuValues.add_row("Cores", str(coreCount), style="blue")
        cpuValues.add_row("Architecture", cpuArch, style="white")
        cpuValues.add_row("Base Speed", str(cpuHz), style="yellow")
        cpuValues.add_row("Usage", str(currentUsage) + "%", style=cpuUsageColour)
        
        
        ramUsage = psutil.virtual_memory()
        ramPercent = ramUsage[2]
        ramUsageColour = "green"
        if 0 < ramPercent <= 40:
            pass
        elif 40 < ramPercent <= 60:
            ramUsageColour = "yellow"
        elif 60 < ramPercent <= 80:
            ramUsageColour = "rgb(255,102,0)"
        else:
            ramUsageColour = "red"
            
        ramValues = Table(title="RAM")
        ramValues.add_column("Field", style="cyan")
        ramValues.add_column("Value", style="yellow")
        ramValues.add_row("Total", str(numpy.round(ramUsage[0] / 1000000000, 2)) + "GB")
        ramValues.add_row("Available", str(numpy.round(ramUsage[1] / 1000000000, 2)) + "GB", style=ramUsageColour)
        ramValues.add_row("Percentage Used", str(ramPercent) + "%", style=ramUsageColour)
        
        data = Columns([cpuValues, ramValues])

        live.update(data)
        sleep(3)
        