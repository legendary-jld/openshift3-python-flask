from flask import Blueprint

templatefilters = Blueprint('templatefilters', __name__)


@templatefilters.app_template_filter('date')
def filter_date_formatting(dt, output="readable"):
    if dt is None:
        return ""
    else:
        if output == "readable"
            suffixes = {"st": [1, 21, 31], "nd": [2, 22], "rd": [3, 23]}
            day = int(dt.strftime("%d"))
            if day in suffixes["st"]:
                day_suffix = "st"
            elif day in suffixes["nd"]:
                day_suffix = "nd"
            elif day in suffixes["rd"]:
                day_suffix = "rd"
            else:
                day_suffix = "th"
            formatting = "%b %d{0}, %Y".format(day_suffix)
            return dt.strftime(formatting)
        else:
            return ""
