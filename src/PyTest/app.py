def percentage(Classes_Conducted,total_Classes):
    if total_Classes == 0:
        raise ValueError("Total classes cannot be zero")
    if Classes_Conducted > total_Classes:
        raise ValueError("Classes conducted cannot exceed total classes")
    return Classes_Conducted/total_Classes *100