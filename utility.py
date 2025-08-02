import re

time_regex = re.compile(r"^(\d+)([smhd])$", re.IGNORECASE)

time_multipliers = {
    's': 1,
    'm': 60,
    'h': 3600,
    'd': 86400,
}

def parse_time_string(time_str):
    match = time_regex.match(time_str.strip())
    if not match:
        return None
    value, unit = match.groups()
    return int(value) * time_multipliers[unit.lower()]
