class Stats:

    def __init__(self):
        print("init stats")

    @staticmethod
    def stats(request):
        print(request)
        '''
        parse request as a querydsl string
        
        eg. hops by style
            select h.id, h.name, count(rh.recipeID) as ct
            from recipe_hops rh
            join hops h on rh.hopID = h.id
            join recipes r on rh.recipeID = r.id
            where r.styleID = 28
            group by rh.hopID
            --having count(styleID) > 2000
            order by ct desc;
        '''

        return []
