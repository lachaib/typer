from datetime import datetime

from typer import Argument, Option, Typer, echo
from typing_extensions import Annotated, TypeAlias

app = Typer()

Name: TypeAlias = Annotated[str, Argument(help="The name of the user.")]
Title: TypeAlias = Annotated[str, Option(help="The title of the user.")]

@app.command()
def greet(name: Name, title: Title="Mr") -> None:
    """Greet the user with their name and title."""
    echo(f"Hello, {title} {name}!")

@app.command()
def farewell(name: Name, title: Title="Mr")-> None:
    """Bid farewell to the user with their name and title."""
    echo(f"Goodbye, {title} {name}!")

Country: TypeAlias = Annotated[str, "The name of a country."]
Countries: TypeAlias = Annotated[list[Country], Option("--country", help="List of countries you've visited.", default_factory=list)]

@app.command()
def countries(countries: Countries) -> None:
    """List the countries you've visited."""
    echo(f"You've visited: {', '.join(countries)}")
    echo("Thank you for sharing your travel experiences!")

type City = Annotated[str, "The name of a city."]
type BirthDate = Annotated[datetime, "The date of birth of the user."]
type BirthInfo = Annotated[tuple[City, BirthDate], Argument(help="The city and date of birth of the user.")]

@app.command()
def birth_info(birth_info: BirthInfo) -> None:
    """Display the user's birth information."""
    city, date = birth_info
    echo(f"You were born in {city} on {date}.")

if __name__ == "__main__":
    app()
# To run this code, save it to a file named `tutorial001_type_alias.py` and run it with: