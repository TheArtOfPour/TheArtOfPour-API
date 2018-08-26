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
            
        eg. list by style
            select s.name, count(r.styleID) as ct
            from styles s
            join recipes r on r.styleID = s.id
            group by styleID
            having count(styleID) > 7000
            order by ct desc;
            
        eg. combined
            select h.id, h.name, count(rh.recipeID) as ct
            from recipe_hops rh
            join hops h on rh.hopID = h.id
            join recipes r on rh.recipeID = r.id
            join recipe_fermentables rf on r.id = rf.recipeID
            join fermentables f on rf.fermentableID = f.id
            where r.styleID = 4 -- american ipa
            and f.id = 27 -- golden promise
            group by rh.hopID
            --having count(styleID) > 2000
            order by ct desc;
        '''

        return []
