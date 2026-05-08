def validate_input(data):
    if data['area'] <= 0:
        raise ValueError('Area must be positive')
