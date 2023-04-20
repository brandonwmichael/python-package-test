

def format_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    # full_name = f'{first_name}'
    return full_name

def main():
    assert format_name('John', 'Doe') == 'John Doe'
    
if __name__ == '__main__':
    main()