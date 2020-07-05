def div(func):
    # You have to code here!
    def wrapper(*args):
        
        print(f'<div>{func(*args)}</div>')
        
        
    return wrapper


def article(func):
    # You have to code here!
    def wrapper(*args):
        
        print(f'<article>{func(*args)}</article>')
        
        
    return wrapper


def p(func):
    # You have to code here!
    def wrapper(*args):
        
        print(f'<p>{func(*args)}</p>')
        
        
    return wrapper


# Here you must apply the decorators, uncomment this later
# @div
#@article
@p
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
