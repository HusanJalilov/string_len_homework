def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    x=len(s1)%2
    y=len(s2)%2
    z=len(s3)%2
    if x!=0 and y!=0 and z!=0:
        return "["+s1+" "+s2+", "+s3+"]"
    elif x!=0 and y!=0:
        return "["+s1+", "+s2+"]"
    elif y!=0 and z!=0:
        return "["+s2+", "+s3+"]"
    elif x!=0:
        return "["+s1+"]"
    elif y!=0:
        return "["+s2+"]"
    elif z!=0:
        return "["+s3+"]"
    else:
        return "[]"
        