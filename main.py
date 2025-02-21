import math

def format_views(num_of_views):
    if num_of_views < 0:
        raise ValueError("Views cannot be negative")
    elif num_of_views == 0 or num_of_views == None:
        return "No Views"
    elif num_of_views == 1:
        return "1 View"
    elif num_of_views > 0 and num_of_views < 1000:
        return f"{num_of_views} Views"
    elif num_of_views >= 1000 and num_of_views < 10000:
        prefix = num_of_views // 1000
        suffix = num_of_views % 1000

        suffix_tens_place_decimal = suffix // 10 / 10

        if suffix_tens_place_decimal >= 5 and suffix_tens_place_decimal < 9:
            suffix = math.ceil(suffix / 100)
        elif suffix_tens_place_decimal == 9:
            suffix = 9
        else:
            suffix = math.floor(suffix / 100)
        
        return f"{prefix}.{suffix}K Views"
    elif num_of_views >= 10000 and num_of_views < 1000000:
        return f"{num_of_views // 1000}K Views"
    elif num_of_views >= 1000000 and num_of_views < 1000000000:  # million to billion
        return f"{num_of_views // 1000000}M Views"
    elif num_of_views >= 1000000000:
        return f"{num_of_views // 1000000000}B Views"