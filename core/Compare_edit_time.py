def time_cal(edit_Time, endTime):
    edit_Time = str(edit_Time)
    year_edit = edit_Time[0:4]
    year_end = endTime[0:4]
    month_edit = edit_Time[5:7]
    month_end = endTime[5:7]
    day_edit = edit_Time[8:10]
    day_end = endTime[8:10]

    if int(year_edit) > int(year_end):
        return True
    if int(month_edit) > int(month_end):
        return True
    else:
        if int(year_edit) < int(year_end):
            return False
        elif int(year_edit) == int(year_end):
            if int(month_edit) < int(month_end):
                return False
            elif int(month_edit) >= int(month_end):
                if int(day_edit) < int(day_end):
                    return False
                elif int(day_edit) >= int(day_end):
                    return True