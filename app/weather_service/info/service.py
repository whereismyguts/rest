
def is_temp_cross_zero(temp_list):
    prev_sign = None
    for tmp in temp_list:
        if tmp == 0:
            return True

        sign = tmp > 0 - tmp < 0
        if prev_sign is not None:
            if sign != prev_sign:
                return True
        prev_sign = sign
    return False
