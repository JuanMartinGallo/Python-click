import json_manager
import click


@click.group()
def cli():
    pass


@cli.command()
def users():
    data = json_manager.read_json()
    for user in data:
        print(f"{user['id'] } - {user['name']} - {user['lastname']}")


@cli.command()
@click.pass_context
@click.option("--name", required=True, help="name of the user")
@click.option("--lastname", required=True, help="lastname of the user")
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail("the name and lastname are required")
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {"id": new_id, "name": name, "lastname": lastname}
        data.append(new_user)
        json_manager.write_json(data)
        print(f"User {name} {lastname} created successfully! with id {new_id}")


@cli.command()
@click.argument("id", required=True, type=int)
def search(id):
    data = json_manager.read_json()
    user = next((x for x in data if x["id"] == id), None)
    if user is None:
        print(f"User with id: {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument("id", required=True, type=int)
@click.option("--name", required=True, help="Name of the user")
@click.option("--lastname", required=True, help="Last name of the user")
def update(id, name, lastname):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if lastname is not None:
                user['lastname'] = lastname
            break    
    json_manager.write_json(data)
    print(f"User with id: {id} updated successfully!")

@cli.command()
@click.argument("id", required=True, type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x["id"] == id), None)
    if user is None:
        print(f"User with id: {id} not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"User with id: {id} deleted successfully!")


if __name__ == "__main__":
    cli()
