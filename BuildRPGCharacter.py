full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # 2. Empty name validation
    if name == '':
        return 'The character should have a name'
    
    # 3. Name length validation
    if len(name) > 10:
        return 'The character name is too long'
    
    # 4. Spaces in name validation
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    # 5. Stat type validation (using type() ensures booleans are excluded)
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return 'All stats should be integers'
    
    # 6. Minimum stat value validation
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    
    # 7. Maximum stat value validation
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    
    # 8. Stat point sum validation
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    # Format character stats string
    str_line = f"STR {full_dot * strength}{empty_dot * (10 - strength)}"
    int_line = f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
    cha_line = f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
    
    return f"{name}\n{str_line}\n{int_line}\n{cha_line}"