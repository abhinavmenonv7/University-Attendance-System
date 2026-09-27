def validate_roll(roll):
    if roll.strip() == "":
        return False
    return True
def validate_attendance_status(status):
    status = status.upper()
    if status == "P" or status == "A":
        return True
    return False