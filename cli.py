import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def email(email_addres:str, block: bool = False):
    if block:
        print("Email sended")
    else:
        print(f"Email was send to the address {email_addres}")
    

if __name__ == "__main__":
    app()


