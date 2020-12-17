import re

def validate_passport(passport, ignoreCID, validate_values):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not ignoreCID:
        required_fields.append('cid')

    for field in required_fields:
        if field not in passport:
            return False

    if validate_values:
        # Birth year, issue year, expiration year
        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            return False
        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            return False
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            return False

        # Height
        height, unit = int(passport['hgt'][:-2]), passport['hgt'][-2:]
        if unit == 'cm':
            if height < 150 or height > 193:
                return False
        elif unit == 'in':
            if height < 59 or height > 76:
                return False
        else:
            return False

        # Hair and eye color
        if not re.fullmatch('#[0-9a-f]{6}', passport['hcl']):
            return False
        if passport['ecl'] not in ['amb', 'blu', 'brn', 
                                   'gry', 'grn', 'hzl', 'oth']:
            return False
        # Passport ID
        if len(passport['pid']) != 9 or not passport['pid'].isdecimal():
            return False

    return True

def count_valid_passports(filename, ignoreCID, validate_values):
    valid_count = 0
    with open(filename) as input_file:
        passport = {}
        for line in input_file:
            if line.isspace():
                valid_count += validate_passport(passport, ignoreCID,
                                                 validate_values)
                passport.clear()

            else:
                for field in line.split():
                    key, value = field.split(':')
                    passport[key] = value
        # Check the last passport
        valid_count += validate_passport(passport, ignoreCID, validate_values)
    return valid_count

def main():
    print(count_valid_passports("day4-input.txt", True, False))
    print(count_valid_passports("day4-input.txt", True, True))

if __name__ == "__main__":
    main()