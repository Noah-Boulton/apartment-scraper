import math

# Setup neighbourhood bounding boxes and use bounding box formula to determine which box a listing is in


neighbourhoods = {
                    "Burnaby Heights"                   :   [[49.294669, -122.999776],
                                                            [49.280663, -123.032589]],

                    "Capitol Hill"                      :   [[49.294595, -122.971255],
                                                            [49.280605, -123.000554]],

                    "Brentwood Park"                    :   [[49.281049, -122.968506],
                                                            [49.261929, -123.024536]],

                    "Discovery Park"                    :   [[49.261602, -122.982861],
                                                            [49.245009, -123.025177]],

                    "Garden Village"                    :   [[49.245656, -122.982961],
                                                            [49.234446, -123.025219]],

                    "Metrotown"                         :   [[49.234966, -122.975531],
                                                            [49.219269, -123.03232]],

                    "Renfrew"                           :   [[49.25214, -123.023765],
                                                            [49.232642, -123.076496]],

                    "Hastings-Sunrise"                  :   [[49.292917, -123.023952],
                                                            [49.250147, -123.057239]],

                    "Grandview-Woodland"                :   [[49.292483, -123.055921],
                                                            [49.249753, -123.080183]],

                    "Olympic Village-Mount Pleasant"    :   [[49.270699, -123.082986],
                                                            [49.248516, -123.14044]],

                    "Downtown"                          :   [[49.297016, -123.092285],
                                                            [49.270318, -123.149788]]
                }

def area(coords):
    area = "Vancouver"
    for neighbourhood in neighbourhoods:
        box = neighbourhoods[neighbourhood]
        if (box[0][0] > coords[0] > box[1][0]) and (box[1][1] < coords[1] < box[0][1]):
            area = neighbourhood
    return area