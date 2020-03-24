import datetime


def next_code(model, field):

    current_year = datetime.datetime.now().year
    year = str(current_year)[2:4]

    try:
        latest = model.objects.latest(field)
        last_year = latest.number[0:2]
    except:
        latest = None
        last_year = None

    if not latest or last_year != year:
        return year+'0001'

    return str(int(latest.number)+1)
