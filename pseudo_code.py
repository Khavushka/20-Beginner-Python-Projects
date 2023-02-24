def generate_association_rules(F, sigma, c):
    # vi har tre parametrer
    # F stå for itemsets med deres support
    # sigma = minimum support 
    # c = minimum confidence

    # initialize association rules
    association_rules = []

    # loop over alle frequent X in F med deres support >= sigma
    for X, support_X in F.items(): 
        if support_X < sigma:
            continue

        # Nested loop, loop over alle ikke tom subsets Y af X
        for Y in powerset(X):
            if Y == X or len(Y) == 0:
                continue

            # Calculate the confidence of the rule Y=>X\Y
            support_Y = F.get(Y, 0)
            confidence = support_X / support_Y

            # Hvis confidence under c, prune all subsets of Y
            if confidence < c:
                for Y_prime in powerset(Y):
                    if len(Y_prime) == 0 or Y_prime == Y:
                        continue
                    association_rules.append((Y_prime, X - Y_prime, support_X, support_Y, confidence))

            else:
                association_rules.append((Y, X - Y, support_X, support_Y, confidence))

        return association_rules
    
    def powerset(s):
        
        # 

        return (set(combo) for r in range(1, len(s)) for combo in combinations(s, r))
