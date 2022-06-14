# Incluindo % dos cores
from time import sleep
from dashing import VGauge, VSplit, HSplit, HGauge
from psutil import virtual_memory, swap_memory, cpu_percent

ui = HSplit(  # ui
    HSplit(  # ui.items[0]
        VGauge(title='RAM'),  # ui.items[0].items[0]
        VGauge(title='Swap'),  # ui.items[0].items[0]
        title='Memória',
        border_color=3
    ),
    VSplit(  # ui.items[1]
        HGauge(title='CPU %'),  # ui.items[1].items[0]
        HGauge(title='cpu_0'),  # ui.items[1].items[1]
        HGauge(title='cpu_1'),  # ui.items[1].items[2]
        HGauge(title='cpu_2'),  # ui.items[1].items[3]
        HGauge(title='cpu_3'),  # ui.items[1].items[4]
        HGauge(title='cpu_4'),  # ui.items[1].items[5]
        HGauge(title='cpu_5'),  # ui.items[1].items[6]
        HGauge(title='cpu_6'),  # ui.items[1].items[7]
        HGauge(title='cpu_7'),  # ui.items[1].items[8]
        title='CPU',
        border_color=5
    ),
)


while True:
    # # Memoria
    # RAM
    ram_tui = ui.items[0].items[0]
    memoria = virtual_memory().percent
    ram_tui.title = f'RAM {memoria} %'
    ram_tui.value = memoria
    # SWAP
    swap_tui = ui.items[0].items[1]
    memoria = swap_memory().percent
    swap_tui.title = f'SWAP {memoria} %'
    swap_tui.value = memoria

    # # CPU
    cpu_tui = ui.items[1]
    # CPU %
    cpu_percent_tui = cpu_tui.items[0]
    ps_cpu_percent = cpu_percent()
    cpu_percent_tui.value = ps_cpu_percent
    cpu_percent_tui.title = f'CPU {ps_cpu_percent}%'

    # Porcentagem dos cores
    cores = cpu_tui.items[1:9]
    for i, (core, value) in enumerate(zip(cores, cpu_percent(percpu=True))):
        core.value = value
        core.title = f'cpu_{i} {value}%'

    try:
        ui.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
