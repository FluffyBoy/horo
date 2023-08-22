from horo_mail import get_horo
from rich.console import Console

console = Console(width=81)

message = get_horo()

console.print(message, overflow='fold', style="bold green")
console.input("Press enter to exit...")

