import click
from product_tracker.database import add_product


@click.group()
def cli():
    """Product Tracker CLI"""
    pass


@click.command()
@click.argument("name")
@click.argument("url")
@click.option("--threshold", default=None, type=float, help="Price alert threshold")
def add(name, url, threshold):
    """Add a new product to track"""
    add_product(name, url, threshold)
    click.echo(f"Tracking {name} at {url} with threshold {threshold}")


# Register commands
cli.add_command(add)

if __name__ == "__main__":
    cli()
