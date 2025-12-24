class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits=list(zip(timestamp, username, website))
        visits.sort()
        user_sites=defaultdict(list)
        for time,user,site in visits:
            user_sites[user].append(site)

        pattern_users=defaultdict(set)

        for user,sites in user_sites.items():
            patterns = set(combinations(sites, 3))
            for pattern in patterns:
                pattern_users[pattern].add(user)

        max_score=0
        answer=()

        for pattern, users in pattern_users.items():
            score=len(users)
            if score>max_score or (score==max_score and pattern<answer):
                max_score=score
                answer=pattern

        return list(answer)