from rich.console import Console

console = Console()

while True:
    console.clear()

    remaining_questions = input("Total  Questions (\"exit\" to exit)\n> ")
    if remaining_questions == "exit":
        break
    remaining_questions = int(remaining_questions)
    while remaining_questions > 0:
        console.clear()
        console.rule(f"Remaining Questions: [yellow]{remaining_questions}[/yellow]")
        console.print("Press [bold]Enter[/bold] to register a question")
        input()
        remaining_questions -= 1

    console.print("OUT OF QUESTIONS!!!!")
    console.print("Press [bold]Enter[/bold] to restart")
