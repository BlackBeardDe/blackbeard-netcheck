# ---------------------------------------------------------------
#  Internet Speed Test Script
#  Developed by @Ilzci Black Beard
#  Powered by: Rich Library & Speedtest
# ---------------------------------------------------------------

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.text import Text
import speedtest
import time

console = Console()

def run_speed_test():
    console.print(Panel.fit(
        "[bold cyan]Welcome to the Internet Speed Test[/bold cyan]\n[white]By @Ilzci Black Beard[/white]",
        title="Black Beard Network Tool",
        border_style="bold cyan"
    ))

    try:
        with Progress(
            SpinnerColumn(style="bold green"),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None),
            transient=True
        ) as progress:
            progress.add_task(description="Initializing...", total=None)
            time.sleep(1)

        st = speedtest.Speedtest()

        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            progress.add_task(description="Finding Best Server...", total=None)
            st.get_best_server()
            time.sleep(0.5)

        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            progress.add_task(description="Testing Download Speed...", total=None)
            download_speed = st.download() / 1_000_000
            time.sleep(0.5)

        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
            progress.add_task(description="Testing Upload Speed...", total=None)
            upload_speed = st.upload() / 1_000_000
            time.sleep(0.5)

        ping = st.results.ping

        result = Text()
        result.append("\n[ Speed Test Results ]\n\n", style="bold underline")
        result.append(f"Download Speed : {download_speed:.2f} Mbps\n", style="bold green")
        result.append(f"Upload Speed   : {upload_speed:.2f} Mbps\n", style="bold blue")
        result.append(f"Ping           : {ping:.2f} ms\n", style="bold red")

        console.print(Panel(result, title="Test Complete", subtitle="Stay Fast, Stay Connected", border_style="bold white"))

    except Exception as e:
        console.print(Panel.fit(f"[bold red]An error occurred:[/bold red]\n{e}", border_style="red"))

run_speed_test()