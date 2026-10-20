# PASAMOS UN STRING A UNA VARIABLE Y UTILIZAMOS LA FUNCION FIND PARA BUSCAR LA POSICION DE UN CARACTER EN EL STRING

email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

has_at = '@' in email
print(f'Has @ symbol: {has_at}')