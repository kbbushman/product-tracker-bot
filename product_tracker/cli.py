import click
from product_tracker.database import add_product, get_products, delete_product


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


@click.command()
def list():
    """List all products in the database"""
    products = get_products()
    if not products:
        click.echo("No products found.")
    else:
        click.echo("Products in Database:")
        for product in products:
            click.echo(
                f"ID: {product['id']} | Name: {product['name']} | URL: {product['url']} | Threshold: {product['threshold']} | Date Added: {product['date_added']}"
            )


@click.command()
@click.argument("product_id")
def delete(product_id):
    """Delete a product from the database"""
    delete_product(product_id)
    click.echo(f"Deleted product with ID {product_id}")


# Register commands
cli.add_command(add)
cli.add_command(list)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
