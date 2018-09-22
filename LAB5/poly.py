def poly_add2(poly1, poly2):
    l1 = [round(poly1[0] + poly2[0], 2), round(poly1[1] + poly2[1], 2), round(poly1[2] + poly2[2], 2)]
    return l1


def poly_mult2(poly1, poly2):
    l2 = [poly1[0]*poly2[0], poly1[1]*poly2[0] + poly1[0]*poly2[1], poly1[2]*poly2[0] + poly1[1]*poly2[1] +
          poly1[0]*poly2[2], poly1[2]*poly2[1] + poly1[1]*poly2[2], poly1[2]*poly2[2]]
    return l2
