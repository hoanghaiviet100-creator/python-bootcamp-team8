from shared.contract import Block
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

def render(blocks: list[Block]) -> None:
    """Hiển thị danh sách các block học tập ra màn hình CLI."""
    console = Console()
    
    if not blocks:
        console.print("[bold red]No study blocks.[/bold red]")
        return
        
    table = Table(
        title="📚 KẾ HOẠCH HỌC TẬP 📚", 
        show_header=True, 
        header_style="bold magenta",
        border_style="cyan"
    )
    
    table.add_column("STT", justify="center", width=5)
    table.add_column("Tên Task", style="white", width=40)
    table.add_column("Thời gian (giờ)", justify="right", style="green", width=15)
    
    for index, block in enumerate(blocks, start=1):
        # Dùng block.task.title và block.hours giống file cũ của bạn
        table.add_row(
            str(index), 
            block.task.title, 
            f"{block.hours:.1f}h"
        )
        
    console.print(table)
    
    total_hours = sum(block.hours for block in blocks)
    console.print(Panel(
        f"Tổng thời gian phân bổ: [bold green]{total_hours:.1f}h[/bold green]", 
        expand=False, 
        border_style="green"
    ))