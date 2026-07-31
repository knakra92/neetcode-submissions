class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_by_key: dict[str, list[str]] = {}

        for s in strs:
            key_sorted = ''.join(sorted(s))

            if group_by_key.get(key_sorted):
                group_by_key[key_sorted].append(s)
            else:
                group_by_key[key_sorted] = [s]

        print(group_by_key.values())

        output = []

        for v in group_by_key.values():
            output.append(v)

        return output