#2
filter_set = lambda s: (
    set()
    if not s
    else(lambda avg:{x for x in s})
)