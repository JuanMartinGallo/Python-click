import json_manager
import click


@click.group()
def cli():
    pass


@cli.command()
def users():
    """
    Retrieves the list of users and prints their information.

    This function does not take any parameters.

    Returns:
        None

    Raises:
        None
    """
    data = json_manager.read_json()
    for user in data:
        print(f"{user['id'] } - {user['name']} - {user['lastname']}")


@cli.command()
@click.pass_context
@click.option("--name", required=True, help="name of the user")
@click.option("--lastname", required=True, help="lastname of the user")
def new(ctx, name, lastname):
    """
    Creates a new user with the given name and lastname.

    Parameters:
        ctx (click.Context): The click context object.
        name (str): The name of the user.
        lastname (str): The lastname of the user.

    Returns:
        None
    """
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
    """
    Searches for a user with the given id in the data stored in the JSON file.
    
    Parameters:
        id (int): The id of the user to search for.
    
    Returns:
        None
    """
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
    """
    Update a user's name and last name in the database based on their ID.
    
    Args:
        id (int): The ID of the user to update.
        name (str): The new name of the user.
        lastname (str): The new last name of the user.
    
    Returns:
        None
    
    Raises:
        None
    """
    data = json_manager.read_json()
    for user in data:
        if user["id"] == id:
            if name is not None:
                user["name"] = name
            if lastname is not None:
                user["lastname"] = lastname
            break
    json_manager.write_json(data)
    print(f"User with id: {id} updated successfully!")


@cli.command()
@click.argument("id", required=True, type=int)
def delete(id):
    """
    Deletes a user with the specified id.

    Parameters:
        id (int): The id of the user to be deleted.

    Returns:
        None
    """
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
